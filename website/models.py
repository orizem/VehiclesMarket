# models.py

from email.policy import default
from pyexpat import model
from time import timezone
from turtle import color
from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    full_name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    # Profile attributes
    phone_number = db.Column(db.String(50))
    state = db.Column(db.String(50))
    city = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    profession = db.Column(db.String(50))
    addition_details = db.Column(db.Text)
    img = db.Column(db.String(1000000), unique=True)
    img_name = db.Column(db.String(1000), unique=True)



# class User(UserMixin, db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     full_name = db.Column(db.String(100))
#     email = db.Column(db.String(100), unique=True)
#     nickname = db.Column(db.String(100))
#     phone = db.Column(db.String(100))
#     state = db.Column(db.String(100))
#     city = db.Column(db.String(100))
#     gender = db.Column(db.String(10))
#     profession = db.Column(db.String(100))
#     aditional_details = db.Column(db.String(255))
#     img = db.Column(db.String(100))
#     img_name = db.Column(db.String(500))
#     date_created = db.Column(db.DateTime) #(timezone=True), default=func.now())
#     password = db.Column(db.String(100))

#     # one-to-many collection
#     questions = db.relationship("Question", back_populates="user")


# class Vehicle(db.Model):
#     __tablename__ = "vehicle"
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     company = db.Column(db.String(100))
#     model = db.Column(db.String(100))
#     is_auto = db.Column(db.Boolean)
#     year = db.Column(db.Integer)
#     color = db.Column(db.String(25))
#     km = db.Column(db.Float)
#     price = db.Column(db.Integer)
#     owner_id = db.Column(db.Integer)
#     buyer_id = db.Column(db.Integer)
#     date_upload = db.Column(db.DateTime)
#     date_sold = db.Column(db.DateTime)
#     status = db.Column(db.String(25))

#     # one-to-many collection
#     questions = db.relationship("Question", back_populates="vehicle")


# class Question(db.Model):
#     __tablename__ = "question"
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     content = db.Column(db.String(255))

#     # many-to-one scalar
#     vehicle = db.relationship("vehicle", back_populates="question")
#     vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"))

#     # one-to-one Question.answer
#     answer = db.relationship("Answer", back_populates="question", uselist=False)
#     answer_id = db.Column(db.Integer, db.ForeignKey("answer.id"))

#     # one-to-one Question.user
#     user = db.relationship("User", back_populates="question", uselist=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    

# class Answer(db.Model):
#     __tablename__ = "answer"
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     content = db.Column(db.String(255))

#     # one-to-one answer.question
#     question = db.relationship("Question", back_populates="answer", uselist=False)
#     question_id = db.Column(db.Integer, db.ForeignKey("question.id"))

#     # one-to-one Answer.user
#     user = db.relationship("User", back_populates="answer", uselist=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))



