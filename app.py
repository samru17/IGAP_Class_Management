from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import joblib

app = Flask(__name__)
app.secret_key = "igap_secret_key"


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",
        database="igap_class_management"
    )
model = joblib.load("student_performance_model.pkl")

# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM teachers")
    teachers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM classes")
    classes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM subjects")
    subjects = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM attendance")
    attendance = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM exams")
    exams = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM results")
    results = cursor.fetchone()[0]

    cursor.close()
    db.close()

    return render_template(
        "dashboard.html",
        students=students,
        teachers=teachers,
        classes=classes,
        subjects=subjects,
        attendance=attendance,
        exams=exams,
        results=results
    )


# =========================================================
# STUDENTS
# =========================================================

@app.route("/students")
def students():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    query = """
        SELECT students.*, classes.class_name
        FROM students
        LEFT JOIN classes
        ON students.class_id = classes.class_id
        ORDER BY students.student_id
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM classes ORDER BY class_name")
    class_data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
    "students.html",
    students=data,
    classes=class_data
)
    


@app.route("/add_student", methods=["POST"])
def add_student():

    name = request.form["student_name"]
    gender = request.form["gender"]
    age = request.form["age"]
    phone = request.form["phone"]
    class_id = request.form["class_id"]

    db = get_db_connection()
    cursor = db.cursor()

    query = """
        INSERT INTO students
        (student_name, gender, age, phone, class_id)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (name, gender, age, phone, class_id)
    )

    db.commit()

    cursor.close()
    db.close()

    flash("Student added successfully!", "success")

    return redirect(url_for("students"))


@app.route("/delete_student/<int:student_id>")
def delete_student(student_id):

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            "DELETE FROM students WHERE student_id=%s",
            (student_id,)
        )

        db.commit()
        flash("Student deleted successfully!", "success")

    except mysql.connector.Error:
        db.rollback()
        flash(
            "Student cannot be deleted because related records exist.",
            "danger"
        )

    cursor.close()
    db.close()

    return redirect(url_for("students"))


# =========================================================
# TEACHERS
# =========================================================

@app.route("/teachers")
def teachers():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM teachers
        ORDER BY teacher_id
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "teachers.html",
        teachers=data
    )


@app.route("/add_teacher", methods=["POST"])
def add_teacher():

    name = request.form["teacher_name"]
    specialization = request.form["subject_specialization"]
    phone = request.form["phone"]

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO teachers
        (teacher_name, subject_specialization, phone)
        VALUES (%s, %s, %s)
    """, (name, specialization, phone))

    db.commit()

    cursor.close()
    db.close()

    flash("Teacher added successfully!", "success")

    return redirect(url_for("teachers"))


@app.route("/delete_teacher/<int:teacher_id>")
def delete_teacher(teacher_id):

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            "DELETE FROM teachers WHERE teacher_id=%s",
            (teacher_id,)
        )

        db.commit()

        flash("Teacher deleted successfully!", "success")

    except mysql.connector.Error:
        db.rollback()

        flash(
            "Teacher cannot be deleted because it is linked with a class.",
            "danger"
        )

    cursor.close()
    db.close()

    return redirect(url_for("teachers"))


# =========================================================
# CLASSES
# =========================================================

@app.route("/classes")
def classes():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT classes.*, teachers.teacher_name
        FROM classes
        LEFT JOIN teachers
        ON classes.teacher_id = teachers.teacher_id
        ORDER BY classes.class_id
    """)

    class_data = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM teachers
        ORDER BY teacher_name
    """)

    teacher_data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "classes.html",
        classes=class_data,
        teachers=teacher_data
    )


@app.route("/add_class", methods=["POST"])
def add_class():

    class_name = request.form["class_name"]
    course_name = request.form["course_name"]
    division = request.form["division"]
    teacher_id = request.form["teacher_id"]
    room_no = request.form["room_no"]

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO classes
        (class_name, course_name, division, teacher_id, room_no)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        class_name,
        course_name,
        division,
        teacher_id,
        room_no
    ))

    db.commit()

    cursor.close()
    db.close()

    flash("Class added successfully!", "success")

    return redirect(url_for("classes"))


@app.route("/delete_class/<int:class_id>")
def delete_class(class_id):

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            "DELETE FROM classes WHERE class_id=%s",
            (class_id,)
        )

        db.commit()

        flash("Class deleted successfully!", "success")

    except mysql.connector.Error:
        db.rollback()

        flash(
            "Class cannot be deleted because related records exist.",
            "danger"
        )

    cursor.close()
    db.close()

    return redirect(url_for("classes"))


# =========================================================
# SUBJECTS
# =========================================================

@app.route("/subjects")
def subjects():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT subjects.*, classes.class_name
        FROM subjects
        LEFT JOIN classes
        ON subjects.class_id = classes.class_id
        ORDER BY subjects.subject_id
    """)

    subject_data = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM classes
        ORDER BY class_name
    """)

    class_data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "subjects.html",
        subjects=subject_data,
        classes=class_data
    )


@app.route("/add_subject", methods=["POST"])
def add_subject():

    subject_name = request.form["subject_name"]
    class_id = request.form["class_id"]

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO subjects
        (subject_name, class_id)
        VALUES (%s, %s)
    """, (subject_name, class_id))

    db.commit()

    cursor.close()
    db.close()

    flash("Subject added successfully!", "success")

    return redirect(url_for("subjects"))


@app.route("/delete_subject/<int:subject_id>")
def delete_subject(subject_id):

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            "DELETE FROM subjects WHERE subject_id=%s",
            (subject_id,)
        )

        db.commit()

        flash("Subject deleted successfully!", "success")

    except mysql.connector.Error:
        db.rollback()

        flash(
            "Subject cannot be deleted because related records exist.",
            "danger"
        )

    cursor.close()
    db.close()

    return redirect(url_for("subjects"))


# =========================================================
# ATTENDANCE
# =========================================================


@app.route("/attendance")
def attendance():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT attendance.*,
               students.student_name
        FROM attendance
        LEFT JOIN students
        ON attendance.student_id = students.student_id
        ORDER BY attendance.attendance_id DESC
    """)

    attendance_data = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY student_name
    """)

    student_data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "attendance.html",
        attendance_records=attendance_data,
        students=student_data
    )


@app.route("/add_attendance", methods=["POST"])
def add_attendance():

    student_id = request.form["student_id"]
    attendance_date = request.form["attendance_date"]
    status = request.form["status"]

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO attendance
        (student_id, attendance_date, status)
        VALUES (%s, %s, %s)
    """, (
        student_id,
        attendance_date,
        status
    ))

    db.commit()

    cursor.close()
    db.close()

    flash("Attendance added successfully!", "success")

    return redirect(url_for("attendance"))


@app.route("/delete_attendance/<int:attendance_id>")
def delete_attendance(attendance_id):

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM attendance WHERE attendance_id=%s",
        (attendance_id,)
    )

    db.commit()

    cursor.close()
    db.close()

    flash("Attendance deleted successfully!", "success")

    return redirect(url_for("attendance"))

# =========================================================
# EXAMS
# =========================================================

@app.route("/exams")
def exams():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT exams.*,
               subjects.subject_name
        FROM exams
        LEFT JOIN subjects
        ON exams.subject_id = subjects.subject_id
        ORDER BY exams.exam_id
    """)

    exam_data = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM subjects
        ORDER BY subject_name
    """)

    subject_data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "exams.html",
        exams=exam_data,
        subjects=subject_data
    )


@app.route("/add_exam", methods=["POST"])
def add_exam():

    exam_name = request.form["exam_name"]
    subject_id = request.form["subject_id"]
    exam_date = request.form["exam_date"]

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO exams
        (exam_name, subject_id, exam_date)
        VALUES (%s, %s, %s)
    """, (
        exam_name,
        subject_id,
        exam_date
    ))

    db.commit()

    cursor.close()
    db.close()

    flash("Exam added successfully!", "success")

    return redirect(url_for("exams"))


@app.route("/delete_exam/<int:exam_id>")
def delete_exam(exam_id):

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            "DELETE FROM exams WHERE exam_id=%s",
            (exam_id,)
        )

        db.commit()

        flash("Exam deleted successfully!", "success")

    except mysql.connector.Error:
        db.rollback()

        flash(
            "Exam cannot be deleted because result records exist.",
            "danger"
        )

    cursor.close()
    db.close()

    return redirect(url_for("exams"))


# =========================================================
# RESULTS
# =========================================================

@app.route("/results")
def results():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT results.*,
               students.student_name,
               subjects.subject_name,
               exams.exam_name
        FROM results
        LEFT JOIN students
        ON results.student_id = students.student_id
        LEFT JOIN subjects
        ON results.subject_id = subjects.subject_id
        LEFT JOIN exams
        ON results.exam_id = exams.exam_id
        ORDER BY results.result_id DESC
    """)

    result_data = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY student_name
    """)

    student_data = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM subjects
        ORDER BY subject_name
    """)

    subject_data = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM exams
        ORDER BY exam_id
    """)

    exam_data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "results.html",
        results=result_data,
        students=student_data,
        subjects=subject_data,
        exams=exam_data
    )


@app.route("/add_result", methods=["POST"])
def add_result():

    student_id = request.form["student_id"]
    subject_id = request.form["subject_id"]
    exam_id = request.form["exam_id"]
    marks = float(request.form["marks"])

    if marks >= 40:
        result_status = "Pass"
    else:
        result_status = "Fail"

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO results
        (student_id, subject_id, exam_id, marks, result_status)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        student_id,
        subject_id,
        exam_id,
        marks,
        result_status
    ))

    db.commit()

    cursor.close()
    db.close()

    flash("Result added successfully!", "success")

    return redirect(url_for("results"))


@app.route("/delete_result/<int:result_id>")
def delete_result(result_id):

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM results WHERE result_id=%s",
        (result_id,)
    )

    db.commit()

    cursor.close()
    db.close()

    flash("Result deleted successfully!", "success")

    return redirect(url_for("results"))


# =========================================================
# RUN APPLICATION
# =========================================================

@app.route("/prediction", methods=["GET", "POST"])
def prediction():

    prediction_result = None
    probability = None

    if request.method == "POST":

        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        previous_marks = float(request.form["previous_marks"])
        assignment_score = float(request.form["assignment_score"])

        input_data = [[
            study_hours,
            attendance,
            previous_marks,
            assignment_score
        ]]

        prediction_value = model.predict(input_data)[0]
        prediction_probability = model.predict_proba(input_data)[0]

        if prediction_value == 1:
            prediction_result = "Likely to Pass"
        else:
            prediction_result = "Needs Improvement"

        probability = round(
            max(prediction_probability) * 100,
            2
        )

    return render_template(
        "prediction.html",
        prediction_result=prediction_result,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


