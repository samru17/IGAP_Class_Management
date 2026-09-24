CREATE DATABASE IF NOT EXISTS igap_class_management;

USE igap_class_management;


-- ==========================================
-- TEACHERS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL,
    subject_specialization VARCHAR(100),
    phone VARCHAR(15)
);


-- ==========================================
-- CLASSES TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL,
    course_name VARCHAR(100),
    division VARCHAR(20),
    teacher_id INT,
    room_no VARCHAR(20),

    FOREIGN KEY (teacher_id)
        REFERENCES teachers(teacher_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


-- ==========================================
-- STUDENTS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    gender VARCHAR(20),
    age INT,
    phone VARCHAR(15),
    class_id INT,

    FOREIGN KEY (class_id)
        REFERENCES classes(class_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


-- ==========================================
-- SUBJECTS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    class_id INT,

    FOREIGN KEY (class_id)
        REFERENCES classes(class_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- ==========================================
-- ATTENDANCE TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- ==========================================
-- EXAMS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS exams (
    exam_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_name VARCHAR(100) NOT NULL,
    subject_id INT NOT NULL,
    exam_date DATE,

    FOREIGN KEY (subject_id)
        REFERENCES subjects(subject_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- ==========================================
-- RESULTS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    exam_id INT NOT NULL,
    marks DECIMAL(5,2),
    result_status VARCHAR(20),

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (subject_id)
        REFERENCES subjects(subject_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (exam_id)
        REFERENCES exams(exam_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- ==========================================
-- SAMPLE TEACHERS
-- ==========================================

INSERT INTO teachers
(teacher_name, subject_specialization, phone)
VALUES
('Prof. Rahul Patil', 'Python', '9876543210'),
('Prof. Sneha Joshi', 'Database Management', '9876543211');


-- ==========================================
-- SAMPLE CLASSES
-- ==========================================

INSERT INTO classes
(class_name, course_name, division, teacher_id, room_no)
VALUES
('B.Com CA', 'Computer Applications', 'A', 1, '101'),
('B.Com CA', 'Computer Applications', 'B', 2, '102');


-- ==========================================
-- SAMPLE STUDENTS
-- ==========================================

INSERT INTO students
(student_name, gender, age, phone, class_id)
VALUES
('Aarav Patil', 'Male', 20, '9876500001', 1),
('Sneha More', 'Female', 19, '9876500002', 1),
('Rohit Jadhav', 'Male', 20, '9876500003', 2);


-- ==========================================
-- SAMPLE SUBJECTS
-- ==========================================

INSERT INTO subjects
(subject_name, class_id)
VALUES
('Python Programming', 1),
('RDBMS', 1),
('Advanced Excel', 1);


-- ==========================================
-- SAMPLE EXAMS
-- ==========================================

INSERT INTO exams
(exam_name, subject_id, exam_date)
VALUES
('Unit Test 1', 1, '2026-09-25'),
('Unit Test 1', 2, '2026-09-26');


-- ==========================================
-- SAMPLE ATTENDANCE
-- ==========================================

INSERT INTO attendance
(student_id, attendance_date, status)
VALUES
(1, '2026-09-24', 'Present'),
(2, '2026-09-24', 'Present'),
(3, '2026-09-24', 'Absent');


-- ==========================================
-- SAMPLE RESULTS
-- ==========================================

INSERT INTO results
(student_id, subject_id, exam_id, marks, result_status)
VALUES
(1, 1, 1, 85, 'Pass'),
(2, 1, 1, 72, 'Pass'),
(3, 2, 2, 35, 'Fail');