import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('Flightprice.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to get travel time based on source and destination
def get_travel_time(source, destination):
    travel_times = {
        ('Banglore', 'New Delhi'): 150,  # example in minutes
        ('Banglore', 'Cochin'): 90,
        ('Banglore', 'Kolkata'): 120,
        ('Banglore', 'Delhi'): 150,
        ('Banglore', 'Hyderabad'): 60,
        ('Kolkata', 'New Delhi'): 120,
        ('Delhi', 'Cochin'): 180,
        # Add more routes as necessary
    }
    return travel_times.get((source, destination), 120)  # default 120 minutes if route not found

# Prediction function using the loaded model
def Flight_fare(input_data):
    input_data_as_numpy_Array = np.array(input_data, dtype=object)
    input_data_reshaped = input_data_as_numpy_Array.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
    return prediction

def main():
    st.title('✈️ FLIGHT PRICE PREDICTION')

    st.text("Choose your Flight Details:")

    try:
        # Airline selection
        airline = st.selectbox("Airline", [
            'IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
            'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
            'Vistara Premium economy', 'Jet Airways Business',
            'Multiple carriers Premium economy', 'Trujet'
        ])

        # Date of Journey
        Date_of_Journey = st.date_input("Date Of Journey")
        Journey_day = Date_of_Journey.day
        Journey_month = Date_of_Journey.month

        # Source and Destination
        Source = st.selectbox("Source", ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
        Destination = st.selectbox("Destination", ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])

        # Departure Time
        Dep_Time = st.time_input("Departure Time")
        Dep_hour = Dep_Time.hour
        Dep_min = Dep_Time.minute

        # Total Stops
        Total_Stops = st.selectbox("Total Stops", (0, 1, 2, 3, 4))

        # Assume arrival hour same as departure for simplicity
        Arrival_hour = Dep_hour

        # Get travel time in minutes from dictionary
        travel_time = get_travel_time(Source, Destination)

        # Prepare input features list
        input_data = [
            Total_Stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            travel_time // 60,   # Travel time hours
            travel_time % 60     # Travel time minutes
        ]

        # Map categorical values
        airline_map = {
            'IndiGo': 0, 'Air India': 1, 'Jet Airways': 2, 'SpiceJet': 3,
            'Multiple carriers': 4, 'GoAir': 5, 'Vistara': 6, 'Air Asia': 7,
            'Vistara Premium economy': 8, 'Jet Airways Business': 9,
            'Multiple carriers Premium economy': 10, 'Trujet': 11
        }

        source_map = {'Banglore': 0, 'Kolkata': 1, 'Delhi': 2, 'Chennai': 3, 'Mumbai': 4}
        destination_map = {'New Delhi': 0, 'Banglore': 1, 'Cochin': 2, 'Kolkata': 3, 'Delhi': 4, 'Hyderabad': 5}

        # Add mapped values to input
        input_data.append(airline_map[airline])
        input_data.append(source_map[Source])
        input_data.append(destination_map[Destination])

        # Predict when button is clicked
        if st.button("Predict Fare"):
            if len(input_data) == 11:
                prediction = Flight_fare(input_data)
                output = round(prediction[0], 2)
                st.success(f"Predicted Flight Fare: ₹{output}")
            else:
                st.error(f"The model expects 11 features, but {len(input_data)} were provided.")

    except Exception as e:
        st.error(f"Error: {e}")

if __name__ == "__main__":
    main()

