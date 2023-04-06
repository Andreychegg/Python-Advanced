import logging
from dict_config import dict_config
from flask import Flask, request
from logging import config

app = Flask(__name__)


logging.config.dictConfig(dict_config)
logger = logging.getLogger('flask')


@app.route('/logs_post', methods=['POST'])
def logs_post():
    data = request.json
    service = data.pop('service')
    level = getattr(logging, data['level'].upper())
    logger.log(level, f'{service}: {data["message"]}', extra=data)
    return 'Success'


@app.route('/logs', methods=['GET'])
def logs():
    with open('utils.log', 'r') as file:
        data = file.read().replace('\n', '</br>')
    return data


if __name__ == '__main__':
    app.run(debug=True)
