from flask import request, jsonify, Blueprint
from app.models import Nonprofit, NonprofitSchema
np = NonprofitSchema()

api_blueprint = Blueprint('api', __name__,)

@api_blueprint.route("/api/orgs/", methods=["GET"])
def get_orgs():
    all_orgs = Nonprofit.query.order_by(Nonprofit.ein).get(3)
    #f = open("/tmp/vimp", "w")
    #f.write("Sneaky Deaky ein: {}, {}".format(all_orgs.ein, all_orgs.id))
    #f.write("\n {}".format(jsonify(all_orgs)))
    #f.close()
    return np.jsonify(all_orgs)


@api_blueprint.route("/api/orgs/<int:ein>/", methods=["GET"])
def get_org_ein(ein):
    #for ein in 
    return render_template("main/about.html")
