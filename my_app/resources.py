from flask_restful import Resource, request
from flask import abort, make_response
from mongoengine.errors import DoesNotExist
from my_app.models import User
from my_app.schemas import UserSchema
from my_app.utils import update_user
# ValidationError from mongoengine and marshmallow has been crossed that's why i made an aliases
from mongoengine.errors import ValidationError as MongoValidationError
from marshmallow.exceptions import ValidationError as MarshmallowValidationError


class UserResource(Resource):

    def get(self, id=None):
        if id:
            try:
                post = User.objects(id=id).first()
            except MongoValidationError as error:
                abort(400, f"{error}")
            return UserSchema().dump(post)
        else:
            posts = User.objects()
            return UserSchema().dump(posts, many=True)

    def post(self):
        try:
            data = UserSchema().load(request.get_json())
        except MarshmallowValidationError as error:
            return str(error)
        post_ = User.objects.create(**data)
        return UserSchema().dump(post_)

    def put(self, id):
        try:
            data = UserSchema().load(request.get_json())
            # method to update fields
            update_user(data, id)
        except (MarshmallowValidationError, MongoValidationError) as error:
            abort(400, f"{error}")
        new_author = User.objects(id=id)
        return UserSchema().dump(new_author, many=True)

    def delete(self, id):
        try:
            User.objects.get(id=id).delete()
        except (DoesNotExist, MongoValidationError) as error:
            abort(400, f"{error}")
        return make_response('No content', 204)