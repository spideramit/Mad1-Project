from flask import jsonify, request
from app import app
from app import api
from database import db
from models import Users, Service
from flask_restful import Resource


# Users Resource
class UsersResource(Resource):
    # Get all users (GET)
    def get(self):
        users = Users.query.all()
        return jsonify([user.json() for user in users])

    # Create a new user (POST)
    def post(self):
        data = request.get_json()
        new_user = Users(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            role=data['role'],
            resume=data['resume'],
            experience=data['experience'],
            address=data['address'],
            pincode=data['pincode']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.json()), 201

class UserResource(Resource):
    # Get a specific user by ID (GET)
    def get(self, id):
        user = Users.query.get_or_404(id)
        return jsonify(user.json())

    # Update a user by ID (PUT)
    def put(self, id):
        user = Users.query.get_or_404(id)
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
        user.role = data['role']
        user.resume = data['resume']
        user.experience = data['experience']
        user.address = data['address']
        user.pincode = data['pincode']
        db.session.commit()
        return jsonify(user.json())

    # Delete a user by ID (DELETE)
    def delete(self, id):
        user = Users.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200

# Service Resource
class ServicesResource(Resource):
    # Get all services (GET)
    def get(self):
        services = Service.query.all()
        return jsonify([service.json() for service in services])

    # Create a new service (POST)
    def post(self):
        data = request.get_json()
        new_service = Service(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            time_required=data['time_required']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.json()), 201

class ServiceResource(Resource):
    # Get a specific service by ID (GET)
    def get(self, id):
        service = Service.query.get_or_404(id)
        return jsonify(service.json())

    # Update a service by ID (PUT)
    def put(self, id):
        service = Service.query.get_or_404(id)
        data = request.get_json()
        service.name = data['name']
        service.description = data['description']
        service.price = data['price']
        service.time_required = data['time_required']
        db.session.commit()
        return jsonify(service.json())

    # Delete a service by ID (DELETE)
    def delete(self, id):
        service = Service.query.get_or_404(id)
        db.session.delete(service)
        db.session.commit()
        return jsonify({"message": "Service deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
