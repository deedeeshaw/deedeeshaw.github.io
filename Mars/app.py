from flask import Flask, render_template, redirect, Response, request, url_for
from flask_pymongo import PyMongo
import scrape_mars

app= Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo=PyMongo(app, uri='mongodb://localhost:27017/mars_db')

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)
   

@app.route('/scrape/', methods=['GET'])
def scrape():
    mars= mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/")
    
    

if __name__=='__main__':
    app.run(debug=True)
