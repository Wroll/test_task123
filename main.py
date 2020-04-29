from flask import Flask
from flask_restful import Api
from my_app.resources import UserResource


app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/', '/user/<id>', '/delete_user/<id>', '/update_user/<id>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")