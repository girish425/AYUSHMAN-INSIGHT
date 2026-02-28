# AYUSHMAN-INSIGHT
Ayushman Bharat Fraud Detection Agent


📌 Project Overview
----------------------

Ayushman Insight is an AI-powered healthcare fraud detection system designed to identify suspicious insurance claims under large-scale public health schemes. Healthcare fraud, including up-coding, inflated billing, ghost claims, and abnormal hospitalization patterns, results in significant financial losses and reduced system transparency. This project aims to address these challenges through intelligent analytics, anomaly detection, and automated risk reporting.

The system leverages machine learning techniques to detect unusual claim behavior without requiring labeled fraud datasets. By combining anomaly detection, dynamic risk scoring, hospital-level risk ranking, and AI-generated executive summaries, Ayushman Insight provides a scalable and proactive fraud monitoring framework suitable for public healthcare systems.

🎯 Problem Statement
----------------------

Healthcare insurance programs process thousands of claims daily. Manual auditing is time-consuming, resource-intensive, and often reactive rather than proactive. Fraudulent claims such as inflated billing, unnecessary procedures, repeated short admissions, and abnormal treatment costs are difficult to detect using traditional rule-based systems.

There is a need for an intelligent, automated, and scalable fraud detection mechanism that can:
1)Detect anomalous claims in real-time

2)Prioritize high-risk cases

3)Provide explainable insights

4)Generate executive-level fraud reports

5)Support data-driven auditing

6)Ayushman Insight addresses these challenges using AI-driven analytics.


🚀 Key Features
--------------------
🔍 1. AI-Based Anomaly Detection
-----------------------------

The system uses the Isolation Forest algorithm to detect outliers in healthcare claim data. It identifies abnormal patterns in:
Claim amount
1)Admission duration

2)Patient age trends

3)Repeated claim behaviors

This allows fraud detection without pre-labeled datasets.

📊 2. Dynamic Risk Scoring (0–100 Scale)
-------------------------------------------
Each claim is assigned a dynamic risk score calculated based on:

1)Anomaly strength

2)Claim amount deviation

3)Admission duration deviation

This enables auditors to prioritize high-risk claims efficiently.

🏷 3. Risk Categorization
----------------------------
Claims are categorized into:

1)Low Risk

2)Medium Risk

3)High Risk
This simplifies interpretation and improves decision-making.

🏥 4. Hospital Risk Ranking
------------------------------
The system aggregates risk scores at the hospital level and ranks institutions based on average risk patterns. This helps identify potentially fraudulent providers.

📈 5. Real-Time Analytics Dashboard
--------------------------------------
Built using Streamlit, the dashboard provides:
1)Fraud distribution visualization

2)Risk level breakdown

3)High-risk claims table

4)Hospital ranking view

🤖 6. AI-Generated Executive Fraud Report
-------------------------------------------
Using LLM integration, the system generates professional audit summaries highlighting:
1)Total claims analyzed

2)Fraud percentage

3)High-risk hospitals

4)Recommended actions
This transforms raw analytics into actionable intelligence.

🧠 System Architecture
-----------------------------

The system follows a modular layered architecture:

1)Presentation Layer
   -->Streamlit Web Application
   
   -->Interactive dashboard
   
2)Application Layer
   -->Fraud detection engine
   
   -->Risk scoring module
   
   -->Risk categorization logic
   
   -->Hospital risk aggregation
   
3)Intelligence Layer
   -->Isolation Forest anomaly detection
   
   -->Pattern-based fraud indicators
   
   -->AI report generation
   
4)Data Layer
   -->Synthetic healthcare claim dataset
   
   -->SQLite (optional database integration

⚙️ Technology Stack
----------------------
1)Python

2)Streamlit

3)Scikit-learn

4)Pandas

5)OpenAI API (LLM Reporting)

6) ml model for anomaly detection

📊 How It Works
-----------------
step -1: Synthetic healthcare claim data is generated.

step -2: The Isolation Forest model detects anomalous claims.

step-3: Risk scores are calculated for each claim.

step 4: Claims are categorized by risk level.

step 5: Hospitals are ranked based on aggregate risk.

step 6: An AI-generated executive report is produced.

🎯 Unique Selling Proposition (USP)
--------------------------------------
Ayushman Insight uniquely integrates anomaly detection, dynamic risk intelligence, hospital-level ranking, and automated executive fraud reporting into a single AI-driven system for proactive healthcare fraud prevention.

🌍 Impact & Use Cases
------------------------
This solution can be applied to:

1)Government healthcare insurance schemes

2)Public health auditing bodies

3)Insurance fraud monitoring departments

4)Healthcare regulatory agencies

5)By enabling early detection of suspicious patterns, Ayushman Insight can significantly reduce financial leakage and enhance system transparency.
