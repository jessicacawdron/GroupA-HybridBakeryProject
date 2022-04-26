from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AddressForm(FlaskForm):
    first_line = StringField('First Line', validators=[DataRequired()])
    second_line = StringField('Second Line')
    town = StringField('Town', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Not a valid email address')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20, message='Not a Valid Password. Passwords must be between 5 and 20 characters')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords do not match')])
    first_name = StringField('First_Name', validators=[DataRequired(), Length(max=35)])
    last_name = StringField('Last_Name', validators=[DataRequired(), Length(max=35)])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    home_address = FormField(AddressForm)
    submit = SubmitField('Sign Up')