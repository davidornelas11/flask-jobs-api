from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app.config['SQLALCHEMY_DATABSE_URI'] = 'postgres://qosgxgbtgrgcon:0b3052b2e33c963162695b314fe14641178edbcdee2bb25d7dd6fcf0007b86cd@ec2-3-216-89-250.compute-1.amazonaws.com:5432/d1us7navtfu14d'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class State(db.Model):
  _id = db.Column('id', db.Integer, primary_key=True)
  state = db.Column('state', db.String(25))
  programming_language = db.Column('programming_language', db.String(20))
  number_of_jobs = db.Column('number_of_jobs', db.Integer)
  created_at = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = db

def initialize():
  db.connect()
  db.create_all()
  print("TABLES Created")
  db.close()