from flask import Flask

app = Flask(__name__)

storage = {}


@app.route('/add/<date>/<int:number>')
def add(date, number):
    response_code = 200 if len(date) == 8 else 404
    year, month, day = date[:4], date[4:6], date[6:]
    storage.setdefault(f'{year}.{month}.{day}', 0)
    storage[f'{year}.{month}.{day}'] += number
    return f'{year}.{month}.{day} потрачено {number} рублей'


@app.route('/calculate/<int:year>')
def calculate_year(year):
    total_expenses = 0
    for date, expense in storage.items():
        if date.startswith(str(year)):
            total_expenses += expense
    return f'Всего потрачено в {year} году: {total_expenses} рублей'


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    total_expenses = 0
    for date, expense in storage.items():
        if date.startswith(f"{year}.{month:02d}"):
            total_expenses += expense
    return f'{year}.{month:02d} всего потрачено {total_expenses} рублей'


if __name__ == '__main__':
    app.run(debug=True)
