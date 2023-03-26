from time import sleep
from flask import Flask
import signal
import subprocess
import os


def run_server(port):
    app = Flask(__name__)

    @app.route('/test')
    def test():
        return f'Success'

    try:
        app.run(port=port)
    except:
        data = subprocess.check_output(['lsof', '-i', ':' + str(port)]).decode()
        lines = data.strip().split("\n")
        PIDs = [line.split()[1] for line in lines[1:]]
        for pid in PIDs:
            os.kill(int(pid), signal.SIGTERM)
        sleep(1)
        app.run(port=port)


port = int(input('Введите порт: '))
if __name__ == '__main__':
    run_server(port)
