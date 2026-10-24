# Local PDF RAG Chatbot — On-Device Knowledge Retrieval

A fully local Retrieval-Augmented Generation system for PDF ingestion 
and conversational Q&A. Runs entirely on-device — no external API 
calls, no cloud dependency, no data leaving the machine.

Built for industrial and enterprise environments where engineering 
documents, maintenance records, and technical manuals contain 
information that cannot be processed by external services.

---

## Why local matters

Cloud-hosted LLMs require data to leave the machine. In manufacturing, 
aviation, and industrial settings — where documents contain proprietary 
specifications, sensor data, CTQ records, and operational intelligence 
— that is not an option.

This system delivers RAG capability entirely within a local environment. 
The architecture makes GenAI viable where cloud deployment is not.

---

## Architecture
PDF Input
│
▼
Document Loading (PyPDF / LangChain)
│
▼
Text Chunking (RecursiveCharacterTextSplitter)
│
▼
Embedding Generation (all-MiniLM-L6-v2, local)
│
▼
Vector Store (ChromaDB, persistent local storage)
│
▼
Semantic Retrieval (top-k relevant chunks)
│
▼
Answer Generation (Mistral-7B quantized .gguf, local inference)
│
▼
Gradio Interface (local UI, browser-accessible)

---

## Stack

| Component | Technology |
|---|---|
| LLM | Mistral-7B (quantized .gguf — local inference, no API) |
| Embeddings | all-MiniLM-L6-v2 (SentenceTransformers, local) |
| Vector Store | ChromaDB (persistent local storage) |
| Orchestration | LangChain |
| PDF Processing | PyPDF / LangChain document loaders |
| Interface | Gradio |

---

## Key design decisions

**Mistral-7B quantized** — delivers substantively better answer 
quality than lightweight cloud-viable models (e.g. Flan-T5) while 
remaining runnable on consumer hardware without a GPU, using 
quantized .gguf format via ctransformers.

**ChromaDB over FAISS** — persistent vector storage means embeddings 
are computed once and reused across sessions. FAISS rebuilds in-memory 
on every run; ChromaDB persists to disk, which matters for large 
document collections.

**Fully local execution** — every component runs on-device. No 
internet connection required after initial setup. No data leaves 
the machine at any point.

---

## Quickstart

**1. Create and activate a virtual environment**

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure the application**

```bash
cp config.example.yaml config.yaml
```

Edit `config.yaml` to set your local model path and any other 
parameters.

**4. Download the model**

```bash
./scripts/download_model.sh
```

Or manually place your quantized `.gguf` model file into `models/` 
and update `config.yaml` accordingly. See `models/README.md` for 
model selection guidance.

> Model binaries are not included in this repository. A quantized 
> Mistral-7B .gguf file (~4GB) is required. Recommended: 
> `mistral-7b-instruct-v0.1.Q4_K_M.gguf` from Hugging Face.

**5. Run the notebook**

Open `1_IM_PDF_QAbot.ipynb` in Jupyter or VS Code and run the cells 
sequentially. The notebook walks through ingestion, embedding, 
retrieval, and generation with inline explanations.

Alternatively, launch the Gradio interface directly:

```bash
python app_gradio.py
```

---

## Repository structure
1_IM_PDF_QAchatbot/
├── 1_IM_PDF_QAbot.ipynb # Main notebook — full pipeline walkthrough
├── app_gradio.py # Standalone Gradio app (optional)
├── config.example.yaml # Configuration template
├── requirements.txt # Python dependencies
├── scripts/
│ └── download_model.sh # Model download helper
└── README.md

---

## Comparison with the Cloud-Ready variant

This project is one of two RAG implementations in this repository. 
The companion project 
([`2_CloudReady_KnowledgeAssistant`](../2_CloudReady_KnowledgeAssistant)) 
deploys the same core pipeline on Hugging Face Spaces — accessible 
to anyone, no local setup required, but constrained by free-tier 
CPU hardware and a lighter model.

| Dimension | This project (Local) | Cloud variant |
|---|---|---|
| Model | Mistral-7B (quantized) | Flan-T5 (250M) |
| Answer quality | High | Constrained by hardware |
| Data privacy | Complete — no external calls | Data sent to HF Spaces |
| Setup required | Yes — local environment | None — browser only |
| Infrastructure cost | None after setup | Free tier |
| Use case | Industrial / enterprise / private docs | Demonstration / accessibility |

The right choice depends on the constraint that matters most: 
privacy and accuracy, or accessibility and zero setup.

---

## Author

**Sumedh Bhalerao**  
Data Science Lead | Industrial AI & IoT | Generative AI | 
Engineering-Domain ML

[LinkedIn](https://linkedin.com/in/sumedh-bhalerao) · 
[GitHub](https://github.com/Sum-BH)

---

*All data used in this project is synthetic or user-supplied at 
runtime. No proprietary datasets, algorithms, or confidential 
information are included in this repository.*
