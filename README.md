<!--# ticket-intelligence-hub

# python -m ticket_hub.ui.app
-->

# Ticket Intelligence Hub

**Ticket Intelligence Hub (TIH)** is an **AI-powered support analytics platform** that could consolidate helpdesk, engineering, and QA tickets from multiple sources, analyze them using **LLM-based contextual intelligence**, and provide insights into **patterns, prioritization, and efficiency improvement** across sprints or releases. This is a POC which can be extended in future to be full-fledged and deployable.

---

## Overview

Modern product teams manage thousands of tickets across Jira, GitHub, Zendesk, or internal tools. Manual triage, duplicate detection, and root-cause identification often consume hours.  
Ticket Intelligence Hub is a POC to automate this by combining:

- **Data ingestion** (SQL Server + APIs)
- **Natural Language Understanding (LLM)**
- **Smart analytics (effort, scope creep, iteration trends)**
- **Interactive Gradio UI for visualization**
- **AI agent workflows for summarization and RCA**

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Database** | SQL Server | Store tickets, comments, iterations, and metrics |
| **Backend Logic** | Python 3.11+ | Core business logic and analytics engine |
| **ORM/DB Access** | pyodbc / SQLAlchemy | Database interaction |
| **LLM Engine** | OpenAI / Anthropic / Google / Deepseek | Summarization, classification, and insights |
| **Vector Indexing** | FAISS | Semantic similarity and duplicate detection |
| **Frontend/UI** | Gradio | Web-based dashboard and analytics UI |

---

## Project Structure
```
ticket_intelligence_hub/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── .env.example
├── __init__.py
├── config.py
├── infrastructure/
│   ├── __init__.py
│   ├── db.py
│   ├── embedding.py
│   ├── llm.py
│   ├── mappers.py
│   ├── repository.py
├── domain/
│   ├── __init__.py
│   ├── entities.py
│   ├── events.py
│   ├── value_objects.py
├── application/
│   ├── __init__.py
│   ├── dtos.py
│   ├── notifications.py
│   ├── pipelines.py
│   ├── rules.py
│   ├── services.py
├── ui/
│   └── __init__.py
│   └── app.py

```
---

## Features

### AI-Driven Insights
- **Automatic ticket summarization** using LLMs (OpenAI / Ollama)

---

## Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/jitu108/ticket-intelligence-hub.git
cd ticket-intelligence-hub
```

### 2️⃣ Configure environment
```bash
cp .env.example .env
```

Update `.env` with your values:
```env
SQLSERVER_CONN=Server=localhost,1433;Database=ticket_hub;User Id=sa;Password=YourStrong@Pass123;Encrypt=False
OPENAI_API_KEY=sk-xxxx
```



### 5️⃣ Run the application
```bash
python -m ticket_hub.ui.app
```

Access the app at [http://localhost:7860](http://localhost:7860)

---

## 🧠 LLM Workflow

```text
Ticket → LLM Summarizer → Embedding Vectorizer 
           ↓
   Insights Dashboard (Gradio)
```

- **Embedding Strategy:** OpenAI
- **Prompt Templates:** Context-aware summarization
- **FAISS Index:** Used for semantic search

---

## Contributing

We welcome contributions!  
1. Fork the repo  
2. Create a feature branch (`feature/ai-insight`)  
3. Commit changes  
4. Submit a PR  

---

## 📜 License

MIT License © 2025 Ticket Intelligence Hub Contributors
