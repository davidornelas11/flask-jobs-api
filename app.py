from flask import Flask, jsonify, g, Blueprint, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import datetime
import os

DEBUG = True
PORT = 8001
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  os.path.join(basedir, 'everystate.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    state = request.form['state']
    programming_language = request.form['programming_language']
    number_of_jobs = int(request.form['number_of_jobs'])
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
    return jsonify(l)
    return jsonify({results[0].state:results[0].programming_language})

# @app.after_request
# def after_request(response):
#   """Close the db connection after each requewst."""
#   db.close()
#   return response


CORS(origins='*', supports_credentials=True)


if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)