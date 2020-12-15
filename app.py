from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import os

DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))

ENV = 'prod'

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)
if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  os.path.join(basedir, 'everystate.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
else:
    DEBUG = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://arylqgtqaiklsp:1a5f7f4f83f7d7cb6a748b8fe5d99fa990bf00df944bde85afdf7096022294e3@ec2-54-211-238-131.compute-1.amazonaws.com:5432/dd6k37pt995nvc'
db = SQLAlchemy(app)


class State(db.Model):
    __tablename__ = 'State'
    _id = db.Column('id', db.Integer, primary_key=True)
    state = db.Column('state', db.String(25))
    programming_language = db.Column('programming_language', db.String(20))
    number_of_jobs = db.Column('number_of_jobs', db.Integer)

    def __init__(self, state, programming_language, number_of_jobs):
        self.state = state
        self.programming_language = programming_language
        self.number_of_jobs = number_of_jobs

# Logic for our database connection
# @app.before_request
# def before_request():
#   """Connect to the database before each request."""
#   db.connect()


@app.route('/', methods=["POST"])
def post_new_state():
    try:
        state = request.form['state']
        programming_language = request.form['programming_language']
        number_of_jobs = int(request.form['number_of_jobs'])
        new_state = State(state, programming_language, number_of_jobs)
        print("it was a form request")
    except:
        payload = request.get_json()
        state = payload['state']
        programming_language = payload['programming_language']
        number_of_jobs = payload['number_of_jobs']
        new_state = State(state, programming_language, number_of_jobs)
    try:
        db.session.add(new_state)
        db.session.commit()
        print('it worked')
        return jsonify({state:{programming_language: number_of_jobs}})
    except:
        return(jsonify('null'))
        # return jsonify(data={}, status={"code": 200, "message": "Error getting the resources"})


@app.route('/', methods=['GET'])
def find_data():
    answer = request.get_json()
    # print(answer['state'], answer['programming_language'])
    # langanswerrequest.form['programming_language']
    # print(answer)
    results = State.query.all()
    # print(len(results))
    l = {}
    for i in results:
        # print([i.state, i.programming_language, i.number_of_jobs])
        if i.state not in l:
            l[i.state] =  {}
        if i.programming_language not in l:
            l[i.state][i.programming_language] = i.number_of_jobs
        # print(l[i.state])
        # l[i.state][i.programming_language] = i.number_of_jobs
    print(l)
    # print(l)
    try:
        return jsonify(l)
    except: 
        return jsonify({"message": "error"})
# @app.after_request
# def after_request(response):
#   """Close the db connection after each requewst."""
#   db.close()
#   return response


CORS(origins='*', supports_credentials=True)


if __name__ == '__main__':
  app.run(port=8003)