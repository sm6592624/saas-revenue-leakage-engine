# SaaS Revenue Leakage & Churn Anomaly Engine

Interactive Streamlit dashboard for identifying subscription revenue leakage,
payment delays, and churn anomalies.

## Run Locally

1. Create a virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` or `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Generate the dataset: `python generate_data.py`
5. Start the dashboard: `streamlit run app.py`

## Deploy on Streamlit Cloud

1. Open [Streamlit Community Cloud](https://share.streamlit.io/).
2. Select **New app** and choose the GitHub repository
	`sm6592624/saas-revenue-leakage-engine`.
3. Set the branch to `main` and the main file to `app.py`.
4. Select **Deploy**.

The dataset is included in `data/saas_revenue_data.csv`, so no additional
deployment command is required.

## Deployment Note

This is a Streamlit application and should be deployed on Streamlit Cloud.
Vercel's Python runtime expects a web server entry point such as `app`,
`application`, or `handler`; a Streamlit script is not a Vercel serverless
function.