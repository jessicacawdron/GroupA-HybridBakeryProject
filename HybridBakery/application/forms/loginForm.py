from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField


class LoginForm(FlaskForm):
    email = StringField('Email')
    pass_word = PasswordField('Password')
    submit = SubmitField('Login')
