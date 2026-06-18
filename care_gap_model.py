def detect_care_gap(data):
    score = 0

    # Age risk
    if data["age"] > 60:
        score += 1

    # Missed checkups
    if data["missed_checkups"] >= 2:
        score += 1

    # Chronic disease
    if data["chronic_disease"]:
        score += 1

    # Medication adherence
    if data["medication_adherence"] < 0.7:
        score += 1

    # Decision rule
    if score >= 2:
        return True
    else:
        return False