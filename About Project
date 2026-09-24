# 🚀 Predictive Lead Enrichment & Churn Rescue Engine

**An autonomous, event-driven retention engine that instantly correlates customer support complaints with financial telemetry to predict churn and automatically draft rescue offers.**

---

## 💡 The Problem
SaaS companies frequently lose high-value accounts because customer support friction is rarely correlated with financial telemetry in real-time. By the time a Customer Success Manager (CSM) identifies a flight risk, the customer has already decided to churn. Support is reactive, not proactive.

## 🎯 Our Solution
This project introduces an autonomous retention engine that catches churn before it happens. 

When a customer emails a complaint, the system intercepts the message, cross-references the user against real-time CRM data, runs an Ensemble Voting Machine Learning model to calculate churn risk, and automatically dispatches an AI-drafted rescue email (with a targeted incentive) to the CS team—all in sub-second latency.

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
* **Backend Microservice:** Python, FastAPI, Uvicorn, Ngrok
* **Machine Learning:** Scikit-Learn (Random Forest, Gradient Boosting, Logistic Regression)
* **AI / Synthesis:** OpenAI LLM
* **Delivery:** Resend API

---

## 🧠 The Machine Learning Engine

Rather than relying on basic heuristics, the backend utilizes an **Ensemble Voting Classifier** built with `scikit-learn`. 
* The model is trained on synthetic B2B telemetry, identifying complex patterns (e.g., high MRR combined with recent login drops and spiking ticket volumes).
* It is wrapped in a lightweight FastAPI application, enabling rapid inference via a local `/predict` endpoint exposed to Fastn via Ngrok.

---

## 🚀 How to Run Locally (For Judges)

### Prerequisites
* Python 3.9+
* Ngrok installed
* A Supabase project
* Fastn workspace

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
