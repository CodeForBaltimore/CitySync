from flask import request, jsonify, Blueprint
from app.models import Nonprofit

api_blueprint = Blueprint('api', __name__,)

@api_blueprint.route("/api/orgs/", methods=["GET"])
def get_orgs():
    all_orgs = Nonprofits.query.all()
    return jsonify(all_orgs)


@api_blueprint.route("/api/orgs/<int:ein>/", methods=["GET"])
def get_org_ein(ein):
    #for ein in 
    return render_template("main/about.html")
