import datetime as dt

from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    activated = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=dt.datetime.now)

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __str__(self):
        return '<User> {}'.format(self.username)


class AnonymousUser(AnonymousUserMixin):
    pass


class Nonprofit(db.Model):

    __tablename__ = 'nonprofits'

    id = db.Column(db.Integer, primary_key=True)
    ein = db.Column(db.Integer, unique=True, nullable=False)
    ico = db.Column(db.String(60), unique=False, nullable=True)
    street = db.Column(db.String(60), unique=False, nullable=False)
    city = db.Column(db.String(60), unique=False, nullable=False)
    state = db.Column(db.String(2), unique=False, nullable=False)
    zipcode = db.Column(db.String(15), unique=False, nullable=False)
    group = db.Column(db.Integer, unique=False, nullable=False)
    subsection = db.Column(db.Integer, unique=False, nullable=False)
    affiliation = db.Column(db.Integer, unique=False, nullable=False)
    classification = db.Column(db.Integer, unique=False, nullable=False)
    ruling = db.Column(db.Integer, unique=False, nullable=False)
    deductability = db.Column(db.Integer, unique=False, nullable=False)
    foundation = db.Column(db.Integer, unique=False, nullable=False)
    activity = db.Column(db.Integer, unique=False, nullable=False)
    organization = db.Column(db.Integer, unique=False, nullable=False)
    status = db.Column(db.Integer, unique=False, nullable=False)
    tax_period = db.Column(db.Integer, unique=False, nullable=True)
    asset_cd = db.Column(db.Integer, unique=False, nullable=False)
    income_cd = db.Column(db.Integer, unique=False, nullable=False)
    filing_req_cd = db.Column(db.Integer, unique=False, nullable=False)
    pf_filing_req_cd = db.Column(db.Integer, unique=False, nullable=False)
    acct_pd = db.Column(db.Integer, unique=False, nullable=False)
    income_cd = db.Column(db.Integer, unique=False, nullable=False)
    asset_amt = db.Column(db.Integer, unique=False, nullable=True)
    income_amt = db.Column(db.Integer, unique=False, nullable=True)
    revenue_amt = db.Column(db.Integer, unique=False, nullable=True)
    ntee = db.Column(db.String(10), unique=False, nullable=True)
    sort_name = db.Column(db.String(60), unique=False, nullable=True)
    activity_full = db.Column(db.String(250), unique=False, nullable=True)

    def get_activities():
        pass


    def get_ntee():
        pass



