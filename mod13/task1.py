import sqlite3

get_count_temperature_violations = """
SELECT COUNT(*)
    FROM(SELECT *
         FROM table_truck_with_vaccine 
         WHERE truck_number = ? AND temperature_in_celsius NOT BETWEEN 16 and 20)
"""


def check_if_vaccine_has_spoiled(
        cursor: sqlite3.Cursor,
        truck_number: str
) -> bool:
    result = cursor.execute(get_count_temperature_violations, (truck_number,)).fetchone()[0]
    return result > 2


if __name__ == '__main__':
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()

        truck_number = input('Номер грузовика: ')
        if check_if_vaccine_has_spoiled(cursor, truck_number):
            print('Вакцина испорчена')
        else:
            print('Вакцина не испорчена')
