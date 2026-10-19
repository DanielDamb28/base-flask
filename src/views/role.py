from src.app import ma
from marshmallow import fields

class RoleSchema(ma.Schema):
    role_id = fields.Integer(attribute="id")
    role_name = fields.String(attribute="name")