

# ✈️ Flight Price Prediction using Machine Learning
![Flight Price Prediction](https://github.com/sumankhatua5/Flight_Fare_Prediction/blob/main/1_kNBJQzG-tIWHGIcjv-7x4A%20(1).jpg)



This project predicts flight ticket prices using machine learning. With an accuracy of **83%** achieved using a **Random Forest Regressor**, this web-based application is designed to provide reliable fare predictions based on key features such as airline, stops, travel duration, and more.

---

## 🌟 Key Highlights

- **💡 Real-Time Price Prediction**: Get instant fare predictions based on your flight details.
- **📊 Data Processing**: Managed missing values, outliers, and engineered features for improved prediction performance.
- **🛠️ Machine Learning**: Achieved **80% accuracy** with a **Random Forest Regressor**.
- **📈 Visualizations**: Gain insights into flight pricing trends with graphical representations.
- **🌐 Streamlit Web App**: User-friendly and intuitive interface for instant predictions.

---

## 📂 Dataset

The dataset is sourced from **Kaggle**: [Flight Fare Prediction Dataset](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh). It includes the following features:

- **Airline**: Name of the airline.
- **Source**: Departure city.
- **Destination**: Arrival city.
- **Duration**: Flight duration.
- **Total_Stops**: Number of stops.
- **Price**: Target variable representing flight price.
- **Date_of_Journey**: The date of the journey, transformed into `Journey_day` and `Journey_month`.
- **Dep_time**: Split into `Dep_hour` and `Dep_min` to represent flight departure time.
- **Arrival_time**: Split into `Arrival_hour` and `Arrival_min` for flight arrival time.

---

## 🧠 Data Preprocessing

- **Null Value Handling**: Missing values were handled using imputation techniques, ensuring no information loss.
- **Outlier Detection**: Applied **IQR** to detect and remove price outliers.
- **Feature Engineering**: Key transformations included splitting date and time fields into more granular features like `Dep_hour`, `Arrival_hour`, `Journey_day`, and `Journey_month`.

---

## 🏗️ Machine Learning Model

- **Model Used**: **Random Forest Regressor** was chosen for its ability to handle complex data relationships and non-linearity.
- **Accuracy**: Achieved an impressive **80% accuracy**, indicating the model's strong predictive capability.
- **Libraries**: Utilized **Pandas** and **NumPy** for data manipulation and preparation, while **Scikit-learn** was used for model training and evaluation.

### Evaluation Metrics:
- **R² Score**: Explained variance for predicted prices.
- **Mean Absolute Error (MAE)**: Evaluated average prediction error.

---

## 📊 Visualizations

In the jupyter notebook i provides insightful visualizations to help users understand key trends:
- **Price Distribution**: Visualize how flight prices are distributed.
- **Airline Pricing**: Compare average prices across different airlines.
- **Correlation Matrix**: Explore relationships between various flight details and pricing.

---

## 🚀 Live Demo

Check out the live version of the application here:
[Live Flight Price Prediction App](https://flightpricepredictionn.streamlit.app/)

---

## 🌐 How to Use

1. **Input Details**: 
   - Choose the **Airline**, **Source**, and **Destination** cities.
   - Select the **Date of Journey** and flight **Duration**.
   - Enter the number of **Stops**.

2. **Get Predicted Price**: 
   - Based on the provided input, the app will display the **Predicted Price** for the flight.

---

## 🛠️ Technologies Used

- **Frontend**: Streamlit for building the web application.
- **Backend**: Python for data processing and machine learning.
- **Libraries**:
  - **Pandas**: For data manipulation and preprocessing.
  - **NumPy**: For numerical computations.
  - **Scikit-learn**: For model building and evaluation.
  
---

## 🏗️ Project Workflow

1. **Data Preprocessing**:
   - Null values handled using imputation.
   - Outliers identified and removed to improve data quality.
   - Features engineered from date and time fields to improve model performance.
   
2. **Model Building**:
   - **Random Forest Regressor** used for price prediction.
   - Achieved **80% accuracy** after hyperparameter tuning.

3. **Web App Development**:
   - Built using **Streamlit** for an interactive interface.
   - Deployed for easy access to flight price predictions.
## 📬 Contact

If you have any questions or feedback, reach out to me:

- **Your Name**: [Your LinkedIn](https://www.linkedin.com/in/suman-khatua-919a7b2b0/)
- **Email**: sumankhatua51@gmail.com

---

## 🌱 Future Improvements
- **Additional Features**: i will Introduce features like flight class, day of the week, or demand trends to improve predictions
 and low cost flight recomendation .
- **Deployment**: in future i will Extend the app for mobile and cloud-based accessibility.

---



