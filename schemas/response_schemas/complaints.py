from marshmallow import fields, Schema

from models import State
from schemas.base import ComplaintBaseSchema


class ComplaintResponseSchema(ComplaintBaseSchema):
    id = fields.String(required=True)
    created_at = fields.DateTime(required=True)
    status = fields.Enum(State, by_value=True)
    user_id = fields.Integer(required=True)
    # TODO : nest user inside this schema


class ComplaintsResponseSchema(Schema):
    # TODO : Make a list of object schemas
    complains = fields.Nested(ComplaintResponseSchema, many=True)


