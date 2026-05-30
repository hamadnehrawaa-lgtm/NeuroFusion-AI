
import streamlit as st

st.set_page_config(
    page_title="NeuroFusion AI",
    page_icon="🧠",
    layout="wide"
)

def calculate_risk(hrv, sleep, stress, tremor, cardiac, genetic):
    risk = (
        (100 - hrv) * 0.25 +
        (100 - sleep) * 0.20 +
        stress * 0.20 +
        tremor * 0.15 +
        cardiac * 0.10 +
        genetic * 0.10
    )
    return round(min(max(risk, 0), 100), 2)

def alert_level(score):
    if score < 30:
        return "Level 1 - Stable"
    elif score < 55:
        return "Level 2 - Mild Risk"
    elif score < 78:
        return "Level 3 - High Predictive Risk"
    else:
        return "Level 4 - Emergency Warning"

st.title("NeuroFusion AI")
st.subheader("Predicting Human Health Before Symptoms Appear")

st.write("""
NeuroFusion AI is a predictive healthcare prototype that combines smartwatch biosignals,
smartphone behavioral biomarkers, genetic/family history, and adaptive AI to detect
early neurological and cardiovascular risk patterns before symptoms appear.
""")

st.warning(
    "Medical note: This prototype does not diagnose disease. "
    "It only predicts possible risk patterns for preventive support."
)

st.header("Input Signals")

col1, col2, col3 = st.columns(3)

with col1:
    hrv = st.slider("HRV Stability", 0, 100, 75)
    sleep = st.slider("Sleep Recovery", 0, 100, 82)

with col2:
    stress = st.slider("Autonomic Stress Level", 0, 100, 25)
    tremor = st.slider("Micro Tremor / Motion Irregularity", 0, 100, 15)

with col3:
    cardiac = st.slider("Cardiac Strain Index", 0, 100, 20)
    genetic = st.slider("Genetic / Family Risk Weight", 0, 100, 40)

risk_score = calculate_risk(
    hrv=hrv,
    sleep=sleep,
    stress=stress,
    tremor=tremor,
    cardiac=cardiac,
    genetic=genetic
)

level = alert_level(risk_score)

st.header("Prediction Result")

c1, c2 = st.columns(2)

with c1:
    st.metric("Total Preventive Risk", f"{risk_score}%")

with c2:
    st.metric("Alert Level", level)

st.progress(risk_score / 100)

if risk_score < 30:
    st.success("Stable personal baseline. No major deviation detected.")
elif risk_score < 55:
    st.info("Minor deviation detected. Continue monitoring and apply wellness recommendations.")
elif risk_score < 78:
    st.warning("Multiple signals show elevated risk. Medical review is recommended.")
else:
    st.error("Emergency-level warning pattern. Immediate confirmation or support may be needed.")

st.header("Personalized NeuroDigital Twin")

st.write("""
The system compares the user's current signals with their personal baseline.
If heart rhythm, sleep, movement, stress, or phone-behavior patterns deviate from the user's normal range,
NeuroFusion AI raises the risk score and suggests preventive action.
""")

st.header("Risk Targets")

st.markdown("""
- Motor seizure-like event monitoring
- Parkinsonian movement pattern monitoring
- Stroke-like emergency warning
- Acute cardiac warning
- Heart failure strain pattern
- Peripheral circulation risk
- Autonomic nervous-system imbalance
""")
