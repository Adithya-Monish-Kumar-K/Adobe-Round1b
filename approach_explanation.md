# Persona-Driven Document Intelligence: Methodology & Approach

## Overview

This system is designed to extract and rank contextually relevant sections from a set of PDF documents, tailored to a specific user *persona* and *job-to-be-done*. It intelligently combines traditional layout analysis, machine learning classification, and semantic similarity modeling to produce refined, high-quality content recommendations.

## Multi-Stage Pipeline Design

The solution is architected in two synergistic rounds:

### 🔹 Round 1A – Structural Parsing & Semantic Labeling

Using a hybrid of *LightGBM-based layout classifiers* and a *transformer-based sequence classifier*, Round 1A isolates document structure elements such as titles and hierarchical headings (H1–H4). It groups spatially and stylistically similar blocks, enabling robust outline generation even in noisy, unstructured PDFs.

Key techniques:
- Block merging using typographic heuristics.
- Multi-feature scoring (e.g., font size, alignment, boldness).
- Transformer pipeline for semantic label correction.
- Supports both sequential and parallel execution modes.

### 🔹 Round 1B – Semantic Matching & Relevance Scoring

In Round 1B, a fine-tuned SentenceTransformer model is leveraged to semantically match the persona's task with each document section. It combines:
- *Title similarity*
- *Section content embedding*
- *Subsection summarization* (e.g., ingredients/instructions for recipes)

Scores are computed using contextualized embeddings and cosine similarity. The final relevance score is a weighted fusion of title, content, and subsection scores.

Refined textual summaries are generated using natural language chunking, heuristically prioritizing instructional or list-based content over generic paragraphs.

## Model Fine-Tuning

To further enhance relevance detection, a domain-specific variant of all-MiniLM-L6-v2 is trained using curated triplets from annotated corpora. The training data includes:
- Positive examples from ground truth extraction.
- Negative and hard-negative samples across documents.
- Query reformulations and paraphrased augmentations.

Loss function: *CosineSimilarityLoss*  
Evaluation: *EmbeddingSimilarityEvaluator*

This significantly boosts the model’s ability to align abstract personas (e.g., “HR personnel planning onboarding”) with nuanced document segments.

## Output & Robustness

Final output includes:
- Top 5 ranked sections across documents with justification.
- Concise, context-aware summaries for downstream consumption.
- Metadata logging and output schema validation.

The pipeline gracefully falls back to base models if fine-tuned weights are unavailable, ensuring broad usability across environments.

---

*Innovation Highlight:*  
This system doesn't merely extract data — it aligns human intent with document semantics, dynamically adapting to varied personas and domains (legal, culinary, HR, etc.). The modularity, reproducibility, and smart scoring framework make it both technically robust and practically impactful.

