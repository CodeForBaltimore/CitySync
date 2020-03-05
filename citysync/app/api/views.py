from flask import request, jsonify, Blueprint
from app.models import Nonprofit, NonprofitSchema

api_blueprint = Blueprint('api', __name__,)
npschema = NonprofitSchema()
npschemas = NonprofitSchema(many=True)

@api_blueprint.route("/api/orgs/all", methods=["GET"])
def get_orgs():
    all_orgs = Nonprofit.query.all()
    # paginate logic
    records = []
    for x, org in enumerate(all_orgs):
        records.append(org)
        if x == 10:
            break

    return npschemas.jsonify(records)


@api_blueprint.route("/api/orgs/id/<int:id>/", methods=["GET"])
def get_org_by_id(id):
    org = Nonprofit.query.get(id)
    return npschema.jsonify(org)


@api_blueprint.route("/api/orgs/id/<int:id>/address/", methods=["GET"])
def get_org_address_by_id(id):
    org = Nonprofit.query.get(id)
    only_these_fields = ["id", "ein", "name", "street", "city", "state", "zipcode"]
    return jsonify(({ attr : getattr(org, attr) for attr in only_these_fields}))


@api_blueprint.route("/api/orgs/ein/<int:ein>/", methods=["GET"])
def get_org_by_ein(ein):
    org = Nonprofit.query.filter(Nonprofit.ein == ein).first()
    return npschema.jsonify(org)


@api_blueprint.route("/api/orgs/ein/<int:ein>/address/", methods=["GET"])
def get_org_address_by_ein(ein):
    org = Nonprofit.query.filter(Nonprofit.ein == ein).first()
    only_these_fields = ["id", "ein", "name", "street", "city", "state", "zipcode"]
    return jsonify(({ attr : getattr(org, attr) for attr in only_these_fields}))




