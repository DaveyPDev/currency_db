from flask import Flask, render_template, redirect, session, flash, request, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from forms import ConverterForm
from models import connect_db, db, Currency, _app_ctx_stack, DecimalEncoder
from werkzeug.exceptions import Unauthorized
import requests



url = 'https://api.exchangerate.host'
response = requests.get(url)
data = response.json()

print(data)

app = Flask(__name__, template_folder='templates') 
app.json_encoder = DecimalEncoder
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/currency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'not$secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)


@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND page."""
    return render_template('404.html'), 404

@app.route('/')
def home_page():
    return redirect('/converter')

@app.route('/converter', methods=["GET", "POST"])
def convert_currency():
    form = ConverterForm()

    print(f'Method: {request.method}')

    if form.validate_on_submit():
        print('Form submitted')
        session['from_currency'] = form.from_currency.data
        session[' to_currency'] = form.to_currency.data
        session['amount'] = form.amount.data

        print(f'Form Data: from_currency={session["from_currency"]}, to_currency={session["to_currency"]}, amount={session["amount"]}')

        url = f'https://api.exchangerate.host/convert?from={session["from_currency"]}&to={session["to_currency"]}&amount={session["amount"]}'
        response = requests.get(url)
        
        data = response.json()
        session['result'] = data['result']

        print(f'API Response: {data}')

        print(f'Session Variables: result={session["result"]}, from_currency={session["from_currency"]}, to_currency={session["to_currency"]}')

        return redirect(url_for('show_results'))

    print('Form not submitted')
    print(form.errors)
    return render_template('converter.html', form=form)



@app.route('/results')
def show_results():
    from_currency = session.get('from_currency')
    to_currency = session.get('to_currency')
    result = session.get('result')

    if result is None or from_currency is None or to_currency is None:
        flash('No result found')
        return redirect('/converter')
    
    print(f'Show Results: from_currency={from_currency}, to_currency={to_currency}, result={result}')
   
    return render_template('results.html', from_currency=from_currency, to_currency=to_currency, result=result)

if __name__ == '__main__':
    app.run()
