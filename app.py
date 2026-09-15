import streamlit as st
import pandas as pd
import plotly.express as px
from analytics_engine import analyze_revenue_leakage

st.set_page_config(page_title="SaaS Revenue Leakage Engine", layout="wide")
st.title("💳 SaaS Revenue Leakage & Churn Anomaly Engine")

try:
    df, summary = analyze_revenue_leakage()
except FileNotFoundError:
    st.error("Data source missing. Run `python generate_data.py` first.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Gross MRR", f"${df['mrr'].sum():,}")
col2.metric("Net Realized MRR", f"${df['realized_mrr'].sum():,.2f}")
col3.metric("Total Revenue Leakage", f"${df['leakage_amount'].sum():,.2f}", delta="-Discount Impact")
col4.metric("Overall Churn Rate", f"{(df['churn_flag'].mean()*100):.1f}%")

st.divider()
st.subheader("Financial Performance Summary by Plan Tier")
st.dataframe(summary, use_container_width=True)

st.divider()
c1, c2 = st.columns(2)

with c1:
    st.subheader("Payment Delays vs. Revenue Leakage")
    fig_scatter = px.scatter(
        df, x='payment_delays_days', y='leakage_amount',
        color='plan_tier', size='support_tickets',
        hover_data=['customer_id']
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with c2:
    st.subheader("API Usage vs. Churn Status")
    fig_hist = px.histogram(df, x='api_usage_calls', color='churn_flag', marginal="rug")
    st.plotly_chart(fig_hist, use_container_width=True)