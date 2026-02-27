from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
from openai import OpenAI

app = Flask(__name__)

# Load ML model
model = joblib.load("backend/fraud_model.pkl")

# Load OpenAI client (Make sure API key is set in environment)
client = OpenAI(api_key="sk-your-real-key-here")

@app.route("/")
def home():
    return {"message": "Fraud Detection Backend Running"}

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    df = pd.DataFrame(data)

    required_cols = ["treatment_cost", "approved_amount", "length_of_stay"]

    if not all(col in df.columns for col in required_cols):
        return jsonify({"error": "Missing required columns"}), 400

    # -------------------------------
    # 1️⃣ RULE-BASED DETECTION
    # -------------------------------

    # Upcoding: Approved amount 40% higher than treatment
    df["upcoding_flag"] = df["approved_amount"] > df["treatment_cost"] * 1.4

    # Ghost billing: Very short stay
    df["ghost_billing_flag"] = df["length_of_stay"] <= 1

    # -------------------------------
    # 2️⃣ ML FRAUD PREDICTION
    # -------------------------------

    X = df[required_cols]
    df["ml_fraud_prediction"] = model.predict(X)
    df["risk_score"] = model.predict_proba(X)[:, 1] * 100

    # -------------------------------
    # 3️⃣ LLM SUMMARY
    # -------------------------------

    fraud_cases = df[df["ml_fraud_prediction"] == 1].head(5)

    summary_text = "No high risk fraud detected."

    if len(fraud_cases) > 0:
        prompt = f"""
        Analyze the following healthcare insurance claim fraud data.
        Focus on upcoding and ghost billing patterns.
        Provide a short audit summary and risk recommendation.

        Data:
        {fraud_cases.to_string()}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        summary_text = response.choices[0].message.content

    return jsonify({
        "analysis_data": df.to_dict(orient="records"),
        "llm_summary": summary_text
    })

if __name__ == "__main__":
    app.run(debug=True)
