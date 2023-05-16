SELECT
    students.group_id,
    COUNT(DISTINCT students.student_id) AS count,
    AVG(ag.grade) AS average_grade,
    COUNT(DISTINCT CASE WHEN ag.grade IS NULL THEN students.student_id END) AS not_hand_work_count,
    COUNT(DISTINCT CASE WHEN ag.date > a.due_date THEN students.student_id END) AS miss_deadline_count,
    COUNT(DISTINCT ag.grade_id) AS retries_count
FROM students
LEFT JOIN assignments_grades ag ON students.student_id = ag.student_id
LEFT JOIN assignments a ON ag.assisgnment_id = a.assisgnment_id
GROUP BY students.group_id;