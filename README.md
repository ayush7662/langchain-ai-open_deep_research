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



## 3️⃣ Setup Instructions
 3.1 Clone the repo

git clone <repo_url>
cd deep_research_backend




## 3.2 Create virtual environment and install dependencies
python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt




## 3.3 Set GEMINI API key

Create a .env file in the root:

GEMINI_API_KEY=your_google_gemini_key_here


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
Endpoint	Method	Description
/api/research/start	POST	Start a new research session
/api/research/{research_id}/continue	POST	Continue an existing research
/api/research/{research_id}/upload	POST	Upload PDF/TXT for context
/api/research/history	GET	List research history for user
/api/research/{research_id}	GET	Research details (includes summary, reasoning, cost, trace_id)
