import shlex
import subprocess
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


class Form(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[NumberRange(min=1, max=30)], default=10)


def run_subprocess(code, timeout):
    cmd = shlex.split(f'prlimit --nproc=1:1 python3 -c "{code}"')
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    killed = False
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        killed = True
    return stdout.decode(), stderr.decode(), killed


@app.route('/python', methods=['POST'])
def python():
    form = Form()
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data
        result, errors, killed = run_subprocess(code=code, timeout=timeout)
        if killed:
            return f'Исполнение кода не уложилось в данное время'
        else:
            return f'{result} {errors}'

    return f'Invalid input, {form.errors}', 400


if __name__ == '__main__':
    app.run(debug=True)
