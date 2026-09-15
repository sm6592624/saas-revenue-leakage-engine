import pandas as pd
import numpy as np
import os

def generate_saas_data():
    np.random.seed(101)
    n = 1200
    plans = ['Basic', 'Pro', 'Enterprise']
    regions = ['APAC', 'EMEA', 'NAM']

    data = {
        'customer_id': [f"CUST-{5000+i}" for i in range(n)],
        'plan_tier': np.random.choice(plans, n, p=[0.5, 0.35, 0.15]),
        'region': np.random.choice(regions, n),
        'mrr': np.random.choice([29, 99, 499], n, p=[0.5, 0.35, 0.15]),
        'api_usage_calls': np.random.randint(100, 50000, n),
        'support_tickets': np.random.randint(0, 15, n),
        'discount_pct': np.random.choice([0, 0.1, 0.2, 0.5], n, p=[0.6, 0.2, 0.1, 0.1]),
        'payment_delays_days': np.random.randint(0, 45, n),
        'churn_flag': np.random.choice([0, 1], n, p=[0.82, 0.18])
    }
    df = pd.DataFrame(data)
    df.loc[df['discount_pct'] == 0.5, 'revenue_leakage_flag'] = 1
    df['revenue_leakage_flag'] = df['revenue_leakage_flag'].fillna(0).astype(int)

    os.makedirs('data', exist_ok=True)
    df.to_csv('data/saas_revenue_data.csv', index=False)
    print("SaaS dataset generated at data/saas_revenue_data.csv")

if __name__ == '__main__':
    generate_saas_data()