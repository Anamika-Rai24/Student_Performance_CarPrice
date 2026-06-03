import streamlit as st
import pandas as pd
import joblib

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# LOAD MODEL
# ==========================

model = joblib.load("student_performance_model.pkl")

# ==========================
# CUSTOM CSS
# ==========================

import base64

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64("Std.png")

st.markdown(
    f"""
    <style>

    [data-testid="stAppViewContainer"] {{
        background:
        linear-gradient(
            rgba(0,0,0,0.78),
            rgba(0,0,0,0.78)
        ),
        url("data:image/jpg;base64,{bg_image}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    h1,h2,h3,h4,p,label {{
        color: white !important;
    }}

    .main-card {{
        background: rgba(255,255,255,0.10);
        padding:25px;
        border-radius:20px;
        backdrop-filter: blur(12px);
        border:1px solid rgba(255,255,255,0.15);
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# TITLE
# ==========================

st.markdown("""
<div class="main-card">
<h1 style="text-align:center;">
🎓 Student Performance Prediction System
</h1>

<p style="text-align:center;font-size:20px;">
Predict whether a student is likely to Pass or Fail using Machine Learning
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# INPUT SECTION
# ==========================

st.markdown("""
<div class="main-card">
<h3>Enter Student Details</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    studytime = st.slider(
        "Study Time",
        min_value=1,
        max_value=4,
        value=2
    )

    failures = st.slider(
        "Previous Failures",
        min_value=0,
        max_value=4,
        value=0
    )

    G1 = st.number_input(
        "First Period Grade (G1)",
        min_value=0,
        max_value=20,
        value=10
    )

with col2:

    absences = st.number_input(
        "Absences",
        min_value=0,
        max_value=100,
        value=5
    )

    G2 = st.number_input(
        "Second Period Grade (G2)",
        min_value=0,
        max_value=20,
        value=10
    )

# ==========================
# PREDICTION
# ==========================

if st.button("🔍 Predict Result"):

    input_data = pd.DataFrame({
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })

    prediction = model.predict(input_data)

    st.write("")

    if prediction[0] == 1:
        st.success("✅ Student is Likely to PASS")
    else:
        st.error("❌ Student is Likely to FAIL")

    st.subheader("Student Information")
    st.dataframe(input_data)

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown(
    "<center><h4 style='color:white;'>Built with Streamlit • Scikit-Learn • Machine Learning 🚀</h4></center>",
    unsafe_allow_html=True
)