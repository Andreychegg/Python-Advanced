from flask import Flask
import subprocess

app = Flask(__name__)


@app.route('/uptime', methods=['GET'])
def get_uptime():
    UPTIME = subprocess.check_output(['uptime', '-p']).decode()
    return f"Current uptime is {UPTIME}"


if __name__ == '__main__':
    app.run(debug=True)
