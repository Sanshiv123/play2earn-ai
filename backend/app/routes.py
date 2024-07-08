from flask import request, jsonify, current_app as app
from app import db
from app.models import User, Task
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to Play2Earn.ai!'})

bcrypt = Bcrypt()

@app.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not email or not password or not fname or not lname:
        return jsonify({'error': 'Email, password, first name, and last name are required'}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already registered. Please use a different email.'}), 400

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!', 'user_id': new_user.id}), 201
    except Exception as e:
        print("Failed to insert into User table:", e)
        db.session.rollback()
        return jsonify({'error': 'Registration failed'}), 500
        
@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
            data = request.get_json()
    else:
            data = request.form
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Generate JWT token
    expiration_time = datetime.utcnow() + timedelta(hours=1)  
    payload = {
        'username': user.username,
        'exp': expiration_time,
        'iat': datetime.utcnow() 
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'message': 'Login successful!', 'token': token}), 200