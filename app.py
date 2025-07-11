import streamlit as st

# List of all possible symptoms
symp = [
    "fever", "cough", "motion", "flu", "loss of taste", "headache", "cramps", "blury vision",
    "sore throat", "fatigue", "rash", "vomiting", "chest pain", "shortness of breath", "nausea", "diarrhea"
]

# Disease symptoms mapping
disease_symptoms = {
    "Malaria": ["fever", "cough", "motion"],
    "Dengue": ["loss of taste", "headache", "cramps"],
    "Flu": ["fever", "cough", "sore throat", "fatigue"],
    "COVID-19": ["fever", "cough", "loss of taste", "fatigue"],
    "Typhoid": ["fever", "headache", "rash", "vomiting"],
    "Pneumonia": ["fever", "cough", "chest pain", "shortness of breath"],
    "Food Poisoning": ["vomiting", "nausea", "diarrhea", "headache"]
}

# First aid tips for each disease
first_aid_tips = {
    "Malaria": "Stay hydrated, eat healthy food",
    "Dengue": "Use mosquito repellent",
    "Flu": "Rest well, drink warm fluids",
    "COVID-19": "Isolate yourself, stay hydrated",
    "Typhoid": "Maintain hygiene, avoid street food",
    "Pneumonia": "Keep warm, take prescribed antibiotics",
    "Food Poisoning": "Drink ORS, avoid solid food temporarily"
}

# Streamlit UI
st.title("🩺 Disease Prediction from Symptoms")
st.write("Select the symptoms you're currently experiencing:")

user_symptoms = st.multiselect("Choose your symptoms", symp)

# Diagnosis logic
if st.button("Diagnose"):
    found = False
    for disease, symptoms in disease_symptoms.items():
        match = set(user_symptoms).intersection(symptoms)
        if len(match) >= 2:
            st.success(f"🔍 Possible Disease: **{disease}**")
            st.info(f"💡 First Aid Tip: {first_aid_tips[disease]}")
            st.warning("Please consult a medical specialist for a proper diagnosis.")
            found = True
            break

    if not found:
        st.error("⚠️ No disease identified. Please consult a doctor.")
