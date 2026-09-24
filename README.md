# 🚀 Predictive Lead Enrichment & Churn Rescue Engine

**An autonomous, event-driven retention engine that instantly correlates customer support complaints with financial telemetry to predict churn and automatically draft rescue offers.**

---

## 💡 The Problem
SaaS companies frequently lose high-value accounts because customer support friction is rarely correlated with financial telemetry in real-time. By the time a Customer Success Manager (CSM) identifies a flight risk, the customer has already decided to churn. Support is reactive, not proactive.

## 🎯 When is this system beneficial?
This codebase and workflow act as the "intelligence bridge" in the customer support lifecycle. It is highly beneficial **immediately after a customer submits a complaint, but before a human agent ever reads it.**

Instead of support tickets sitting in a queue waiting for manual triage, this code:
1. Intercepts the raw complaint.
2. Enriches it with CRM data (MRR, usage metrics).
3. Evaluates it via Machine Learning.
4. Transforms it into a proactive, revenue-saving action plan.

By the time the CSM opens their inbox, the investigation, data gathering, risk assessment, and response drafting are already complete.

---

## 🏗 System Architecture & Data Flow

Our platform is built on a highly decoupled microservices architecture, coordinated by **Fastn**:

1. **Ingestion (`Cloudmailin`):** An angry customer emails our custom support address. Cloudmailin parses the raw payload and hits our Fastn Webhook.
2. **Orchestration (`Fastn`):** Serves as the central nervous system, passing data between the database, the ML microservice, and third-party APIs.
3. **CRM Data Layer (`Supabase`):** Securely fetches critical customer telemetry (MRR, days since last login, lifetime ticket volume).
4. **Prediction Engine (`Python / FastAPI`):** Evaluates the telemetry using a custom Scikit-Learn Ensemble Classifier, returning a real-time `churn_risk_score`.
5. **Context Synthesis (`LLM`):** If the customer is flagged as high-risk, an LLM synthesizes the specific friction points from the raw email and drafts a highly personalized apology with a 20% discount offer.
6. **Alert Dispatch (`Resend`):** Delivers a formatted HTML executive summary and the AI-drafted rescue email directly to the Customer Success team.

---

## 🛠 Tech Stack

* **Orchestration & Workflow:** Fastn
* **Email Ingestion:** Cloudmailin
* **Database / CRM:** Supabase (PostgreSQL)
* **Backend Microservice:** Python, FastAPI, Uvicorn
* **Machine Learning:** Scikit-Learn (Random Forest, Gradient Boosting, Logistic Regression)
* **AI / Synthesis:** OpenAI LLM
* **Delivery:** Resend API

---

## 🧠 The Machine Learning Engine

Rather than relying on basic heuristics, the backend utilizes an **Ensemble Voting Classifier** built with `scikit-learn`. 
* The model is trained on synthetic B2B telemetry, identifying complex patterns (e.g., high MRR combined with recent login drops and spiking ticket volumes).
* It is wrapped in a lightweight FastAPI application, enabling rapid inference via a local `/predict` endpoint.

---

## 🚀 How to Run the Project From Scratch (For Judges & Devs)

Follow these steps to deploy the complete end-to-end architecture on your local machine.

### Prerequisites
* Python 3.9+
* Ngrok installed (Ensure `ngrok.exe` is added to your `.gitignore` if downloaded locally)
* A Supabase project
* Fastn workspace
* Resend API Key

### Step 1: Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
```

### Step 2: Set up the Python Environment
Create an isolated virtual environment and install the required machine learning and API packages.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Configure Environment Secrets
Rename the provided `.env.example` file to `.env` and insert your actual API keys. *(Note: `.env` is gitignored to protect credentials).*
```text
SUPABASE_URL="[https://your-project.supabase.co](https://your-project.supabase.co)"
SUPABASE_KEY="your-supabase-key"
RESEND_API_KEY="re_your_api_key"
```

### Step 4: Seed the Mock CRM Database
Run the database seeding script to populate your Supabase instance with synthetic B2B customer records.
```bash
python seed_db.py
```

### Step 5: Start the ML API & Ngrok Tunnel
Start the local FastAPI server to host the scikit-learn model:
```bash
uvicorn main:app --reload
```
In a **new** terminal window, expose the local server to the internet using Ngrok:
```bash
ngrok http 8000
```
*Copy the generated Ngrok URL (e.g., `https://abc-123.ngrok-free.dev`).*

### Step 6: Configure the Fastn Workflow
1. Go to your Fastn dashboard and import/create the workflow.
2. In the **HTTP Request Node**, paste your Ngrok URL and append `/predict` (e.g., `https://abc-123.ngrok-free.dev/predict`).
3. Ensure the Resend node is configured with your API key.

### Step 7: Trigger the Engine
Send a real email to the configured Cloudmailin address (e.g., "I can't log in and the billing page is broken!"), or use Postman to send a test JSON payload to the Fastn webhook URL. 

Within seconds, the terminal will log the ML prediction, and the drafted rescue email will appear in your Resend-configured inbox.
