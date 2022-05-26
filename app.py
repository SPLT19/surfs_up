#Import the Flask Dependency
from flask import Flask

#Flask App Instance Creation
app = Flask(__name__)

#Flask Routes
@app.route('/')

#hello_world() funciton test
def hello_world():
    return 'Hello world'