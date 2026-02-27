import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="ClaimGuard", layout="wide")

st.title("🛡️ ClaimGuard – Ayushman Bharat Fraud Monitoring")

data = requests.get("http://127.0.0.1:5000/claims").json()
df = pd.DataFrame(data)

# --- METRICS ---
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Claims", len(df))
col2.metric("Flagged Claims", df[df['risk_score'] > 0.5].shape[0])
col3.metric("High Risk Hospitals", df[df['risk_score'] > 0.7]['hospital'].nunique())
col4.metric("Amount at Risk (₹)", int(df[df['risk_score'] > 0.5]['cost'].sum()))

# --- CLAIM TREND ---
st.subheader("📈 Claims Trend")
plt.figure()
plt.plot(df.index, df['cost'])
st.pyplot(plt)

# --- FRAUD TYPES ---
st.subheader("🚨 Fraud Type Distribution")
fraud_counts = df['fraud_types'].explode().value_counts()
plt.figure()
fraud_counts.plot(kind='pie', autopct='%1.1f%%')
st.pyplot(plt)

# --- TABLE ---
st.subheader("🧾 Detailed Claims")
st.dataframe(df)
