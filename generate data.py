import pandas as pd
import numpy as np
import sqlite3

np.random.seed(42)
n = 5000

df = pd.DataFrame({
    "patient_id": np.arange(1, n+1),
    "hospital_id": np.random.randint(1, 100, n),
    "treatment_cost": np.random.randint(10000, 200000, n),
    "length_of_stay": np.random.randint(1, 15, n),
})

# Fraud Logic
df["approved_amount"] = df["treatment_cost"] * np.random.uniform(0.9, 1.2, n)

fraud_indices = np.random.choice(n, int(n*0.2), replace=False)
df.loc[fraud_indices, "approved_amount"] *= np.random.uniform(1.5, 2.5)

df["fraud"] = np.where(
    (df["approved_amount"] > df["treatment_cost"] * 1.4) |
    (df["length_of_stay"] <= 1),
    1, 0
)

conn = sqlite3.connect("backend/fraud.db")
df.to_sql("claims", conn, if_exists="replace", index=False)
conn.close()

print("Database created successfully!")
