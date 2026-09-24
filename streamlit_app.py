import streamlit as st
import pickle
import numpy as np

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="💻",
    layout="wide"
)

# =====================================================
# BACKGROUND + CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-image: url("https://images.unsplash.com/photo-1518770660439-4636190af475");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Main transparent container */
.block-container {
    background: rgba(255, 255, 255, 0.88);
    padding: 35px;
    border-radius: 20px;
    margin-top: 25px;
    margin-bottom: 25px;
}

/* Main title */
.main-title {
    text-align: center;
    color: #172554;
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    text-align: center;
    color: #334155;
    font-size: 20px;
    margin-bottom: 30px;
}

/* Section title */
.section-title {
    background: #4c1d95;
    color: white;
    padding: 12px 20px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 600;
    margin-top: 15px;
}

/* Prediction result */
.result-box {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 25px;
    font-weight: 700;
    margin-top: 25px;
}

/* Button */
.stButton > button {
    width: 100%;
    background-color: #4c1d95;
    color: white;
    font-size: 20px;
    font-weight: 600;
    border-radius: 12px;
    padding: 12px;
    border: none;
}

.stButton > button:hover {
    background-color: #6d28d9;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD MODEL
# =====================================================

try:
    with open("student_performance_model.pkl", "rb") as file:
        model = pickle.load(file)
    model_loaded = True

except:
    model_loaded = False


# =====================================================
# TITLE
# =====================================================

st.markdown(
    '<div class="main-title">💻 Student Performance Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict student academic performance using Machine Learning</div>',
    unsafe_allow_html=True
)


# =====================================================
# STUDENT INFORMATION
# =====================================================

st.markdown(
    '<div class="section-title">📝 Student Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    study_hours = st.slider(
        "📚 Study Hours",
        min_value=0.0,
        max_value=15.0,
        value=5.0,
        step=0.5
    )

    attendance = st.slider(
        "📅 Attendance (%)",
        min_value=0,
        max_value=100,
        value=75
    )

    previous_marks = st.slider(
        "📊 Previous Marks (%)",
        min_value=0,
        max_value=100,
        value=60
    )

with col2:

    assignment_score = st.slider(
        "📝 Assignment Score (%)",
        min_value=0,
        max_value=100,
        value=70
    )

    internal_marks = st.slider(
        "📖 Internal Marks (%)",
        min_value=0,
        max_value=100,
        value=65
    )

    practical_score = st.slider(
        "💻 Practical Score (%)",
        min_value=0,
        max_value=100,
        value=70
    )


# =====================================================
# PREDICT BUTTON
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔮 PREDICT PERFORMANCE"):

    # -------------------------------------------------
    # If your trained model is available
    # -------------------------------------------------

    if model_loaded:

        try:

            input_data = np.array([[
                study_hours,
                attendance,
                previous_marks,
                assignment_score,
                internal_marks,
                practical_score
            ]])

            prediction = model.predict(input_data)[0]

            if prediction == 1 or str(prediction).lower() == "pass":

                st.markdown(
                    """
                    <div class="result-box"
                    style="background:rgba(34,197,94,0.20);
                    color:#15803d;">
                    🎉 STUDENT IS LIKELY TO PASS
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.balloons()

            else:

                st.markdown(
                    """
                    <div class="result-box"
                    style="background:rgba(239,68,68,0.20);
                    color:#b91c1c;">
                    ⚠️ STUDENT MAY NEED IMPROVEMENT
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as e:

            st.warning(
                "Model input columns do not match this prediction form."
            )

    # -------------------------------------------------
    # Demo prediction if model cannot be used
    # -------------------------------------------------

    else:

        score = (
            study_hours * 5
            + attendance * 0.25
            + previous_marks * 0.20
            + assignment_score * 0.10
            + internal_marks * 0.10
            + practical_score * 0.10
        )

        if score >= 70:

            st.markdown(
                """
                <div class="result-box"
                style="background:rgba(34,197,94,0.20);
                color:#15803d;">
                🎉 STUDENT IS LIKELY TO PASS
                </div>
                """,
                unsafe_allow_html=True
            )

            st.balloons()

        else:

            st.markdown(
                """
                <div class="result-box"
                style="background:rgba(239,68,68,0.20);
                color:#b91c1c;">
                ⚠️ STUDENT MAY NEED IMPROVEMENT
                </div>
                """,
                unsafe_allow_html=True
            )


# =====================================================
# INFORMATION
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background:rgba(219,234,254,0.75);
padding:20px;
border-radius:15px;
">

<h2 style="color:#075985;">💡 About Prediction</h2>

<p style="font-size:17px;">
This Machine Learning system analyzes student academic
information such as study hours, attendance, previous marks,
assignments, internal marks and practical performance.
</p>

</div>
""", unsafe_allow_html=True)