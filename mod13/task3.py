import sqlite3
from datetime import datetime

add_bird = """
INSERT INTO table_with_birds (bird_name, date_when_added) VALUES (?, ?);
"""

check_bird_already_seen = """
SELECT EXISTS (SELECT 1 FROM table_with_birds WHERE bird_name = ? LIMIT 1)
"""


def log_bird(
        cursor: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    cursor.execute(add_bird, (bird_name, date_time))


def check_if_such_bird_already_seen(
        cursor: sqlite3.Cursor,
        bird_name: str
) -> bool:
    result = cursor.execute(check_bird_already_seen, (bird_name, )).fetchone()[0]
    return result


if __name__ == '__main__':
    bird_name = input('Название птицы: ')
    datetime_now = datetime.utcnow().isoformat()
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()

        if check_if_such_bird_already_seen(cursor, bird_name):
            print('Вы уже видели эту птицу раньше')
        else:
            print('Вы не видели эту птицу раньше')
        log_bird(cursor, bird_name, datetime_now)
