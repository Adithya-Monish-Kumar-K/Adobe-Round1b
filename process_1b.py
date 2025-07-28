import json
from pathlib import Path
from sentence_transformers import SentenceTransformer, util
import datetime
import os
import torch
import fitz
import re
from collections import defaultdict
import numpy as np

# --- IMPORT THE ROUND 1A LOGIC ---
try:
    from process_pdfs import run_pipeline_sequential as run_1a_pipeline
    from process_pdfs import load_models as load_1a_models
except ImportError:
    print("❌ Error: Could not import 'process_pdfs.py'. Make sure your Round 1A script is in the same directory.")
    exit()

# --- Configuration ---
# Check if fine-tuned model exists, otherwise use base model
MODEL_1B_PATH = 'models/sentence_transformer_finetuned'
if not os.path.exists(MODEL_1B_PATH):
    MODEL_1B_PATH = 'models/sentence-transformer'
    if not os.path.exists(MODEL_1B_PATH):
        MODEL_1B_PATH = 'all-MiniLM-L6-v2'  # Use base model as fallback

# Automatically determine the correct input and output paths
if os.path.exists("/app/input"):
    # We are running inside the Docker container
    DOCS_DIR = Path("/app/input/pdfs")
    PERSONA_FILE = Path("/app/input/persona.json")
    OUTPUT_DIR = Path("/app/output")
else:
    # We are running locally on your computer
    DOCS_DIR = Path("app/input/pdfs")
    PERSONA_FILE = Path("app/input/persona.json")
    OUTPUT_DIR = Path("app/output")
    
DEVICE = 'cpu'

# --- Scoring Weights ---
TITLE_WEIGHT = 0.35
CONTENT_WEIGHT = 0.65

def load_1b_model():
    """Loads the sentence transformer model."""
    print(f"Loading sentence transformer model from {MODEL_1B_PATH}...")
    return SentenceTransformer(MODEL_1B_PATH, device=DEVICE)

def clean_text(text):
    """Clean and normalize text."""
    # Remove excessive whitespace and newlines
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters but keep punctuation
    text = re.sub(r'[^\w\s\.\,\;\:\!\?\-\(\)\[\]]', '', text)
    return text.strip()

def extract_subsections_from_content(content, section_title):
    """
    Extract meaningful subsections from the content based on natural document structure.
    Focus on ingredients, instructions, and recipe components for food-related content.
    """
    subsections = []
    
    # Clean the content first
    content = clean_text(content)
    
    # Food-specific patterns (since your example is food-related)
    ingredients_pattern = r'Ingredients?:\s*(.*?)(?=Instructions?:|Directions?:|Method:|$)'
    instructions_pattern = r'(?:Instructions?|Directions?|Method):\s*(.*?)(?=Ingredients?:|$)'
    
    # Generic patterns for structured content
    recipe_sections = []
    
    # Try to find ingredients sections
    ingredients_match = re.search(ingredients_pattern, content, re.IGNORECASE | re.DOTALL)
    if ingredients_match:
        ingredients_text = ingredients_match.group(1).strip()
        if len(ingredients_text) > 20:
            # Clean up ingredients list
            ingredients_lines = [line.strip() for line in ingredients_text.split('\n') if line.strip()]
            # Take first few ingredients or up to reasonable length
            ingredients_subset = []
            current_length = 0
            for line in ingredients_lines:
                if current_length + len(line) < 300:  # Keep under 300 chars
                    ingredients_subset.append(line)
                    current_length += len(line)
                else:
                    break
            
            if ingredients_subset:
                recipe_sections.append({
                    'type': 'ingredients',
                    'text': ' '.join(ingredients_subset)
                })
    
    # Try to find instructions sections
    instructions_match = re.search(instructions_pattern, content, re.IGNORECASE | re.DOTALL)
    if instructions_match:
        instructions_text = instructions_match.group(1).strip()
        if len(instructions_text) > 20:
            # Split instructions into steps
            steps = re.split(r'(?:\d+\.|\n\s*[•\-\*]|\n\s*[oo])', instructions_text)
            meaningful_steps = []
            
            for step in steps[:5]:  # Take first 5 steps
                step = step.strip()
                if len(step) > 15 and not step.startswith('o'):  # Meaningful step
                    # Clean up step
                    step = re.sub(r'^[•\-\*\s]+', '', step)
                    step = step.replace('o ', '').strip()
                    meaningful_steps.append(step)
            
            if meaningful_steps:
                # Combine first few steps
                combined_steps = '. '.join(meaningful_steps[:3])
                if len(combined_steps) > 50:
                    recipe_sections.append({
                        'type': 'instructions',
                        'text': combined_steps[:400] + ('...' if len(combined_steps) > 400 else '')
                    })
    
    # If we found recipe-specific content, use it
    if recipe_sections:
        return recipe_sections
    
    # Fallback: Generic content chunking
    # Look for bullet points or numbered lists
    bullet_pattern = r'(?:^|\n)\s*[•\-\*o]\s+([^\n]+)'
    bullets = re.findall(bullet_pattern, content, re.MULTILINE)
    
    if len(bullets) >= 3:
        # Group bullets into meaningful chunks
        chunk_size = min(5, len(bullets))
        bullet_text = ' '.join(bullets[:chunk_size])
        if len(bullet_text) > 50:
            subsections.append({
                'type': 'list',
                'text': bullet_text[:400] + ('...' if len(bullet_text) > 400 else '')
            })
    
    # If still no subsections, create paragraph chunks
    if not subsections:
        sentences = re.split(r'(?<=[.!?])\s+', content)
        meaningful_sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        if meaningful_sentences:
            # Take first 3-5 sentences as a chunk
            chunk_size = min(5, len(meaningful_sentences))
            chunk_text = ' '.join(meaningful_sentences[:chunk_size])
            
            if len(chunk_text) > 50:
                subsections.append({
                    'type': 'content',
                    'text': chunk_text[:500] + ('...' if len(chunk_text) > 500 else '')
                })
    
    return subsections

def extract_content_for_heading(pdf_path, heading_item, full_outline_items):
    """
    Extracts the full text content for a specific heading from a PDF.
    """
    doc = fitz.open(pdf_path)
    content = ""
    
    start_page = heading_item['page']
    start_text = heading_item['text']
    
    # Find current heading index
    current_index = None
    for i, item in enumerate(full_outline_items):
        if item['text'] == start_text and item['page'] == start_page:
            current_index = i
            break
    
    if current_index is None:
        doc.close()
        return ""
    
    # Determine end boundary
    end_page = len(doc)
    next_heading = None
    
    if current_index + 1 < len(full_outline_items):
        next_item = full_outline_items[current_index + 1]
        next_heading = next_item['text']
        if next_item['page'] == start_page:
            end_page = start_page
        else:
            end_page = next_item['page'] - 1
    
    # Extract content
    for page_num in range(start_page - 1, min(end_page, len(doc))):
        page = doc[page_num]
        page_text = page.get_text("text")
        
        if page_num == start_page - 1:
            # First page - find start position
            start_pos = page_text.find(start_text)
            if start_pos != -1:
                start_pos += len(start_text)
                
                # Check if there's a next heading on same page
                if next_heading and page_num == end_page - 1:
                    end_pos = page_text.find(next_heading, start_pos)
                    if end_pos != -1:
                        content += page_text[start_pos:end_pos]
                    else:
                        content += page_text[start_pos:]
                else:
                    content += page_text[start_pos:]
        elif page_num < end_page - 1:
            # Middle pages - take full content
            content += "\n" + page_text
        else:
            # Last page - check for next heading
            if next_heading:
                end_pos = page_text.find(next_heading)
                if end_pos != -1:
                    content += "\n" + page_text[:end_pos]
                else:
                    content += "\n" + page_text
            else:
                content += "\n" + page_text
    
    doc.close()
    return content

def calculate_relevance_with_context(query_embedding, section, model, persona_role, job_task):
    """
    Calculate relevance score with contextual understanding.
    """
    # Create different query variations for better matching
    queries = [
        f"{persona_role}: {job_task}",
        job_task,
        f"As a {persona_role}, I need to {job_task}",
        f"Find information about {job_task} for {persona_role}"
    ]
    
    # Encode all query variations
    query_embeddings = model.encode(queries, convert_to_tensor=True)
    
    # Encode section title
    title_embedding = model.encode(section['section_title'], convert_to_tensor=True)
    
    # Calculate title relevance (max across all query variations)
    title_scores = util.pytorch_cos_sim(query_embeddings, title_embedding)
    title_score = torch.max(title_scores).item()
    
    # Encode content (in chunks if too long)
    content = section['text']
    max_length = 512
    
    if len(content) > max_length:
        # Split content into overlapping chunks
        chunks = []
        step = max_length // 2
        for i in range(0, len(content), step):
            chunks.append(content[i:i + max_length])
        
        chunk_embeddings = model.encode(chunks, convert_to_tensor=True)
        content_scores = util.pytorch_cos_sim(query_embeddings[0], chunk_embeddings)
        content_score = torch.max(content_scores).item()
    else:
        content_embedding = model.encode(content, convert_to_tensor=True)
        content_scores = util.pytorch_cos_sim(query_embeddings[0], content_embedding)
        content_score = content_scores[0].item()
    
    # Calculate subsection relevance if available
    subsection_score = 0
    if 'subsections' in section and section['subsections']:
        subsection_texts = [sub['text'] for sub in section['subsections'][:5]]  # Top 5 subsections
        if subsection_texts:
            subsection_embeddings = model.encode(subsection_texts, convert_to_tensor=True)
            sub_scores = util.pytorch_cos_sim(query_embeddings[0], subsection_embeddings)
            subsection_score = torch.max(sub_scores).item()
    
    # Combined score with dynamic weights
    if subsection_score > 0:
        combined_score = (title_score * TITLE_WEIGHT + 
                         content_score * CONTENT_WEIGHT * 0.7 + 
                         subsection_score * 0.3)
    else:
        combined_score = (title_score * TITLE_WEIGHT + content_score * CONTENT_WEIGHT)
    
    return combined_score, title_score, content_score, subsection_score

def run_full_pipeline(models_1a, model_1b):
    """Executes the full pipeline for Round 1B."""
    
    # Load persona and job
    if PERSONA_FILE.exists():
        print(f"Loading persona from {PERSONA_FILE}...")
        with open(PERSONA_FILE, 'r', encoding='utf-8') as f:
            persona_data = json.load(f)
        
        # Handle different formats in the persona file
        if isinstance(persona_data.get("persona"), dict):
            persona_role = persona_data["persona"].get("role", "")
        else:
            persona_role = persona_data.get("persona", "")
            
        if isinstance(persona_data.get("job_to_be_done"), dict):
            job_task = persona_data["job_to_be_done"].get("task", "")
        else:
            job_task = persona_data.get("job_to_be_done", "")
    else:
        print("\n--- Interactive Mode: persona.json not found ---")
        persona_role = input("Enter the Persona (e.g., Travel Planner): ")
        job_task = input("Enter the Job to be Done (e.g., Plan a 4-day trip): ")

    print(f"\nPersona: {persona_role}")
    print(f"Job to be done: {job_task}")

    print("\n--- Step 1: Extracting Document Structure and Content ---")
    pdf_files = list(DOCS_DIR.glob("*.pdf"))
    if not pdf_files:
        print("No PDF files found!")
        return {}
    
    all_sections = []
    
    # Process each PDF
    for pdf_file in pdf_files:
        print(f"Processing {pdf_file.name}...")
        try:
            # Get outline from Round 1A
            outline_json = run_1a_pipeline(pdf_file, *models_1a)
            
            # Build full outline
            full_outline_items = []
            if outline_json.get("title"):
                full_outline_items.append({
                    "document": pdf_file.name,
                    "page": 1,
                    "text": outline_json["title"],
                    "level": "Title"
                })
            
            for item in outline_json.get("outline", []):
                full_outline_items.append({
                    "document": pdf_file.name,
                    "page": item['page'],
                    "text": item['text'],
                    "level": item.get('level', 'H1')
                })

            # Extract content and subsections for each heading
            for heading_item in full_outline_items:
                content = extract_content_for_heading(pdf_file, heading_item, full_outline_items)
                
                if content and len(content) > 50:  # Minimum content length
                    # Extract subsections from the content
                    subsections = extract_subsections_from_content(content, heading_item['text'])
                    
                    section_data = {
                        "document": pdf_file.name,
                        "page": heading_item['page'],
                        "section_title": heading_item['text'],
                        "text": content,
                        "level": heading_item.get('level', 'H1'),
                        "subsections": subsections
                    }
                    all_sections.append(section_data)
                    
        except Exception as e:
            print(f"Error processing {pdf_file.name}: {str(e)}")
            continue
    
    if not all_sections:
        print("No sections extracted!")
        return {}

    print(f"\n--- Step 2: Analyzing Relevance for {len(all_sections)} sections ---")
    
    # Create query embedding
    query = f"{persona_role}: {job_task}"
    query_embedding = model_1b.encode(query, convert_to_tensor=True)
    
    # Calculate relevance scores
    for section in all_sections:
        combined_score, title_score, content_score, subsection_score = calculate_relevance_with_context(
            query_embedding, section, model_1b, persona_role, job_task
        )
        
        section['relevance_score'] = combined_score
        section['title_score'] = title_score
        section['content_score'] = content_score
        section['subsection_score'] = subsection_score
    
    # Sort by relevance
    ranked_sections = sorted(all_sections, key=lambda x: x['relevance_score'], reverse=True)
    
    print("\n--- Step 3: Generating Output ---")
    
    # Prepare output
    output_data = {
        "metadata": {
            "input_documents": [p.name for p in pdf_files],
            "persona": persona_role,
            "job_to_be_done": job_task,
            "processing_timestamp": datetime.datetime.now().isoformat()
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    # Select top sections (let's take top 5 as shown in the example)
    top_sections = ranked_sections[:5]
    
    for i, section in enumerate(top_sections):
        # Add to extracted_sections
        output_data["extracted_sections"].append({
            "document": section["document"],
            "section_title": section["section_title"],
            "importance_rank": i + 1,
            "page_number": section["page"]
        })
        
        # For subsection_analysis, we need to provide refined text
        # Create coherent, readable refined text from the section content
        refined_text = ""
        
        if section.get('subsections') and section['subsections']:
            # Use subsections to create refined text
            refined_parts = []
            
            # Prioritize different types of subsections
            ingredients_sections = [s for s in section['subsections'] if s.get('type') == 'ingredients']
            instruction_sections = [s for s in section['subsections'] if s.get('type') == 'instructions']
            other_sections = [s for s in section['subsections'] if s.get('type') not in ['ingredients', 'instructions']]
            
            # Add ingredients first if available
            if ingredients_sections:
                refined_parts.append(ingredients_sections[0]['text'])
            
            # Add instructions if available
            if instruction_sections:
                refined_parts.append(instruction_sections[0]['text'])
            
            # Add other sections if needed
            for subsection in other_sections[:2]:  # Max 2 additional sections
                if len(' '.join(refined_parts)) < 600:  # Keep under reasonable length
                    refined_parts.append(subsection['text'])
            
            refined_text = ' '.join(refined_parts)
        
        # Fallback: extract meaningful content directly from the section text
        if not refined_text or len(refined_text) < 100:
            content_text = section['text']
            
            # Try to extract a coherent beginning of the content
            # Look for complete sentences or instructions
            sentences = re.split(r'(?<=[.!?])\s+', content_text)
            meaningful_sentences = []
            
            for sentence in sentences:
                sentence = sentence.strip()
                if len(sentence) > 15:  # Meaningful sentence length
                    meaningful_sentences.append(sentence)
                    # Stop when we have enough content
                    if len(' '.join(meaningful_sentences)) > 400:
                        break
            
            if meaningful_sentences:
                refined_text = ' '.join(meaningful_sentences[:7])  # Max 7 sentences
            else:
                # Last resort: take first part of content
                refined_text = content_text[:500]
        
        # Clean up the refined text
        refined_text = clean_text(refined_text)
        
        # Ensure reasonable length
        if len(refined_text) > 800:
            # Try to cut at sentence boundary
            sentences = re.split(r'(?<=[.!?])\s+', refined_text[:800])
            if len(sentences) > 1:
                refined_text = ' '.join(sentences[:-1]) + "..."
            else:
                refined_text = refined_text[:800] + "..."
        
        # Ensure minimum length
        if len(refined_text) < 50:
            refined_text = section['text'][:300] + ("..." if len(section['text']) > 300 else "")
        
        output_data["subsection_analysis"].append({
            "document": section["document"],
            "refined_text": refined_text,
            "page_number": section["page"]
        })
    
    # Debug output
    print("\nTop 5 sections by relevance:")
    for i, section in enumerate(top_sections):
        print(f"{i+1}. {section['section_title']} (Score: {section['relevance_score']:.3f})")
        print(f"   - Title: {section['title_score']:.3f}, Content: {section['content_score']:.3f}, Subsection: {section['subsection_score']:.3f}")
    
    return output_data

def main():
    """Main execution function."""
    print("=== Round 1B: Persona-Driven Document Intelligence ===")
    
    # Load models
    print("\nLoading models...")
    models_1a = load_1a_models()
    model_1b = load_1b_model()
    
    # Run pipeline
    result = run_full_pipeline(models_1a, model_1b)
    
    if result:
        # Save output
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_file = OUTPUT_DIR / "result.json"
        
        with open(output_file, "w", encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
            
        print(f"\n✅ Pipeline complete. Output saved to {output_file}")
        
        # Validate output format
        required_keys = ["metadata", "extracted_sections", "subsection_analysis"]
        if all(key in result for key in required_keys):
            print("✅ Output format validated successfully")
        else:
            print("❌ Warning: Output format may be incorrect")
    else:
        print("\n❌ Pipeline failed to generate results.")

if __name__ == '__main__':
    main()