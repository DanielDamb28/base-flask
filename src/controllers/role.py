from flask import Blueprint, request
from ..models import Role, db
from http import HTTPStatus
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils import required_role

app = Blueprint('role', __name__, url_prefix='/roles')


@jwt_required()
@required_role("admin")
@app.route("/", methods=["POST"])
def create_role():
    data= request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()

    return {"message": "Role Created!"}, HTTPStatus.CREATED