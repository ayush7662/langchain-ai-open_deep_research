<h1 align="center">📚 Deep Research Django + LangChain Assignment </h1>

## 1️⃣ Project Overview*

This project implements a Deep Research platform using Django REST Framework and LangChain (Gemini LLM).
It allows users to:

Start a deep AI-powered research query

Continue previous research

Upload context files (PDF/TXT) for AI processing

Track research history, cost, and tokens

Trace AI executions using LangChain callbacks


## 2️⃣ Features

Research Execution: Start and continue multi-step AI research using LangChain

PDF / TXT Upload: Extract content and include in research context

Research History: Persist research sessions with summaries and reasoning

Cost & Token Tracking: Track input/output tokens and estimated cost

LangChain Tracing: Debug AI execution using trace_id


# 📁 Project File Structure


| Path / File                | Description                                              |
| -------------------------- | -------------------------------------------------------- |
| `deep_research_backend/`   | Root project directory                                   |
| `core/`                    | Django project configuration                             |
| `core/__init__.py`         | Package initializer                                      |
| `core/settings.py`         | Django settings (apps, middleware, env vars)             |
| `core/urls.py`             | Root URL routing                                         |
| `core/asgi.py`             | ASGI config (async support)                              |
| `core/wsgi.py`             | WSGI config (deployment)                                 |
| `research/`                | Main application handling research logic                 |
| `research/admin.py`        | Admin panel registrations                                |
| `research/apps.py`         | App configuration                                        |
| `research/models.py`       | Database models (ResearchSession, Cost, Documents, etc.) |
| `research/views.py`        | REST APIs (start, continue, upload, history, details)    |
| `research/urls.py`         | Research API routes                                      |
| `research/serializers.py`  | DRF serializers (optional)                               |
| `research/tasks.py`        | Background / async research execution                    |
| `research/ai/`             | LangChain + Open Deep Research integration               |
| `research/ai/graph.py`     | Imported LangGraph workflow (unchanged)                  |
| `research/ai/runner.py`    | Research execution wrapper                               |
| `research/ai/callbacks.py` | LangSmith tracing callbacks                              |
| `research/ai/utils.py`     | Token & cost tracking helpers                            |
| `research/migrations/`     | Database migrations                                      |
| `media/`                   | Uploaded research documents                              |
| `media/research_docs/`     | Stored PDFs / TXT files                                  |
| `venv/`                    | Python virtual environment                               |
| `db.sqlite3`               | SQLite database                                          |
| `manage.py`                | Django CLI entry                                         |
| `.env`                     | Environment variables (API keys, tracing flags)          |
| `.gitignore`               | Git ignored files                                        |
| `requirements.txt`         | Python dependencies                                      |
| `README.md`                | Project documentation                                    |






















## 3️⃣ Setup Instructions
 3.1 Clone the repo

git clone https://github.com/ayush7662/langchain-ai-open_deep_research/tree/main

cd langchain-ai-open_deep_research




## 3.2 Create virtual environment and install dependencies
python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt



## 3.3 Set GEMINI API key

Create a .env file in the root:

GEMINI_API_KEY=your_google_gemini_key_here



## 3.4 Migrate database
python manage.py makemigrations

python manage.py migrate



## 4️⃣ Running the Server
python manage.py runserver


Visit: http://127.0.0.1:8000/ → You should see:

{"message": "Welcome to the Research API"}



# 1️⃣ Create Admin Username & Password (FIRST STEP)
   Run this in terminal:

   python manage.py createsuperuser

 Username: admin
Email: admin@example.com
Password: ********
Password (again): ********



# 5️⃣ Django Admin

Visit: http://127.0.0.1:8000/admin/

Use the superuser credentials created earlier

You can view:

ResearchSession

ResearchSummary

ResearchReasoning

ResearchCost

UploadedDocument



# 6️⃣ API Endpoints

| Endpoint                               | Method | Description                                                                          |
| -------------------------------------- | ------ | ------------------------------------------------------------------------------------ |
| `/api/research/start`                  | POST   | Start a new research session                                                         |
| `/api/research/{research_id}/continue` | POST   | Continue an existing research using previous context                                 |
| `/api/research/{research_id}/upload`   | POST   | Upload PDF/TXT file to be used as research context                                   |
| `/api/research/history`                | GET    | Retrieve research history for the user                                               |
| `/api/research/{research_id}`          | GET    | Get research details including summary, reasoning, token usage, cost, and `trace_id` |



# 6.1 Example: Start Research
POST /api/research/start
Content-Type: application/json

{
  "query": "Impact of AI on healthcare",
  "parent_research_id": null
}



# 6.2 Example: Upload PDF


POST /api/research/1/upload

Content-Type: multipart/form-data

File: research_doc.pdf


# 7️⃣ Testing LangChain in Django Shell

python manage.py shell

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash",
    
    temperature=0.2
)

response = llm.invoke("Say hello from LangChain inside Django")

print(response.content)


✅ Output:

"Hello from LangChain, happily running inside your Django application!"



# 8️⃣ Checking Research Data in Shell
from research.models import ResearchSession, ResearchCost

 List all research sessions
 
for r in ResearchSession.objects.all():

    print(r.id, r.query, r.status)

 Check cost
 
cost = ResearchCost.objects.first()

print(cost.input_tokens, cost.output_tokens, cost.total_cost)




# 9️⃣ Upload & Extract PDF

Upload via /api/research/{research_id}/upload

PDF content is extracted and stored in UploadedDocument.extracted_text

LangChain can utilize this extracted text as input to research queries




# 10. Complete Assignment Testing Checklist

 Run Django server (python manage.py runserver)

 Create superuser and login to admin

 Start research via /api/research/start

 Continue research via /api/research/{research_id}/continue

 Upload PDF to research session /api/research/{research_id}/upload

 View research history /api/research/history

 View research details /api/research/{research_id} (includes cost & trace_id)

 Test LangChain queries in shell



 # 11️⃣ Notes

Only GEMINI_API_KEY is required for LangChain












