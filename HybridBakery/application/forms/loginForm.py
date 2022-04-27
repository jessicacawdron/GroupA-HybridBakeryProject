from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Login')
