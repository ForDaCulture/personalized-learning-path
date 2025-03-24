from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade_level = db.Column(db.Integer)
    learning_style = db.Column(db.String(50))

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50))  # e.g., Basic, Intermediate, Advanced
    type = db.Column(db.String(50))   # e.g., Video, Text, Audio

class LearningPath(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
    recommended_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='in progress')