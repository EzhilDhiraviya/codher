import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('sports_person.csv')

X = data[['Food_Intake', 'Workout_Hours']]
y = data['Weight_Change']
model = LinearRegression()
model.fit(X, y)

def predict_weight_change(food_intake, workout_hours):
    prediction = model.predict([[food_intake, workout_hours]])
    return prediction[0]

def get_user_input():
    food_intake = float(input("Enter food intake (in calories): "))
    workout_hours = float(input("Enter workout hours: "))
    return food_intake, workout_hours

def main():
    food_intake, workout_hours = get_user_input()
    predicted_weight_change = predict_weight_change(food_intake, workout_hours)
    
    if predicted_weight_change > 0:
        print("Predicted weight change: Increase")
    elif predicted_weight_change < 0:
        print("Predicted weight change: Decrease")
    else:
        print("Predicted weight change: No change")

if __name__ == "__main__":
    main()


