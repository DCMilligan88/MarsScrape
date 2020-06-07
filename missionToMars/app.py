from flask import Flask, render_template, redirect, url_for
import scrape
from flask_pymongo import PyMongo

#initialize app
app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/marsdb"
mongo = PyMongo(app)

@app.route('/')
def index():

    marsdb = mongo.db.marsdb.find_one()

    return render_template("index.html", mars_info=marsdb)

@app.route('/scrape')
def marscrape():
    mars_info = scrape.scrape()

    mongo.db.marsdb.update({}, mars_info, upsert=True)
    return redirect(url_for('index'), code=302)

@app.route('/delete')
def delete_all():
    mongo.db.marsdb.remove({})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)