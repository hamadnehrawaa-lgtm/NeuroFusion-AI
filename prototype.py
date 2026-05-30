def calculate_risk(hrv, sleep_score, stress_score, genetic_factor):
    risk = (
        (100 - hrv) * 0.30 +
        (100 - sleep_score) * 0.25 +
        stress_score * 0.25 +
        genetic_factor * 0.20
    )
    return round(risk, 2)

risk = calculate_risk(
    hrv=70,
    sleep_score=85,
    stress_score=35,
    genetic_factor=40
)

print("Predicted NeuroFusion Risk:", risk)
