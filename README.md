## Execution Instructions
This guide explains how to build the Docker image and run the container to process a collection of PDFs.

Prerequisites
Docker Desktop must be installed and running.

Step 1: Folder Arrangement
Before running the commands, ensure your input folder is structured correctly. The input folder must be in the same directory as your Dockerfile.

### 📁 Folder Structure

```
<project_root>/
├── input/
│   ├── pdfs/
│   │   └── (Place all your PDFs for analysis here)
│   └── persona.json         # Contains persona and job-to-be-done details
│
├── output/
│   └── (Leave this folder empty; results will be written here)
│
└── Dockerfile
```


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
