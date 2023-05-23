import time
import requests
import sqlite3
import threading


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


def fill_table(base_url):
    start = time.time()
    for n in range(1, 22):
        if n == 17:
            continue
        url = f'{base_url}{n}/'
        fill_database(url)
    print('Время выполнения без использования потоков: {:.4}'.format(time.time() - start))


def fill_table_with_threads(base_url):
    start = time.time()
    threads = []
    for n in range(1, 22):
        if n == 17:
            continue
        url = f'{base_url}{n}/'
        thread = threading.Thread(target=fill_database, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print('Время выполнения с использованием потоков: {:.4}'.format(time.time() - start))


if __name__ == '__main__':
    base_url = 'https://swapi.dev/api/people/'
    # fill_table(base_url)
    fill_table_with_threads(base_url)
