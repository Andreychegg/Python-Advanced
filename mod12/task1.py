import time
import requests
import sqlite3
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool


def fill_database(url):
    data = requests.get(url).json()
    conn = sqlite3.connect('starwars_characters.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS characters
                    (id INTEGER PRIMARY KEY,
                     name TEXT,
                     birth_year TEXT,
                     gender TEXT)''')

    name = data['name']
    birth_year = data['birth_year']
    gender = data['gender']

    cursor.execute("INSERT INTO characters (name, birth_year, gender) VALUES (?, ?, ?)",
                   (name, birth_year, gender))
    conn.commit()
    conn.close()


def fill_table_with_pool(base_url):
    start = time.time()
    urls = [f'{base_url}{n}/' for n in range(1, 22) if n != 17]

    with Pool() as pool:
        pool.map(fill_database, urls)

    print('Время выполнения с использованием Pool: {:.4}'.format(time.time() - start))


def fill_table_with_threadpool(base_url):
    start = time.time()
    urls = [f'{base_url}{n}/' for n in range(1, 22) if n != 17]

    with ThreadPool() as pool:
        pool.map(fill_database, urls)

    print('Время выполнения с использованием ThreadPool: {:.4}'.format(time.time() - start))


if __name__ == '__main__':
    base_url = 'https://swapi.dev/api/people/'
    # fill_table_with_pool(base_url)
    fill_table_with_threadpool(base_url)
