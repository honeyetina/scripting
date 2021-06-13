#!/usr/bin/env python3


from flask import Flask, jsonify, render_template
import datetime as dt
from scrape_mars import scrape
import pymongo
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

@app.route("/")
def home():
    '''query your Mongo database and pass the mars data into an HTML template 
    to display the data.
    Create a template HTML file called index.html that will take the mars data 
    dictionary and display all of the data in the appropriate HTML elements. 
    Use the following as a guide for what the final product should look like, 
    but feel free to create your own design.'''
    db = client.mars_db
    res = db.mars_coll.find_one()
    if res is None:
        res = scrape()
    print(res)
    return render_template("index.html", res=res)

@app.route("/scrape")
def scrape0():
    res = scrape()
    print(res)
    db = client.mars_db
    client.drop_database('mars_db')
    db = client.mars_db
    collection = db.mars_coll
    db.mars_coll.insert_one(res)
    return render_template("index.html", res=res)

if __name__ == "__main__":
    app.run(debug=True)