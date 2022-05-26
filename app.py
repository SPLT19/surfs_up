#Import the Flask Dependency
#from flask import Flask
#Flask App Instance Creation
#app = Flask(__name__)
#Flask Routes
#@app.route('/')
#hello_world() funciton test
#def hello_world():
   # return 'Hello world'

#Weather APP dependencies import
import datetime as dt
import numpy as np
import pandas as pd

#SQLlite-SQLAlchemy database dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#code to import dependencies for Flask
from flask import Flask, jsonify

#Setting up database engine for the Flask application 
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database into classes
Base = automap_base()

#reflect the tables into SQLAlchemy
Base.prepare(engine, reflect=True)

#save references to each table (Measurement, Station)
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link from Python to database
session = Session(engine)

#Set Up Flask
#define our Flask app, application called "app."
app = Flask(__name__)

#Setting routes, routes should go after app = Flask(__name__) line of code.
#define welcome route
@app.route("/")

#add the routing information for other routes, create a function welcome()
def welcome():
    return(

#add the precipitation, stations, tobs, and temp routes
       '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')