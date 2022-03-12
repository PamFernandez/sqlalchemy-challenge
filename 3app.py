import numpy as np
import datetime as dt

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
        f"/api/v1.0/ enter start date<br/>"
        f"/api/v1.0/ enter start and end dates<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip_list = dict(precip)
    
    print(precip_list)
    return jsonify(precip_list)



@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations_all = session.query(Station.station, Station.name).all()
    station_list = dict(stations_all)
    
    print(station_list)
    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    station_tobs = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= query_date).all()
    station_temps = dict(station_tobs)

    print(station_temps)
    return jsonify(station_temps)













# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)