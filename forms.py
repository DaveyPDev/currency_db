from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import requests



url = 'https://api.exchangerate.host/symbols'
response = requests.get(url)
data = response.json()
currencies = data['symbols']

class ConverterForm(FlaskForm):
    from_currency = SelectField('From Currency', choices=[(key, f"{key} - {value}") for key, value in currencies.items()], validators=[DataRequired()])
    to_currency = SelectField('To Currency', choices=[(key, f"{key} - {value}") for key, value in currencies.items()], validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Convert')


