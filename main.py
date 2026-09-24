import os
import pandas as pd
from supabase import create_client, Client
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from fastapi import FastAPI
from pydantic import BaseModel

# ==========================================
# 1. FETCH DATA & TRAIN MODEL
# ==========================================
SUPABASE_URL = os.environ.get("SUPABASE_URL",SUPABASE_URL1 )
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", SUPABASE_KEY1)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Fetching data from Supabase...")
response = supabase.table('customers').select("*").execute()
df = pd.DataFrame(response.data)

# Features and Target
X = df[['mrr', 'days_since_last_login', 'active_users_count', 'support_ticket_volume']]
y = df['churned'].astype(int)

print("Training Ensemble Model...")
model1 = RandomForestClassifier(n_estimators=50, random_state=42)
model2 = GradientBoostingClassifier(n_estimators=50, random_state=42)
model3 = LogisticRegression(max_iter=1000)

ensemble_model = VotingClassifier(
    estimators=[('rf', model1), ('gb', model2), ('lr', model3)],
    voting='soft'
)
ensemble_model.fit(X, y)
print("✅ Model trained successfully!")

# ==========================================
# 2. FASTAPI SETUP
# ==========================================
app = FastAPI(title="Lead Enrichment Engine")

# Data validation model for incoming requests
class CustomerStats(BaseModel):
    mrr: float
    days_since_last_login: int
    active_users_count: int
    support_ticket_volume: int

@app.post("/predict")
async def predict_churn(customer: CustomerStats):
    # Convert input to DataFrame for the model
    input_data = pd.DataFrame([customer.dict()])
    
    # Predict probability of churn (Class 1)
    churn_prob = ensemble_model.predict_proba(input_data)[0][1]
    
    # Return the score to Fastn
    return {
        "churn_risk_score": float(churn_prob),
        "is_high_risk": bool(churn_prob > 0.85)
    }