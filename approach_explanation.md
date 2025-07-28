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


## Execution Instructions
This guide explains how to build the Docker image and run the container to process a collection of PDFs.

Prerequisites
Docker Desktop must be installed and running.

Step 1: Folder Arrangement
Before running the commands, ensure your input folder is structured correctly. The input folder must be in the same directory as your Dockerfile.

<project_root>/
├── input/
│   ├── pdfs/
│   │   └── (Place all your PDFs for analysis here)
│   └── persona.json
│
├── output/
│   └── (This folder should be empty; results will appear here)
│
└── Dockerfile
The persona.json file, which contains the persona and job-to-be-done, must be placed directly inside the input folder.

The PDF files for the document collection must be placed inside the input/pdfs/ subfolder.

Step 2: Build the Docker Image
Open your terminal (PowerShell, Command Prompt, or any other terminal) in the project's root directory and run the following command to build the Docker image.

docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .

This command reads the Dockerfile, installs all necessary dependencies, and packages your application into a self-contained image named mysolutionname:somerandomidentifier.

Step 3: Run the Docker Container
Once the image is built successfully, run the following command to process the documents.

On Windows (PowerShell):
docker run --rm -v "${pwd}/input:/app/input:ro" -v "${pwd}/output:/app/output" --network none mysolutionname:somerandomidentifier

On Linux or macOS:
docker run --rm -v "$(pwd)/input:/app/input:ro" -v "$(pwd)/output:/app/output" --network none mysolutionname:somerandomidentifier

This command starts a new container from your image.

The -v flags create a link between your local input and output folders and the /app/input and `/app/inudside the container.

The --network none flag ensures the container runs completely offline, as required.

After the command finishes, the final result.json file will appear in your local output folder.