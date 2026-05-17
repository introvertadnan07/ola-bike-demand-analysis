import streamlit as st
import pickle
import pandas as pd

# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="Ola Ride Demand Prediction",
    page_icon="🚴",
    layout="centered"
)

# =========================
# Custom Styling
# =========================

st.markdown("""
    <style>

    .main {
        background-color: #0E1117;
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #B0B0B0;
        text-align: center;
        margin-bottom: 30px;
    }

    .prediction-box {
        background-color: #1E293B;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 28px;
        font-weight: bold;
        margin-top: 25px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
    }

    </style>
""", unsafe_allow_html=True)

# =========================
# Load Trained Model
# =========================

with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

# =========================
# Title Section
# =========================

st.markdown(
    '<div class="title">🚴 Ola Bike Ride Demand Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict bike ride demand using weather and seasonal conditions</div>',
    unsafe_allow_html=True
)

# =========================
# Sidebar Inputs
# =========================

st.sidebar.header("Enter Ride Details")

temp = st.sidebar.slider(
    "🌡 Temperature",
    0,
    50,
    25
)

humidity = st.sidebar.slider(
    "💧 Humidity",
    0,
    100,
    50
)

windspeed = st.sidebar.slider(
    "🌬 Windspeed",
    0,
    50,
    10
)

hour = st.sidebar.slider(
    "⏰ Hour",
    0,
    23,
    12
)

season = st.sidebar.selectbox(
    "🍂 Season",
    {
        1: "Spring",
        2: "Summer",
        3: "Fall",
        4: "Winter"
    }
)

# =========================
# Input Summary
# =========================

st.subheader("Selected Inputs")

input_df = pd.DataFrame({
    "Feature": [
        "Temperature",
        "Humidity",
        "Windspeed",
        "Hour",
        "Season"
    ],
    "Value": [
        temp,
        humidity,
        windspeed,
        hour,
        {
            1: "Spring",
            2: "Summer",
            3: "Fall",
            4: "Winter"
        }[season]
    ]
})

st.table(input_df)

# =========================
# Prediction Section
# =========================

if st.button("🚀 Predict Ride Demand"):

    prediction = model.predict([
        [temp, humidity, windspeed, hour, season]
    ])

    st.markdown(
        f'''
        <div class="prediction-box">
            Predicted Ride Count<br><br>
            {int(prediction[0])} Rides
        </div>
        ''',
        unsafe_allow_html=True
    )

# =========================
# Footer
# =========================

st.markdown("---")

st.caption("Developed using Streamlit & Machine Learning")