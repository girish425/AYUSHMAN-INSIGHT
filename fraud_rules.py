def detect_fraud(row):
    frauds = []

    # Upcoding
    if row['cost'] > 1.5 * row['avg_cost']:
        frauds.append("Upcoding")

    # Ghost Billing
    if row['days_admitted'] == 0 and row['cost'] > 10000:
        frauds.append("Ghost Billing")

    # Unbundling
    if row['claims_per_patient'] > 3:
        frauds.append("Unbundling")

    return frauds
