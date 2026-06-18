from care_gap_model import detect_care_gap

print("AI Care Gap Detection System")

# sample patient data
patient_data = {
    "age": 65,
    "missed_checkups": 3,
    "chronic_disease": True,
    "medication_adherence": 0.6
}

result = detect_care_gap(patient_data)

print("\nResult:")
print("Care Gap Found:" if result else "No Care Gap Found")