from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validate
)


class UserSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(validate=validate.Length(min=2) ,required=True)
    country = fields.String(validate=validate.Length(min=3))
    address = fields.String(validate=validate.Length(min=5))
    email_address = fields.Email(validate=validate.Length(min=5))
