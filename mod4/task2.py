from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, Field
from wtforms.validators import InputRequired, Email, ValidationError, Optional

app = Flask(__name__)


def number_length(min: int, max: int, message: Optional = None):

    def _number_length(form: FlaskForm, field: Field):
        if not (min <= len(str(field.data)) <= max):
            if message is not None:
                raise ValidationError(message)
            else:
                raise ValidationError(f'Неверный формат номера телефона')

    return _number_length


class NumberLength:
    def __init__(self, min, max, message=None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form, field):
        if not (self.min <= len(str(field.data)) <= self.max):
            if self.message is not None:
                raise ValidationError(self.message)
            else:
                raise ValidationError(f'Неверный формат номера телефона')


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), number_length(10, 10), NumberLength(10, 10)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route('/registration', methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f'Successfully registered user {email} with phone +7{phone}'

    return f'Invalid input, {form.errors}', 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
