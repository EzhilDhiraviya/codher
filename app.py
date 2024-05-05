from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from db_connection import get_locations_collection, get_mongo_client, get_students_from_locations_collection, get_sdats, get_records_by_sdat

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
    l= get_sdats()
    return render_template('organization.html',l=l)

@app.route('/centers')
def centers():
    l= get_sdats()
    return render_template('centers.html')

@app.route('/otp')
def otp():
    return render_template('otp.html')

@app.route('/students')
def students():
    student_records = get_records_by_sdat("Dharmapuri")
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

@app.route('/dietchart')
def dietchart():
    return render_template('dietchart.html')

@app.route('/diet')
def diet():
    return render_template('diet.html')


def load_data():
    data = pd.read_csv('athlete_health_records.csv')
    return data

def train_model(data):
    X = data.drop(['athlete_id', 'weight_change'], axis=1)
    y = data['weight_change']

    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_weight_change(model, new_data):
    prediction = model.predict(new_data)
    return prediction

@app.route('/medical')
def medical():
    data = load_data()

    model = train_model(data)

    new_data = pd.DataFrame({
        'food_intake': [2050],
        'medicine_intake': [0],
        'workout_duration': [90],
        'weight': [70]
    })
    
    prediction = predict_weight_change(model, new_data)
    
    return render_template("medical_record.html",predicted_weight=round(prediction[0],3))

@app.route('/update')
def update():
    return render_template('update.html')


@app.route('/add_stud')
def add_stud():
    return render_template('add_stud.html')

if __name__ == '__main__':
    app.run(debug=True)
