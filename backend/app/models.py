from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    profile_pic_url = db.Column(db.String(200))
    tasks_completed = db.Column(db.Integer, default=0)
    total_rewards = db.Column(db.Float, default=0.0)
    tasks = db.relationship('Task', backref='user', lazy=True)
    analytics = db.relationship('Analytics', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    reward = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Task {self.title}>"

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # Hashed password should be stored
    profile_pic_url = db.Column(db.String(200))

    def __repr__(self):
        return f"<Admin {self.username}>"

class Analytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer, nullable=False)
    tasks_completed = db.Column(db.Integer, nullable=False)
    rewards_earned = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Analytics for User {self.user_id} - Week {self.week_number}>"
