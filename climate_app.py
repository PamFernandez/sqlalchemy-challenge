import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> and /api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_date["date"] = date
        precipitation_prcp["precip"] = precip
        precipitation.append(precipitation_dict)
    print(precipitation)
    return jsonify(precipitation)











#    # Convert list of tuples into normal list
#    all_names = list(np.ravel(results))
#    print(all_names)
#    return jsonify(all_names)
#
#@app.route("/api/v1.0/passengers")
#def passengers():
#    # Create our session (link) from Python to the DB
#    session = Session(engine)
#
#    """Return a list of passenger data including the name, age, and sex of each passenger"""
#    # Query all passengers
#    results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()
#
#    session.close()
#
#    # Create a dictionary from the row data and append to a list of all_passengers
#    all_passengers = []
#    for name, age, sex in results:
#        passenger_dict = {}
#        passenger_dict["name"] = name
#        passenger_dict["age"] = age
#        passenger_dict["sex"] = sex
#        all_passengers.append(passenger_dict)
#    print(all_passengers)
#    return jsonify(all_passengers)
#
#if __name__ == '__main__':
#    app.run(debug=True)
