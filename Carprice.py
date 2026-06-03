import streamlit as st
import pandas as pd
import joblib
import base64

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Car Price Prediction Dashboard",
    page_icon="🚗",
    layout="wide"
)

# ==========================
# LOAD MODEL
# ==========================

model = joblib.load("car_price_model.pkl")

# ==========================
# BACKGROUND IMAGE
# ==========================

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64("Car.jpg")

page_bg = f"""
<style>

[data-testid="stAppViewContainer"] {{
    background:
    linear-gradient(rgba(0,0,0,0.65),
    rgba(0,0,0,0.65)),
    url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

h1, h2, h3, p, label {{
    color: white !important;
}}

.main-card {{
    background: rgba(255,255,255,0.12);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.2);
}}

.stButton > button {{
    width: 100%;
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    color: white;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    padding: 12px;
}}

.stButton > button:hover {{
    transform: scale(1.02);
}}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ==========================
# TITLE
# ==========================

st.markdown("""
<div class="main-card">
<h1 style="text-align:center;">
🚗 AI Powered Car Price Prediction Dashboard
</h1>

<p style="text-align:center;font-size:20px;">
Predict the market price of a car using Machine Learning
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# INPUT SECTION
# ==========================

st.markdown("""
<div class="main-card">
<h3>Enter Car Details</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    fuel_type = st.selectbox(
        "Fuel Type",
        ["diesel", "gas"]
    )

    engine_location = st.selectbox(
        "Engine Location",
        ["front", "rear"]
    )

    horsepower = st.number_input(
        "Horsepower",
        min_value=40,
        max_value=400,
        value=100
    )

    city_mpg = st.number_input(
        "City MPG",
        min_value=5,
        max_value=60,
        value=20
    )

with col2:

    engine_type = st.selectbox(
        "Engine Type",
        [
            "dohc",
            "dohcv",
            "l",
            "ohc",
            "ohcf",
            "ohcv",
            "rotor"
        ]
    )

    peak_rpm = st.number_input(
        "Peak RPM",
        min_value=3000,
        max_value=8000,
        value=5000
    )

    highway_mpg = st.number_input(
        "Highway MPG",
        min_value=5,
        max_value=70,
        value=30
    )

# ==========================
# ENCODING
# ==========================

fuel_map = {
    "diesel": 0,
    "gas": 1
}

engine_location_map = {
    "front": 0,
    "rear": 1
}

engine_type_map = {
    "dohc": 0,
    "dohcv": 1,
    "l": 2,
    "ohc": 3,
    "ohcf": 4,
    "ohcv": 5,
    "rotor": 6
}

# ==========================
# PREDICTION
# ==========================

if st.button("🔍 Predict Car Price"):

    input_data = pd.DataFrame({
        'fuel-type': [fuel_map[fuel_type]],
        'engine-location': [engine_location_map[engine_location]],
        'engine-type': [engine_type_map[engine_type]],
        'horsepower': [horsepower],
        'peak-rpm': [peak_rpm],
        'city-mpg': [city_mpg],
        'highway-mpg': [highway_mpg]
    })

    prediction = model.predict(input_data)

    st.markdown(
    f"""
    <h1 style="
        text-align:center;
        color:#00FF99 !important;
        font-size:70px;
        font-weight:bold;
    ">
        ₹ {prediction[0]:,.0f}
    </h1>
    """,
    unsafe_allow_html=True
)

    st.balloons()

    st.subheader("Input Summary")

    st.dataframe(input_data)

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown(
    "<center><h4 style='color:white;'>Built with Streamlit • Scikit-Learn • Machine Learning 🚀</h4></center>",
    unsafe_allow_html=True
)