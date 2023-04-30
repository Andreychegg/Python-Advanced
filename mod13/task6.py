from datetime import datetime, timedelta
import sqlite3

weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
sports = ['футбол', 'хоккей', 'шахматы', 'SUP сёрфинг', 'бокс', 'Dota2', 'шах-бокс']


add_employee = """
INSERT INTO table_friendship_schedule (employee_id, date)
    VALUES (?,?)
"""

delete_table = """
DELETE FROM table_friendship_schedule
"""

get_employees = """
SELECT id, preferable_sport 
FROM table_friendship_employees
"""


def update_work_schedule(cursor: sqlite3.Cursor) -> None:
    cursor.execute(delete_table)
    employees = cursor.execute(get_employees).fetchall()
    worker_days = {employee[0]: 0 for employee in employees}
    current_day = datetime.strptime('2023-01-01', '%Y-%m-%d')
    work_days = {current_day + timedelta(days=i): 0 for i in range(366)}

    for day, employee in work_days.items():
        weekday = weekdays[day.weekday()]
        for id_employee, sport_employee in employees:
            if weekday == weekdays[sports.index(sport_employee)]:
                continue

            if worker_days[id_employee] != 11:
                cursor.execute(add_employee, (id_employee, day))
                worker_days[id_employee] += 1
                work_days[day] += 1
                if work_days[day] == 10:
                    break


if __name__ == '__main__':
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()

        update_work_schedule(cursor)
