import datetime as dt

from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app import ma


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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ein = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(60), unique=False, nullable=True)
    ico = db.Column(db.String(60), unique=False, nullable=True)
    street = db.Column(db.String(60), unique=False, nullable=False)
    raw_street = db.Column(db.String(60), unique=False, nullable=True)
    city = db.Column(db.String(60), unique=False, nullable=False)
    state = db.Column(db.String(2), unique=False, nullable=False)
    zipcode = db.Column(db.String(15), unique=False, nullable=False)
    latitude = db.Column(db.Float, unique=False, nullable=False)
    longitude = db.Column(db.Float, unique=False, nullable=False)
    geo_accuracy = db.Column(db.Float, unique=False, nullable=False)
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
    tax_period = db.Column(db.String(15), unique=False, nullable=True)
    asset_cd = db.Column(db.Integer, unique=False, nullable=False)
    income_cd = db.Column(db.Integer, unique=False, nullable=False)
    filing_req_cd = db.Column(db.Integer, unique=False, nullable=False)
    pf_filing_req_cd = db.Column(db.Integer, unique=False, nullable=False)
    acct_pd = db.Column(db.Integer, unique=False, nullable=False)
    asset_amt = db.Column(db.Integer, unique=False, nullable=False, default=-1)
    income_amt = db.Column(db.Integer, unique=False, nullable=False, default=-1)
    revenue_amt = db.Column(db.Integer, unique=False, nullable=False, default=-1)
    ntee = db.Column(db.String(10), unique=False, nullable=True)
    sort_name = db.Column(db.String(60), unique=False, nullable=True)
    activity_full = db.Column(db.String(250), unique=False, nullable=True)


    def __init__(self, id, name, ein, ico, street, raw_street, city, state, zipcode, latitude, longitude, geo_accuracy, group, subsection, affiliation, classification, ruling, deductability,
           foundation, activity, organization, status, tax_period, asset_cd, income_cd, filing_req_cd, pf_filing_req_cd, acct_pd, asset_amt, income_amt,
           revenue_amt, ntee, sort_name, activity_full):

        self.id 	      = id
        self.ein 	      = ein
        self.name             = name
        self.ico 	      = ico
        self.street 	      = street
        self.raw_street       = raw_street
        self.city 	      = city
        self.state 	      = state
        self.zipcode 	      = zipcode
        self.latitude         = latitude
        self.longitude        = longitude
        self.geo_accuracy     = geo_accuracy
        self.group 	      = group
        self.subsection       = subsection
        self.affiliation      = affiliation
        self.classification   = classification
        self.ruling 	      = ruling
        self.deductability    = deductability
        self.foundation       = foundation
        self.activity 	      = activity
        self.organization     = organization
        self.status 	      = status
        self.tax_period       = tax_period
        self.asset_cd         = asset_cd
        self.income_cd 	      = income_cd
        self.filing_req_cd    = filing_req_cd
        self.pf_filing_req_cd = pf_filing_req_cd
        self.acct_pd          = acct_pd
        self.asset_amt        = asset_amt
        self.income_amt       = income_amt
        self.revenue_amt      = revenue_amt
        self.ntee             = ntee
        self.sort_name        = sort_name
        self.activity_full    = activity_full


    def get_activity():
        pass


    def get_ntee():
        pass



class NonprofitSchema(ma.ModelSchema):
    class Meta:
        model = Nonprofit

        # To specialize fields something like so
#        fields = ('id', 'name', 'ein', 'ico', 'street', 'city', 'state', 'zipcode', 'group', 'subsection', 'affiliation', 'classification', 'ruling',
# 'deductability', 'foundation', 'activity', 'organization', 'status', 'tax_period', 'asset_cd','income_cd', 'filing_req_cd', 'pf_filing_req_cd',
# 'acct_pd', 'asset_amt', 'income_amt', 'revenue_amt', 'ntee', 'sort_name', 'activity_full')


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

