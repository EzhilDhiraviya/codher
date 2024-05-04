import pandas as pd
from sklearn.linear_model import LinearRegression

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

def main():
   
    data = load_data()

    model = train_model(data)

    new_data = pd.DataFrame({
        'food_intake': [2050],
        'medicine_intake': [0],
        'workout_duration': [90],
        'weight': [70]
    })
    
   
    prediction = predict_weight_change(model, new_data)
    
    print("Predicted weight change:", prediction)

if __name__ == "__main__":
    main()
