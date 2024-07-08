from flask import request, jsonify, current_app as app
from app import db
from app.models import User, Task

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to Play2Earn.ai!'})

