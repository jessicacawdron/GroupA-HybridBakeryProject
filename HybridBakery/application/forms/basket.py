from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField
class AddToBasketForm(FlaskForm):
    quantity = IntegerField('Quantity')
    submit = SubmitField('Add to basket')