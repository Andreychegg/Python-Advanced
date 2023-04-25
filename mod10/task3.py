import sqlite3


def get_lines_count(table, cursor):
    cursor.execute(f'SELECT COUNT(*) FROM {table}')
    result = cursor.fetchone()[0]
    return result


with sqlite3.connect('hw_3_database.db') as conn:
    cursor = conn.cursor()

    print(f'В table_1 хранится {get_lines_count("table_1", cursor)} записей')
    print(f'В table_2 хранится {get_lines_count("table_2", cursor)} записей')
    print(f'В table_3 хранится {get_lines_count("table_3", cursor)} записей')

    unique_lines = cursor.execute('SELECT COUNT(DISTINCT value) FROM table_1').fetchone()[0]
    print(f'В table_1 {unique_lines} уникальных записей')

    lines_in_table_2 = cursor.execute('SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2)').fetchone()[0]
    print(f'{lines_in_table_2} записей из таблицы table_1 встречается в table_2')

    lines_in_table_2_and_3 = cursor.execute('SELECT COUNT(*) FROM table_1 WHERE value IN (SELECT value FROM table_2) AND value IN (SELECT value FROM table_3)').fetchone()[0]
    print(f'{lines_in_table_2_and_3} записей из таблицы table_1 встречается и в table_2, и в table_3')
