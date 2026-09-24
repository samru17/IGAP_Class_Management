import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="IGAP Class Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f3f6fb;
}

/* Top Navigation */
.navbar {
    background-color: #24428d;
    padding: 18px 20px;
    text-align: center;
    margin: -60px -60px 35px -60px;
}

.navbar span {
    color: white;
    font-size: 20px;
    font-weight: 600;
    margin: 0 17px;
}

/* Main Dashboard Box */
.dashboard-box {
    background-color: white;
    padding: 55px 35px;
    border-radius: 20px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.10);
    margin-bottom: 30px;
}

.dashboard-title {
    color: #24428d;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 15px;
}

.dashboard-subtitle {
    color: #222;
    font-size: 21px;
}

/* Cards */
.card {
    background-color: white;
    height: 105px;
    border-radius: 18px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.10);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 21px;
    color: #111;
    margin-bottom: 25px;
    border: 1px solid #eeeeee;
}

/* Footer */
.footer {
    background-color: #24428d;
    color: white;
    text-align: center;
    padding: 30px;
    margin: 50px -60px -60px -60px;
    font-size: 19px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TOP NAVIGATION
# =========================================================

st.markdown("""
<div class="navbar">
    <span>Home</span>
    <span>Dashboard</span>
    <span>Students</span>
    <span>Teachers</span>
    <span>Classes</span>
    <span>Subjects</span>
    <span>Attendance</span>
    <span>Exams</span>
    <span>Results</span>
</div>
""", unsafe_allow_html=True)


# =========================================================
# DASHBOARD HEADER
# =========================================================

st.markdown("""
<div class="dashboard-box">

<div class="dashboard-title">
📊 Dashboard
</div>

<div class="dashboard-subtitle">
IGAP Private Limited - Class Management System
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FIRST ROW
# =========================================================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="card">
    👨‍🎓 Students
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    👨‍🏫 Teachers
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    📚 Classes
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
    📖 Subjects
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
    📝 Attendance
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# SECOND ROW
# =========================================================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="card">
    📋 Exams
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    📊 Results
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    🎯 Prediction
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# INFORMATION SECTION
# =========================================================

st.markdown("## 🏫 IGAP Private Limited")

st.info("""
Welcome to IGAP Private Limited Class Management System.

This system is designed to manage students, teachers, classes,
subjects, attendance, examinations and academic results
in one place.
""")


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

© 2026 IGAP Private Limited<br><br>
Class Management System

</div>
""", unsafe_allow_html=True)