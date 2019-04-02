from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL
import pandas as pd

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'a2ul0j0$'
app.config['MYSQL_DB'] = 'StatePopulation'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/states')
def states():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT States FROM Population_new''')
    results = cur.fetchall()

    return jsonify(list(results))

@app.route('/data/<entry>')
def sampleData(entry):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM Population_new''')
    results = cur.fetchall()
    print(results)

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
