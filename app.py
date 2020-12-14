from flask import Flask, jsonify, g
from flask_cors import CORS

import models

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# Logic for our database connection
@app.before_request
def before_request():
  """Connect to the database before each request."""
  g.db = models.DATABASE
  g.db.connect()


@app.after_request
def after_request(response):
  """Close the db connection after each requewst."""
  g.db.close()
  return response


CORS(states, origins='*', supports_credentials=True)

app.register_blueprint(state, url_prefix='/api/states')

if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)