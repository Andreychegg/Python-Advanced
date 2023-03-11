from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:numbers>/')
def max_number(numbers):
    numbers = numbers.split('/')
    try:
        nums_list = list(map(int, numbers))
    except ValueError:
        return f'Ошибка: в URL передано не число.'
    else:
        print(nums_list)
        max_num = max(nums_list)
        return f'Максимальное число: <em>{str(max_num)}</em>'


if __name__ == '__main__':
    app.run(debug=True)
