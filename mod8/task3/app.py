import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/newyear')
def new_year():
    new_year_date = datetime.datetime(2024, 1, 1, 0, 0, 0)
    time_left = new_year_date - datetime.datetime.now()

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f'<b>До Нового Года осталось {days} дней, {hours} часов, {minutes} минут, {seconds} секунд</b>'


if __name__ == '__main__':
    app.run()
