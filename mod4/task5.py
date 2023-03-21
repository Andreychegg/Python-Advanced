import shlex
import string
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/ps')
def get_ps():
    args = request.args.getlist('arg')
    clean_user_cmd = [shlex.quote(arg) for arg in args]
    cmd = shlex.split(f'ps {" ".join(clean_user_cmd)}')
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    result = result.stdout.decode()
    return string.Template('<pre>${output}</pre>').substitute(output=result)


if __name__ == '__main__':
    app.run(debug=True)
