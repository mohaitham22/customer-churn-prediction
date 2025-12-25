import streamlit as st
import pickle
import numpy as np

# --------------------------
# Page Config
# --------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

st.title("📉 Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn based on their profile.")

# --------------------------
# Load Model & Scaler
# --------------------------
with open("model.pkl", "rb") as f:
    model_churn = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler_churn = pickle.load(f)

# --------------------------
# Encoding Helper
# --------------------------
def map_inputs(Geography, Gender, Card_Type):
    geo_map = {"France": 0, "Spain": 1, "Germany": 2}
    gender_map = {"Female": 0, "Male": 1}
    card_map = {"GOLD": 1, "SILVER": 2, "PLATINUM": 3, "DIAMOND": 4}
    return geo_map[Geography], gender_map[Gender], card_map[Card_Type]

# --------------------------
# Input Layout
# --------------------------
col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Age", min_value=18, max_value=100, value=30)
    Geography = st.radio("Geography", ["France", "Spain", "Germany"])
    Gender = st.radio("Gender", ["Female", "Male"])
    Tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, value=3)
    Balance = st.number_input("Account Balance", value=10000.0)
    NumOfProducts = st.number_input(
        "Number of Products", min_value=1, max_value=4, value=1
    )
    HasCrCard = st.selectbox("Has Credit Card?", ["No", "Yes"])
    HasCrCard_enc = 1 if HasCrCard == "Yes" else 0

with col2:
    IsActiveMember = st.selectbox("Is Active Member?", ["No", "Yes"])
    IsActiveMember_enc = 1 if IsActiveMember == "Yes" else 0
    EstimatedSalary = st.number_input("Estimated Salary", value=50000.0)
    CreditScore = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
    Points_Earned = st.number_input("Points Earned", value=300)
    Satisfaction_Score = st.slider(
        "Satisfaction Score", min_value=1, max_value=8, value=3
    )
    Card_Type = st.radio(
        "Card Type", ["SILVER", "GOLD", "PLATINUM", "DIAMOND"]
    )

# --------------------------
# Encoding
# --------------------------
Geography_enc, Gender_enc, CardType_enc = map_inputs(
    Geography, Gender, Card_Type
)

# --------------------------
# Build Input Array
# --------------------------
input_churn = np.array([[  
    CreditScore,
    Geography_enc,
    Gender_enc,
    Age,
    Tenure,
    Balance,
    NumOfProducts,
    HasCrCard_enc,
    IsActiveMember_enc,
    EstimatedSalary,
    Satisfaction_Score,
    CardType_enc,
    Points_Earned
]])

# Scale input
input_churn_scaled = scaler_churn.transform(input_churn)

# --------------------------
# Prediction
# --------------------------
if st.button("🔍 Predict Churn"):
    pred = model_churn.predict(input_churn_scaled)[0]
    prob = model_churn.predict_proba(input_churn_scaled)[0][1]
    prob_percent = prob * 100

    if pred == 1:
        st.error(
            f"⚠️ Customer is likely to churn\n\n"
            f"**Churn Probability:** {prob_percent:.2f}%"
        )
    else:
        st.success(
            f"✅ Customer is NOT likely to churn\n\n"
            f"**Churn Probability:** {prob_percent:.2f}%"
        )

    st.progress(int(prob_percent))



