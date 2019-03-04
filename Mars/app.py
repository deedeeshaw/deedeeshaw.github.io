from flask import Flask, render_template, redirect, Response, request, url_for
from flask_pymongo import PyMongo
import scrape_mars

app= Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo=PyMongo(app, uri='mongodb://localhost:27017/mars_db')

@app.route('/')
def index():
    mars = mongo.db.mars.find()
    return render_template('index.html', mars=mars)
   

@app.route('/scrape/', methods=['GET'])
def scrape():
    
    mars_data = scrape_mars.scrape()
    mars= mongo.db.mars
    mars.update({}, mars_data, upsert=True)
    return render_template('index.html', mars=mars_data)
    

if __name__=='__main__':
    app.run(debug=True)
