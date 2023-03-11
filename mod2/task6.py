import os

from flask import Flask

app = Flask(__name__)


@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size, relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(base_dir, relative_path)

    with open(relative_path, 'r') as file:
        text = file.read(size)
        length = len(text)
    return f'<b>{abs_path}</b> {length}<br>{text}'


if __name__ == '__main__':
    app.run(debug=True)
