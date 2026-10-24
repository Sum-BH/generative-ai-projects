# generative-ai-projects

Applied Generative AI systems engineered at the intersection of 
industrial domain expertise and modern LLM infrastructure. Each 
project is production-structured, independently runnable, and 
grounded in real engineering contexts where domain knowledge shapes 
the AI architecture — not the other way around.

---

## Projects

### 1. Local PDF RAG Chatbot — On-Device Knowledge Retrieval
**[`GenAI_Projects/1_IM_PDF_QAchatbot`](GenAI_Projects/1_IM_PDF_QAchatbot)**

A fully local Retrieval-Augmented Generation system for PDF ingestion 
and conversational Q&A. Runs entirely on-device — no external API 
calls, no cloud dependency, no data leaving the machine.

Designed for industrial and enterprise environments where engineering 
documents, maintenance records, and technical manuals cannot be 
processed by external services. The architecture makes RAG viable 
where cloud-hosted LLMs are not an option.

**Stack**
| Component | Technology |
|---|---|
| LLM | Mistral-7B (quantized .gguf, local inference) |
| Embeddings | all-MiniLM-L6-v2 (SentenceTransformers) |
| Vector Store | ChromaDB |
| Orchestration | LangChain |
| Interface | Gradio |

**Key design decisions**
- Quantized local model eliminates cloud API dependency entirely
- ChromaDB for persistent, queryable vector storage on local filesystem
- Modular pipeline — ingestion, embedding, retrieval, and generation 
  are independently testable components
- Gradio interface designed for non-technical users

---

### 2. Cloud-Ready Knowledge Assistant — Hosted RAG on Free Infrastructure
**[`GenAI_Projects/2_CloudReady_KnowledgeAssistant`](GenAI_Projects/2_CloudReady_KnowledgeAssistant)**

A lightweight RAG chatbot fully deployed on Hugging Face Spaces — 
CPU only, zero infrastructure cost, publicly accessible. Demonstrates 
the same retrieval-augmented generation pattern as Project 1, 
re-architected for cloud deployment constraints: no GPU, no paid 
hosting, no persistent storage.

**Stack**
| Component | Technology |
|---|---|
| LLM | Flan-T5 (google/flan-t5-base via Hugging Face) |
| Embeddings | all-MiniLM-L6-v2 (SentenceTransformers) |
| Vector Store | FAISS (in-memory) |
| Orchestration | LangChain |
| Interface | Gradio |
| Hosting | Hugging Face Spaces (CPU, free tier) |

**Key design decisions**
- FAISS in-memory index suited to stateless, ephemeral cloud execution
- Flan-T5 chosen for CPU-viable inference within free-tier constraints
- Stateless architecture — each session is independent, no 
  server-side persistence required

---

## What this repository demonstrates

**RAG pipeline engineering** — end-to-end design across ingestion, 
chunking, embedding, retrieval, and generation stages

**Architectural decision-making** — deliberate selection of vector 
store, LLM, and deployment target based on operational constraints, 
not default choices

**Local vs cloud deployment** — same core RAG pattern implemented 
across two fundamentally different infrastructure requirements

**Domain-informed design** — both projects originate from real 
engineering contexts where data privacy constraints and offline 
operational requirements shaped the architecture

---

## Engineering context

The local deployment architecture in Project 1 mirrors production 
RAG systems built for engineering knowledge retrieval in industrial 
settings — where proprietary technical documentation, sensor data, 
and operational records require on-premises processing. Understanding 
why the architecture is local is as important as knowing how to 
build it.

---

## Author

**Sumedh Bhalerao**  
Data Science Lead | Industrial AI & IoT | Generative AI | 
Engineering-Domain ML

[LinkedIn](https://linkedin.com/in/sumedh-bhalerao) · 
[GitHub](https://github.com/Sum-BH)

---

*All data used in these projects is synthetic or publicly available. 
No proprietary algorithms, datasets, or confidential information 
are included.*
