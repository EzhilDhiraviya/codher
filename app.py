
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from db_connection import get_locations_collection, get_mongo_client, get_students_from_locations_collection


app = Flask(__name__)
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

@app.route('/dietchart')
def dietchart():
    return render_template('dietchart.html')

@app.route('/diet')
def diet():
    return render_template('diet.html')


from flask import render_template, request

@app.route('/ml', methods=['POST'])
def ml():
    try:
        # Load data and train model
        data = load_data()
        model = train_model(data)
        
        # Get input data from request
        json_data = request.json
        new_data = pd.DataFrame(json_data)

        # Make prediction
        prediction = predict_weight_change(model, new_data)

        return render_template('ml.html', predicted_weight=prediction[0]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
