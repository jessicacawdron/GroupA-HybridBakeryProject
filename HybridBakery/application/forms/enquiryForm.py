from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EnquiryForm(FlaskForm):
    email_enquiry = StringField('Email')
    full_name = StringField('Name')
    message = StringField('Type your message here:')
    submit = SubmitField('Submit')
