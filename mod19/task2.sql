SELECT full_name, AVG(assignments_grades.grade) as average_grade
FROM students
JOIN assignments_grades ON students.student_id = assignments_grades.student_id
GROUP BY full_name
ORDER BY average_grade DESC
LIMIT 10;