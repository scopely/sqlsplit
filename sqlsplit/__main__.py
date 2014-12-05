"""Start the server and whatnot."""
from os import environ
from flask import Flask, request
import sqlparse
import json

app = Flask(__name__)

@app.route('/')
def home():
	return "Post your SQL as form data in the field 'sql' to /split.";

@app.route('/split', methods = ['POST'])
def split_sql():
	return json.dumps({"result": sqlparse.split(request.form['sql'])})

if __name__ == '__main__':
   app.run(debug=not environ.get("PROD", False))