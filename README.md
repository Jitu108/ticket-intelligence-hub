<!--# ticket-intelligence-hub

# python -m ticket_hub.ui.app
-->

# 🎫 Ticket Intelligence Hub

**Ticket Intelligence Hub (TIH)** is an **AI-powered support analytics platform** that consolidates helpdesk, engineering, and QA tickets from multiple sources, analyzes them using **LLM-based contextual intelligence**, and provides insights into **patterns, prioritization, and efficiency improvement** across sprints or releases.

---

## 🚀 Overview

Modern product teams manage thousands of tickets across Jira, GitHub, Zendesk, or internal tools. Manual triage, duplicate detection, and root-cause identification often consume hours.  
Ticket Intelligence Hub automates this by combining:

- **Data ingestion** (SQL Server + APIs)
- **Natural Language Understanding (LLM)**
- **Smart analytics (effort, scope creep, iteration trends)**
- **Interactive Gradio UI for visualization**
- **AI agent workflows for summarization and RCA**

---

## 🧩 Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Database** | SQL Server | Store tickets, comments, iterations, and metrics |
| **Backend Logic** | Python 3.11+ | Core business logic and analytics engine |
| **ORM/DB Access** | pyodbc / SQLAlchemy | Database interaction |
| **LLM Engine** | OpenAI / Ollama | Summarization, classification, and insights |
| **Vector Indexing** | FAISS | Semantic similarity and duplicate detection |
| **Frontend/UI** | Gradio | Web-based dashboard and analytics UI |
| **Deployment** | Docker / Docker Compose | Containerized deployment for reproducibility |

---

## 📁 Project Structure
```
ticket_intelligence_hub/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── .env.example
│
├── init.py
├── config/
│   └── settings.py
├── infrastructure/
│   ├── db.py
│   └── vector_store.py
├── domain/
│   ├── models.py
│   ├── entities/
│   │   ├── ticket.py
│   │   ├── iteration.py
│   │   └── developer.py
├── services/
│   ├── ticket_service.py
│   ├── analytics_service.py
│   └── llm_service.py
├── ui/
│   └── app.py
├── utils/
│   └── logger.py
├── main.py
│
└── sql/
├── schema.sql
├── seed_data.sql
└── stored_procs/
└── get_ticket_metrics.sql
```
---

## ⚙️ Features

### 🧠 AI-Driven Insights
- **Automatic ticket summarization** using LLMs (OpenAI / Ollama)
- **Root cause analysis** via agentic reasoning
- **Duplicate ticket detection** using vector embeddings (FAISS)
- **Effort estimation** and T-shirt sizing (S/M/L/XL)

### 📊 Sprint & Effort Analytics
- Tracks effort, iterations, scope creep, and rework
- Sprint-to-sprint comparison dashboard
- Developer and team performance summaries

### 🔎 Smart Querying
- Semantic search: “Show me all tickets delayed due to API timeout”
- Context-based recommendations for similar issues

### 🧱 Extensible Architecture
- Plug-and-play data connectors (e.g., Jira, GitHub, or CSV imports)
- Modular design for adding new AI or data modules

---

## 🧰 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/ticket-intelligence-hub.git
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

### 3️⃣ Setup database
```bash
docker-compose up -d sqlserver
sleep 10
sqlcmd -S localhost,1433 -U sa -P YourStrong@Pass123 -i sql/schema.sql
sqlcmd -S localhost,1433 -U sa -P YourStrong@Pass123 -i sql/seed_data.sql
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the application
```bash
python -m ticket_hub.ui.app
```

Access the app at [http://localhost:7860](http://localhost:7860)

---

## 🧠 LLM Workflow

```text
Ticket → LLM Summarizer → Embedding Vectorizer → FAISS Index
           ↓
   AI Classifier → Category / RCA / Priority
           ↓
   Insights Dashboard (Gradio)
```

- **Embedding Strategy:** OpenAI + Local (Fallback)
- **Prompt Templates:** Context-aware summarization and RCA generation
- **FAISS Index:** Used for semantic search and duplicate detection

---

## 📦 Docker Deployment

```bash
docker-compose up --build
```

This launches:
- `sqlserver` (database)
- `tih-app` (Python/Gradio)
- `vector-store` (optional FAISS container)

---

## 🧭 Roadmap

- [ ] Integrate Jira / GitHub connectors  
- [ ] Add multi-tenant capability (PlanId, TeamId)  
- [ ] Include automated RCA scoring  
- [ ] Introduce Slack/Email notifications  
- [ ] Add dashboard filters by project, module, or sprint  

---

## 🧑‍💻 Contributing

We welcome contributions!  
1. Fork the repo  
2. Create a feature branch (`feature/ai-insight`)  
3. Commit changes  
4. Submit a PR  

---

## 📜 License

MIT License © 2025 Ticket Intelligence Hub Contributors
