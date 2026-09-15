import pandas as pd
from pathlib import Path

def analyze_revenue_leakage():
    data_path = Path(__file__).resolve().parent / 'data' / 'saas_revenue_data.csv'
    df = pd.read_csv(data_path)
    df['realized_mrr'] = df['mrr'] * (1 - df['discount_pct'])
    df['leakage_amount'] = df['mrr'] - df['realized_mrr']

    summary = df.groupby('plan_tier').agg(
        total_customers=('customer_id', 'count'),
        gross_mrr=('mrr', 'sum'),
        net_mrr=('realized_mrr', 'sum'),
        total_leakage=('leakage_amount', 'sum'),
        avg_payment_delay=('payment_delays_days', 'mean'),
        churn_rate=('churn_flag', 'mean')
    ).reset_index()

    summary['churn_rate'] = (summary['churn_rate'] * 100).round(2)
    return df, summary

if __name__ == '__main__':
    _, summary = analyze_revenue_leakage()
    print(summary)