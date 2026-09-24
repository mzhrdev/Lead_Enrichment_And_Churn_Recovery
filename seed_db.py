import random
from faker import Faker
from supabase import create_client, Client

# 1. ADD YOUR CREDENTIALS HERE
SUPABASE_URL = SUPABASE_URL1
SUPABASE_KEY = SUPABASE_KEY1

fake = Faker()
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def generate_b2b_mock_data(num_records=500):
    records = []
    for _ in range(num_records):
        tier = random.choices(['Free', 'Pro', 'Enterprise'], weights=[0.5, 0.3, 0.2])[0]
        mrr = {'Free': 0, 'Pro': 199, 'Enterprise': 999}[tier]
        
        days_since_last_login = random.randint(0, 60)
        active_users_count = random.randint(1, 50) if tier != 'Free' else random.randint(1, 5)
        support_ticket_volume = random.randint(0, 15)
        
        # Synthetic pattern for the ML model to learn
        churn_probability = 0.05
        if days_since_last_login > 30: churn_probability += 0.40
        if support_ticket_volume > 7: churn_probability += 0.30
        if active_users_count < 3 and tier != 'Free': churn_probability += 0.15
            
        records.append({
            "company_name": fake.company(),
            "subscription_tier": tier,
            "mrr": mrr,
            "days_since_last_login": days_since_last_login,
            "active_users_count": active_users_count,
            "support_ticket_volume": support_ticket_volume,
            "churned": random.random() < churn_probability
        })
    return records

print("Generating 500 records of synthetic data...")
mock_data = generate_b2b_mock_data(500)
    
print("Pushing to Supabase...")
response = supabase.table('customers').insert(mock_data).execute()
    
print(f"Successfully inserted {len(response.data)} records!")