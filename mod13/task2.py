import csv
import sqlite3

delete_fees = """
    DELETE FROM table_fees
        WHERE truck_number = ? AND timestamp = ?
"""


def delete_wrong_fees(
        cursor: sqlite3.Cursor,
        wrong_fees_file: str
) -> None:
    with open(wrong_fees_file, 'r') as file:
        wrong_fees_list = list(csv.reader(file))[1:]
        for wrong_fee in wrong_fees_list:
            cursor.execute(delete_fees, (wrong_fee[0], wrong_fee[1]))


if __name__ == '__main__':
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()

        delete_wrong_fees(cursor, 'wrong_fees.csv')
