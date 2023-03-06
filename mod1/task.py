import os
from datetime import datetime, timedelta
from random import choice
import re

from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    global cars
    return f'{", ".join(cars)}'


@app.route('/cats')
def cats():
    global cats
    return choice(cats)


@app.route('/get_time/now')
def time_now():
    current_time = datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def time_future():
    current_time = datetime.now()
    current_time_after_hour = current_time + timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def random_word():
    return choice(words)


def get_words():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

    with open(BOOK_FILE, 'r', encoding='utf-8') as book:
        file = book.read()
        words = re.findall(r"\w+", file)
    return words


@app.route('/counter')
def counter():
    counter.visits += 1
    return str(counter.visits)


counter.visits = 0


cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
words = get_words()

if __name__ == '__main__':
    app.run(debug=True)
