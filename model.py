import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

conn = sqlite3.connect("backend/fraud.db")
df = pd.read_sql("SELECT * FROM claims", conn)
conn.close()

X = df[["treatment_cost", "approved_amount", "length_of_stay"]]
y = df["fraud"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "backend/fraud_model.pkl")

print("Model trained successfully!")
