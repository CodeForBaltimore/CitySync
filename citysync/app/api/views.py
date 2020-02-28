from flask import request, jsonify, Blueprint
from app.models import Nonprofit

api_blueprint = Blueprint('api', __name__,)

@api_blueprint.route("/api/orgs/", methods=["GET"])
def get_orgs():
    all_orgs = Nonprofit.query.order_by(Nonprofit.ein).all()
    for org in all_orgs:
        f = open("/tmp/vimp", "w")
        f.write("Sneaky Deaky ein: {}, {}".format(org.ein, org.id))
        f.write(org.__dict__)
    return (org.serialize())


@api_blueprint.route("/api/orgs/<int:ein>/", methods=["GET"])
def get_org_ein(ein):
    #for ein in 
    return render_template("main/about.html")
