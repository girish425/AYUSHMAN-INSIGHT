import sqlite3

def init_db():
    conn = sqlite3.connect("claims.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS claims (
            claim_id INTEGER,
            hospital TEXT,
            procedure TEXT,
            cost REAL,
            risk_score REAL,
            fraud_types TEXT
        )
    """)
    conn.commit()
    conn.close()
