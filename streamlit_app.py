import streamlit as st

st.set_page_config(
    page_title="IGAP Class Management System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 IGAP Class Management System")

st.write("Welcome to IGAP Private Limited")

st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Select Section",
    [
        "Home",
        "Students",
        "Teachers",
        "Classes",
        "Subjects",
        "Attendance",
        "Exams",
        "Results",
        "Student Performance Prediction"
    ]
)

if option == "Home":
    st.header("🏫 IGAP Private Limited")
    st.write("Class Management System")
    st.success("Welcome to IGAP Class Management System!")

elif option == "Students":
    st.header("👨‍🎓 Students")
    st.info("Student management section")

elif option == "Teachers":
    st.header("👨‍🏫 Teachers")
    st.info("Teacher management section")

elif option == "Classes":
    st.header("📚 Classes")
    st.info("Class management section")

elif option == "Subjects":
    st.header("📖 Subjects")
    st.info("Subject management section")

elif option == "Attendance":
    st.header("📝 Attendance")
    st.info("Attendance management section")

elif option == "Exams":
    st.header("📋 Exams")
    st.info("Exam management section")

elif option == "Results":
    st.header("📊 Results")
    st.info("Result management section")

elif option == "Student Performance Prediction":
    st.header("🎯 Student Performance Prediction")

    study_hours = st.number_input(
        "Study Hours",
        min_value=0.0,
        max_value=15.0,
        value=5.0
    )

    attendance = st.number_input(
        "Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

    previous_marks = st.number_input(
        "Previous Marks (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

    if st.button("🔮 Predict"):
        score = (
            study_hours * 5
            + attendance * 0.3
            + previous_marks * 0.2
        )

        if score >= 50:
            st.success("🎉 Student is likely to PASS!")
        else:
            st.error("⚠️ Student is likely to FAIL!")