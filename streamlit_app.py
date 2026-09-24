import streamlit as st
import pickle
import numpy as np

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="IGAP Student Performance Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   TECHNOLOGY BACKGROUND
   ===================================================== */

.stApp {
    background-image:
        linear-gradient(
            rgba(0, 0, 0, 0.20),
            rgba(0, 0, 0, 0.20)
        ),
        url("https://images.unsplash.com/photo-1518770660439-4636190af475");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}


/* =====================================================
   MAIN CONTAINER
   ===================================================== */

.block-container {
    padding-top: 2rem !important;
    padding-left: 4rem !important;
    padding-right: 4rem !important;
    background: transparent !important;
}


/* =====================================================
   HEADER
   ===================================================== */

.header-box {
    background: rgba(255, 255, 255, 0.92);
    padding: 28px;
    border-radius: 25px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.30);
}

.header-title {
    font-size: 40px;
    font-weight: 800;
    color: #172554;
}

.header-subtitle {
    font-size: 18px;
    color: #475569;
    margin-top: 8px;
}


/* =====================================================
   INPUT SECTION
   ===================================================== */

.input-box {
    background: rgba(15, 23, 42, 0.82);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.40);
    border: 1px solid rgba(255,255,255,0.20);
}


/* =====================================================
   SECTION TITLE
   ===================================================== */

.section-title {
    font-size: 24px;
    font-weight: 800;
    color: white;
    margin-bottom: 20px;
    text-shadow: 2px 2px 5px #000000;
}


/* =====================================================
   INPUT LABELS
   ===================================================== */

.stNumberInput label {
    color: white !important;
    font-weight: 800 !important;
    font-size: 17px !important;
    text-shadow: 2px 2px 5px #000000 !important;
}


/* =====================================================
   INPUT BOX
   ===================================================== */

.stNumberInput input {
    background: rgba(255,255,255,0.97) !important;
    color: #111827 !important;
    border-radius: 12px !important;
    border: 2px solid white !important;
    font-size: 17px !important;
    font-weight: 600 !important;
}


/* =====================================================
   INPUT BOX FOCUS
   ===================================================== */

.stNumberInput input:focus {
    border: 2px solid #60a5fa !important;
    box-shadow: 0 0 10px rgba(96,165,250,0.5) !important;
}


/* =====================================================
   PERFORMANCE TITLE
   ===================================================== */

.performance-title {
    color: white;
    font-size: 25px;
    font-weight: 800;
    text-align: center;
    margin-top: 30px;
    margin-bottom: 20px;
    text-shadow: 2px 2px 5px #000000;
}


/* =====================================================
   PERFORMANCE CARDS
   ===================================================== */

.performance-card {
    background: rgba(255,255,255,0.94);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 22px rgba(0,0,0,0.30);
}

.performance-card h3 {
    color: #475569;
    font-size: 17px;
}

.performance-card h2 {
    color: #172554;
    font-size: 27px;
    margin: 5px;
}

.performance-card p {
    color: #64748b;
}


/* =====================================================
   PREDICT BUTTON
   ===================================================== */

.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 16px;
    border: none;

    background: linear-gradient(
        90deg,
        #4f46e5,
        #2563eb
    );

    color: white;
    font-size: 20px;
    font-weight: 800;

    box-shadow: 0 8px 22px rgba(37,99,235,0.40);
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #3730a3,
        #1d4ed8
    );

    color: white;
}


/* =====================================================
   PASS RESULT
   ===================================================== */

.pass-result {
    background: rgba(22,163,74,0.95);
    color: white;
    padding: 28px;
    border-radius: 22px;
    text-align: center;
    margin-top: 25px;
    font-size: 26px;
    font-weight: 800;

    box-shadow:
        0 10px 30px rgba(22,163,74,0.40);
}


/* =====================================================
   FAIL RESULT
   ===================================================== */

.fail-result {
    background: rgba(220,38,38,0.95);
    color: white;
    padding: 28px;
    border-radius: 22px;
    text-align: center;
    margin-top: 25px;
    font-size: 26px;
    font-weight: 800;

    box-shadow:
        0 10px 30px rgba(220,38,38,0.40);
}


/* =====================================================
   ABOUT BOX
   ===================================================== */

.about-box {
    background: rgba(255,255,255,0.92);
    padding: 25px;
    border-radius: 22px;
    margin-top: 30px;

    box-shadow:
        0 8px 22px rgba(0,0,0,0.25);

    color: #334155;
}

.about-box h2 {
    color: #172554;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;
    color: white;
    font-size: 16px;
    font-weight: 700;
    padding: 25px;

    text-shadow:
        2px 2px 5px #000000;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MACHINE LEARNING MODEL
# =========================================================

try:

    with open("student_performance_model.pkl", "rb") as file:
        model = pickle.load(file)

    model_loaded = True

except Exception:

    model_loaded = False


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header-box">

<div class="header-title">
🎓 IGAP Student Performance Prediction
</div>

<div class="header-subtitle">
AI & Machine Learning Based Academic Performance Analysis
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown("""
<div class="input-box">

<div class="section-title">
📝 Enter Student Academic Information
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)


# =========================================================
# LEFT COLUMN
# =========================================================

with col1:

    study_hours = st.number_input(
        "📚 Study Hours",
        min_value=0.0,
        max_value=15.0,
        value=5.0,
        step=0.5
    )

    attendance = st.number_input(
        "📅 Attendance (%)",
        min_value=0,
        max_value=100,
        value=75
    )

    previous_marks = st.number_input(
        "📊 Previous Marks (%)",
        min_value=0,
        max_value=100,
        value=60
    )


# =========================================================
# RIGHT COLUMN
# =========================================================

with col2:

    assignment_score = st.number_input(
        "📝 Assignment Score (%)",
        min_value=0,
        max_value=100,
        value=70
    )

    internal_marks = st.number_input(
        "📖 Internal Marks (%)",
        min_value=0,
        max_value=100,
        value=65
    )

    practical_score = st.number_input(
        "💻 Practical Score (%)",
        min_value=0,
        max_value=100,
        value=70
    )


st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PERFORMANCE OVERVIEW
# =========================================================

st.markdown("""
<div class="performance-title">
📈 Performance Overview
</div>
""", unsafe_allow_html=True)


card1, card2, card3, card4 = st.columns(4)


with card1:

    st.markdown(f"""
    <div class="performance-card">

        <h3>📚 Study Hours</h3>

        <h2>{study_hours}</h2>

        <p>Hours / Day</p>

    </div>
    """, unsafe_allow_html=True)


with card2:

    st.markdown(f"""
    <div class="performance-card">

        <h3>📅 Attendance</h3>

        <h2>{attendance}%</h2>

        <p>Attendance Rate</p>

    </div>
    """, unsafe_allow_html=True)


with card3:

    st.markdown(f"""
    <div class="performance-card">

        <h3>📊 Previous Marks</h3>

        <h2>{previous_marks}%</h2>

        <p>Previous Performance</p>

    </div>
    """, unsafe_allow_html=True)


with card4:

    st.markdown(f"""
    <div class="performance-card">

        <h3>💻 Practical</h3>

        <h2>{practical_score}%</h2>

        <p>Practical Performance</p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🔮  PREDICT STUDENT PERFORMANCE"
)


# =========================================================
# PREDICTION
# =========================================================

if predict:

    input_data = np.array([[
        study_hours,
        attendance,
        previous_marks,
        assignment_score,
        internal_marks,
        practical_score
    ]])

    prediction_done = False


    # =====================================================
    # REAL MODEL
    # =====================================================

    if model_loaded:

        try:

            prediction = model.predict(input_data)[0]

            prediction_done = True


            if (
                prediction == 1
                or str(prediction).lower() == "pass"
            ):

                st.markdown("""
                <div class="pass-result">

                🎉 STUDENT IS LIKELY TO PASS!

                <br>

                <span style="font-size:16px;">
                Keep maintaining the same performance.
                </span>

                </div>
                """, unsafe_allow_html=True)

                st.balloons()


            else:

                st.markdown("""
                <div class="fail-result">

                ⚠️ STUDENT MAY NEED IMPROVEMENT

                <br>

                <span style="font-size:16px;">
                Focus more on studies, attendance and assignments.
                </span>

                </div>
                """, unsafe_allow_html=True)


        except Exception:

            prediction_done = False


    # =====================================================
    # FALLBACK
    # =====================================================

    if not prediction_done:

        score = (
            study_hours * 5
            + attendance * 0.25
            + previous_marks * 0.20
            + assignment_score * 0.10
            + internal_marks * 0.10
            + practical_score * 0.10
        )


        if score >= 70:

            st.markdown("""
            <div class="pass-result">

            🎉 STUDENT IS LIKELY TO PASS!

            <br>

            <span style="font-size:16px;">
            Overall academic performance looks positive.
            </span>

            </div>
            """, unsafe_allow_html=True)

            st.balloons()


        else:

            st.markdown("""
            <div class="fail-result">

            ⚠️ STUDENT MAY NEED IMPROVEMENT

            <br>

            <span style="font-size:16px;">
            More academic improvement is recommended.
            </span>

            </div>
            """, unsafe_allow_html=True)


# =========================================================
# ABOUT SYSTEM
# =========================================================

st.markdown("""
<div class="about-box">

<h2>
💡 About IGAP Prediction System
</h2>

<p style="font-size:17px; line-height:1.7;">

This Machine Learning based application predicts student
academic performance using study hours, attendance,
previous marks, assignment score, internal marks and
practical performance.

The application is developed using
<b>Python, Streamlit, NumPy and Machine Learning.</b>

</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

🎓 IGAP Private Limited<br>

Student Performance Prediction System<br><br>

© 2026 IGAP Private Limited

</div>
""", unsafe_allow_html=True)