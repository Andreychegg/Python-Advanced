from flask import Flask, url_for, request

app = Flask(__name__)


def get_endpoints():
    endpoints = list()
    for rule in app.url_map.iter_rules():
        if "static" not in str(rule.endpoint):
            endpoints.append(rule.endpoint)
    return endpoints


@app.errorhandler(404)
def page_not_found(error):
    endpoints = get_endpoints()
    links = ''
    for endpoint in endpoints:
        url = url_for(endpoint)
        full_url = request.host_url.rstrip('/') + url
        link = f'<li><a href="{full_url}">{full_url}</a></li>'
        links += link
    return f'Такой страницы не существует.<br>Доступные адреса:<ul>{links}</ul>', 404


@app.route('/hello_world')
def hello():
    return 'Привет, мир!'


@app.route('/about')
def about():
    return 'О нас'


@app.route('/good_day')
def good_day():
    return 'Хорошего дня!'


if __name__ == '__main__':
    app.run(debug=True)
