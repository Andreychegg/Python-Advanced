from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/hello-world/<string:name>')
def hello_name(name):
    global weekdays_tuple
    weekday = datetime.today().weekday()
    if weekday in (2, 4, 5):
        good = 'Хорошей'
    else:
        good = 'Хорошего'
    return f'Привет, {name}. {good} {weekdays_tuple[weekday]}!'


weekdays_tuple = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')

if __name__ == '__main__':
    app.run(debug=True)
