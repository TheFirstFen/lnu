CREATE SCHEMA
IF NOT EXISTS students_db DEFAULT CHARACTER
SET utf8mb3;

USE students_db;

CREATE TABLE
IF NOT EXISTS students
(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR
(255) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR
(255) NOT NULL,
)

INSERT INTO students
    (name, age, grade)
VALUES
    ('John Doe', 20, 'C'),
    ('Jane Smith', 22, 'E'),
    ('Michael Johnson', 21, 'B');