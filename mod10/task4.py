import sqlite3

with sqlite3.connect('hw_4_database.db') as conn:
    cursor = conn.cursor()

    poor_people = cursor.execute('SELECT COUNT(*) FROM salaries WHERE salary < 5000').fetchone()[0]
    print(f'{poor_people} человек находятся за чертой бедности')

    avg_salary = cursor.execute('SELECT AVG(salary) FROM salaries').fetchone()[0]
    print(f'Средняя зарплата по острову: {avg_salary}')

    sorted_salaries = cursor.execute('SELECT salary FROM salaries ORDER BY salary').fetchall()
    median_salary = sorted_salaries[len(sorted_salaries) // 2][0]
    print(f'Медианная зарплата по острову: {median_salary}')

    total = cursor.execute('SELECT COUNT(salary) FROM salaries').fetchone()[0]
    top10 = f'SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {total}'
    top10_salary = cursor.execute(f'SELECT SUM(salary) FROM ({top10})').fetchone()[0]
    sum_salary = cursor.execute('SELECT SUM(salary) FROM salaries').fetchone()[0]
    top90 = sum_salary - top10_salary
    social_inequality = round(top10_salary / top90 * 100, 2)
    print(f'Социальное неравенство = {social_inequality}%')
