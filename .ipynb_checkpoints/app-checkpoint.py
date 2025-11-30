import streamlit as st
import joblib

# -----------------------------
# LOAD TRAINED MODEL
# -----------------------------
try:
    model = joblib.load("disease_model.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -----------------------------
# SYMPTOM LIST
# -----------------------------
symptoms = [
    "fever", "cough", "sore_throat", "headache", "fatigue",
    "shortness_breath", "chest_pain", "nausea", "vomiting", "diarrhea"
]

# -----------------------------
# PREVENTION DICTIONARY
# -----------------------------
prevention = {
    "Viral Fever": "• Stay hydrated\n• Rest well\n• Take paracetamol\n• Doctor if fever persists 3+ days",
    "Common Cold": "• Warm fluids\n• Steam inhalation\n• Saltwater gargles\n• Vitamin C",
    "COVID-like Symptoms": "• Self isolate\n• Monitor oxygen\n• Steam inhalation\n• Seek medical help if breathless",
    "Food Poisoning": "• Drink ORS\n• Avoid solid food\n• Rest\n• Visit doctor if dehydration persists",
    "Pneumonia": "• Seek immediate medical care\n• Avoid cold\n• Take prescribed antibiotics"
}

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("🩺 AI Health Diagnosis System")
st.write("Select your symptoms to get disease prediction + prevention guide.")

st.header("Select Symptoms:")
user_input = []

for symptom in symptoms:
    value = st.checkbox(symptom.replace("_", " ").title())
    user_input.append(1 if value else 0)

# -----------------------------
# ON BUTTON CLICK
# -----------------------------
if st.button("Predict Disease"):
    
    # Make model prediction
    prediction = model.predict([user_input])[0]

    st.success(f"🧠 Predicted Disease: **{prediction}**")

    # Debug: show actual prediction returned by model
    st.warning(f"DEBUG — Model predicted: {prediction}")

    # -----------------------------
    # SHOW PREVENTION (Even if mismatch)
    # -----------------------------

    # Case 1: Exact match found
    if prediction in prevention:
        st.subheader("🛡 Prevention & Recommendations")
        st.write(prevention[prediction])

    # Case 2: Model predicted differently → Map closest disease
    else:
        st.error("⚠ Prevention not found for predicted label. Using best possible match...")

        # Convert to lowercase for safer matching
        prediction_lower = prediction.lower()

        mapped = None
        for key in prevention.keys():
            if key.lower() in prediction_lower or prediction_lower in key.lower():
                mapped = key
                break

        if mapped:
            st.subheader(f"🛡 Prevention for similar condition → {mapped}")
            st.write(prevention[mapped])
        else:
            st.warning("No matching prevention guide found.")

    # -----------------------------
    # Confidence Score
    # -----------------------------
    try:
        probs = model.predict_proba([user_input])
        confidence = round(max(probs[0]) * 100, 2)
        st.info(f"Confidence Level: {confidence}%")
    except:
        st.info("Confidence score not available (model may not support predict_proba).")
