from database import db

class Users:
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    role = db.Column(db.String(120), unique=False, nullable=False)
    resume = db.Column(db.String(120), unique=False, nullable=False)
    experience = db.Column(db.Integer, unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    pincode = db.Column(db.Integer, unique=False, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=True)

    def __init__(self, name, email, password, role, resume, experience, address, pincode):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.resume = resume
        self.experience = experience
        self.address = address
        self.pincode = pincode


    def __repr__(self):
        return '<User %r>' % self.name
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "role": self.role,
            "resume": self.resume,
            "experience": self.experience,
            "address": self.address,
            "pincode": self.pincode
        }


class Service:
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    time_required = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, name, description, price, time_required):
        self.name = name
        self.description = description
        self.price = price
        self.time_required = time_required

    def __repr__(self):
        return '<Service %r>' % self.name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "time_required": self.time_required
        }