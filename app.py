import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'gamer-reviews'
app.config["MONGO_URI"] = 'mongodb+srv://joe:Drumgoon6894@gamerreview.85ibj.mongodb.net/gamer-reviews?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", reviews=mongo.db.reviews.find())
    
@app.route('/articles')
def articles():
    return render_template("articles.html", reviews=mongo.db.reviews.find())

@app.route('/single-article')
def single-article():
    return render_template("single-article.html", reviews=mongo.db.reviews.find())
    
@app.route()

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
