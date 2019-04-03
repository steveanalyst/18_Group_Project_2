from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'a2ul0j0$'
# app.config['MYSQL_DB'] = 'StatePopulation'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:a2ul0j0$@127.0.0.1:3306/StatePopulation"

# mysql = MySQL(app)
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
States = Base.classes.population_new

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/names')
def names():
    # cur = mysql.connection.cursor()
    # cur.execute('''SELECT States FROM Population_new''')
    # results = cur.fetchall()

    stmt = db.session.query(States).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(list(df.States))

@app.route('/data/<entry>')
def sampleData(entry):

    sel = [
        States.States,
        States.yr_2010,
        States.yr_2011,
        States.yr_2012,
        States.yr_2013,
        States.yr_2014,
        States.yr_2015,
        States.yr_2016,
        States.yr_2017,
    ]

    results = db.session.query(*sel).filter(States.States == entry).all()

    data = {}
    for result in results:
        data["State"] = result[0]
        data["2010"] = result[1]
        data["2011"] = result[2]
        data["2012"] = result[3]
        data["2013"] = result[4]
        data["2014"] = result[5]
        data["2015"] = result[6]
        data["2016"] = result[7]
        data["2017"] = result[8]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)
