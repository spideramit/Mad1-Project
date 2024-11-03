from flask import Flask, render_template
from flask_restful import Api
from application.api import UsersResource, UserResource, ServicesResource, ServiceResource
from application.database import db


app = Flask(__name__)
api = Api(app)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')



#  Adding resources to API
api.add_resource(UsersResource, '/users')  # For creating and getting all users
api.add_resource(UserResource, '/users/<int:id>')  # For operations on specific users (get, put, delete)

api.add_resource(ServicesResource, '/services')  # For creating and getting all services
api.add_resource(ServiceResource, '/services/<int:id>')  # For operations on specific services (get, put, delete)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 