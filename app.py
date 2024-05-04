from flask import Flask, render_template
from db_connection import get_locations_collection,get_mongo_client,get_students_from_locations_collection
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

@app.route('/org')
def org():
    return render_template('organization.html')

@app.route('/centers')
def centers():
    return render_template('centers.html')

@app.route('/otp')
def otp():
    return render_template('otp.html')

@app.route('/students')
def students():
    student_records = get_students_from_locations_collection()
    return render_template('students.html',student_records=student_records)

@app.route('/s')
def s():
    student_records = get_students_from_locations_collection()
    return render_template('students.html', student_records=student_records)

@app.route('/dashboard')
def dashboard():
    return render_template('studentdashboard.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

if __name__ == '__main__':
    app.run(debug=True)
