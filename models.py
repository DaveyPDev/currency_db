from flask_sqlalchemy import SQLAlchemy
from werkzeug.local import Local
from datetime import datetime
_app_ctx_stack = Local()
import decimal
from decimal import Decimal
import json



# from flask_bcrypt import Bcrypt


db = SQLAlchemy()
# bcrypt = Bcrypt()

def connect_db(app):
    """ Connect to Database """

    db.app = app
    db.init_app(app)

class Currency(db.Model):

    __tablename__ = 'currency'

    id = db.Column(db.Integer, primary_key=True)

    from_currency = db.Column(db.Text, nullable=False)
    to_currency = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    submit = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)