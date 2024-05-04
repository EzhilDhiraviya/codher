from flask import Flask, render_template
from db_connection import get_locations_collection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loc')
def loc():
    locations_collection = get_locations_collection()
    if locations_collection is not None:
        locations = list(locations_collection.find({}))  # Retrieve all records from the collection
        return render_template('loc.html', locations=locations)
    else:
        return "Failed to fetch data from MongoDB."

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/centers')
def centers():
    return render_template('centers.html')

if __name__ == '__main__':
    app.run(debug=True)
