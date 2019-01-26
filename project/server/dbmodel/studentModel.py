import jwt
import datetime

from project.server import app, db, bcrypt

class student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)