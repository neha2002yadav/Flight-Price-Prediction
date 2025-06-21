# ✈️ Flight Price Prediction

This project focuses on predicting airline ticket prices using machine learning techniques. By analyzing key flight-related features such as airline, source, destination, number of stops, duration, and journey details, this model aims to provide accurate price predictions to help users make informed travel decisions.

---

## 📌 Table of Contents
 -  Problem Statement
 -  Dataset Description
 -  Tools & Technologies Used
 -  Data Preprocessing
 -  Exploratory Data Analysis (EDA)
 -  Model Building
 -  Model Evaluation
 -  Key Findings
 -  Future Scope
 -  How to Run


## 🎯 Problem Statement

Airline ticket prices vary widely depending on several factors, including the airline, duration, number of stops, departure time, and more. This project aims to:
- Predict flight fares based on given input features.
- Understand the underlying trends in flight pricing through data analysis.
- Help users and businesses make better decisions for travel planning or fare estimation.


## 🗂 Dataset Description

The dataset used for this project contains the following columns:
- **Airline**: The name of the airline
- **Date_of_Journey**: Journey date
- **Source**: Departure city
- **Destination**: Arrival city
- **Route**: Route of the flight
- **Dep_Time**: Departure time
- **Arrival_Time**: Arrival time
- **Duration**: Total duration of the flight
- **Total_Stops**: Number of stops
- **Additional_Info**: Miscellaneous information
- **Price**: Target variable (fare of the flight)


## 🛠 Tools & Technologies Used

- **Languages**: Python  
- **Libraries**:  
  - NumPy  
  - Pandas  
  - Matplotlib  
  - Seaborn  
  - Scikit-learn  
- **IDE**: Jupyter Notebook  
- **Version Control**: Git & GitHub  


## 🧹 Data Preprocessing

Steps performed:
- Handled missing values (especially in Route and Total_Stops)
- Extracted day, month, hour, and minute from date-time columns
- Converted categorical variables using One-Hot and Label Encoding
- Removed outliers and duplicates
- Feature engineering (flight duration in minutes, weekday/weekend categorization)


## 📊 Exploratory Data Analysis (EDA)

Some key insights:
- Prices vary significantly with the number of stops (non-stop flights are more expensive)
- Certain airlines consistently charge higher fares
- Evening and night flights tend to be cheaper than early morning flights
- Duration and total stops are directly proportional to price


## 🤖 Model Building

Models tested:
- Linear Regression
- Decision Tree Regressor
- **Random Forest Regressor** ✅ *(Best performance)*
- XGBoost Regressor


## 📈 Model Evaluation

| Model                  | R² Score | RMSE       |
|------------------------|----------|------------|
| Linear Regression      | 0.61     | Moderate   |
| Decision Tree Regressor| 0.85     | Low        |
| **Random Forest**      | **0.92** | **Very Low** |
| XGBoost                | 0.89     | Low        |

✅ **Random Forest Regressor** was selected due to its high accuracy and robustness to overfitting.


## 🔍 Key Findings

- Airline and number of stops are the most important features.
- Feature engineering significantly improves model accuracy.
- Random Forest performs best due to its ensemble approach.


## 🚀 Future Scope

- Integrate live flight data through APIs.
- Deploy model as a web or mobile app.
- Add features like weather, holidays, seat class, and booking window.
- Use advanced models like LSTM for sequential pricing prediction.



## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/neha2002yadav/Flight-Price-Prediction.git
   cd Flight-Price-Prediction
