# PDF RAG Chatbot — IM for PDF Q&A

A local Retrieval-Augmented Generation (RAG) chatbot that ingests PDFs and answers questions using:
- LangChain
- Chroma DB
- All-MiniLM embeddings
- Mistral-7B (quantized .gguf) as the LLM (local)
- Gradio UI (notebook or script)

## Demo
This repository contains the notebook `rag_pdf_chatbot.ipynb` which demonstrates ingestion, embedding, retrieval and Gradio UI locally.

## Quickstart (local)
1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows

##Install dependencies
pip install -r requirements.txt

##Prepare configuration
cp config.example.yaml config.yaml
# Edit config.yaml to set local model path and any other params

##Download model (if using Hugging Face)
./scripts/download_model.sh
#Or manually place your model file into models/ and update config.yaml.

##Run the notebook
Open rag_pdf_chatbot.ipynb in Jupyter or VS Code and run the cells.
Or convert cells into app_gradio.py and run python app_gradio.py to launch the Gradio UI.

##Note - Model binaries are not included. See models/README.md for details.