import sqlite3

get_employee_info = """
SELECT * 
    FROM table_effective_manager
    WHERE name LIKE ?
"""

fire_employee = """
DELETE 
    FROM table_effective_manager 
    WHERE name = ?
"""

raise_salary = """
UPDATE table_effective_manager 
    SET salary = ? 
    WHERE name = ?
"""


def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
        employee_name: str
) -> None:
    effective_manager_salary = cursor.execute(get_employee_info, ('Иван Совин', )).fetchone()[2]
    employee = cursor.execute(get_employee_info, (employee_name, )).fetchone()
    if employee_name == 'Иван Совин':
        print('Сотрудник является эффективным менеджером')
    else:
        employee_salary = employee[2] * 1.1
        if employee_salary > effective_manager_salary:
            cursor.execute(fire_employee, (employee_name, ))
            print('Сотрудник уволен')
        else:
            cursor.execute(raise_salary, (int(employee_salary), employee_name))
            print(f'Зарплата сотрудника повышена до {int(employee_salary)}')


if __name__ == '__main__':
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()

        employee_name = input('ФИО сотрудника: ')
        ivan_sovin_the_most_effective(cursor, employee_name)
