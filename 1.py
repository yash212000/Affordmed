from flask import Flask, request, jsonify
import datetime
import random

app = Flask(__name__)

# Sample data for demonstration purposes
trains = [
    {
        "train_id": "T123",
        "departure_time": "2023-08-15 10:00:00",
        "seats_available": random.randint(0, 100),
        "price": random.randint(50, 200)
    },
    {
        "train_id": "T456",
        "departure_time": "2023-08-15 13:30:00",
        "seats_available": random.randint(0, 100),
        "price": random.randint(50, 200)
    },
    # ... Add more train data
]

def get_trains_within_next_12_hours():
    current_time = datetime.datetime.now()
    twelve_hours_later = current_time + datetime.timedelta(hours=12)
    
    trains_within_12_hours = []
    for train in trains:
        departure_time = datetime.datetime.strptime(train["departure_time"], "%Y-%m-%d %H:%M:%S")
        if current_time <= departure_time <= twelve_hours_later:
            trains_within_12_hours.append(train)
            
    return trains_within_12_hours

@app.route('/trains', methods=['GET'])
def get_trains():
    trains_within_12_hours = get_trains_within_next_12_hours()
    
    response = []
    for train in trains_within_12_hours:
        response.append({
            "train_id": train["train_id"],
            "departure_time": train["departure_time"],
            "seats_available": train["seats_available"],
            "price": train["price"]
        })
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
