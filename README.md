# Hybrid ML Model on Apple Stock Data

This project demonstrates the creation of a hybrid machine learning model to predict the closing price of Apple stock for the next 10 days. The hybrid model combines predictions from an LSTM (Long Short-Term Memory) model and a Linear Regression model to leverage the strengths of both sequential pattern recognition and linear trend analysis.

---

## Project Overview

### Objective:
Train an LSTM model and a Linear Regression model on historical Apple stock data and combine their predictions to achieve better accuracy for forecasting the next 10 days' stock prices.

### Dataset:
The project uses the Apple stock dataset, which contains the following columns:
- **Date**: The trading date.
- **Close**: The stock’s closing price for the day.

---

## Workflow

### 1. Data Preprocessing:
- Loaded the dataset and parsed the "Date" column as datetime.
- Set the "Date" column as the index.
- Selected only the "Close" column for predictions.
- Scaled the data to the range (0, 1) using `MinMaxScaler` for normalization.

### 2. Creating Sequences:
- Split the closing prices into sequences of 60 days each for training the LSTM model. Each sequence represents the input data, and the value immediately following the sequence is the target output.

### 3. Training Models:

#### **LSTM Model**:
- Architecture:
  - Two LSTM layers with 50 units each.
  - A Dense layer for output.
- Trained using the Adam optimizer and mean squared error (MSE) loss function for 20 epochs with a batch size of 32.

#### **Linear Regression Model**:
- Created lagged features (“Lag_1”, “Lag_2”, “Lag_3”) representing the previous 3 days' closing prices.
- Trained a Linear Regression model on these features to predict the next day's closing price.

### 4. Making Predictions:

#### **LSTM Predictions**:
- Used the trained LSTM model to forecast the next 10 days by iteratively appending predictions to the input sequence.

#### **Linear Regression Predictions**:
- Used the trained Linear Regression model to predict the next 10 days by iteratively updating the lagged feature set with the latest predictions.

### 5. Hybrid Model:
- Combined the predictions from both models using weighted averaging:
  
  ```
  hybrid_predictions = (0.7 * lstm_predictions) + (0.3 * lin_predictions)
  ```
  - LSTM predictions are given a weight of 0.7.
  - Linear Regression predictions are given a weight of 0.3.

---

## Results

The hybrid model predictions, along with individual model predictions, were stored in a DataFrame and visualized as a table in a Flask web application.

### Predictions DataFrame:
| Date       | LSTM Predictions | Linear Regression Predictions | Hybrid Model Predictions |
|------------|------------------|------------------------------|--------------------------|
| 2024-01-01 | 150.50           | 151.20                       | 150.71                   |
| 2024-01-02 | 151.00           | 151.50                       | 151.15                   |
| ...        | ...              | ...                          | ...                      |

---

## Deployment

### Flask Application:
- A Flask app was created to serve the predictions as an interactive HTML table.
- The app uses a combination of HTML, CSS, and Python for the frontend and backend.

---

## Files and Structure:
```
project/
├── app.py                 # Flask app backend
├── templates/
│   └── index.html         # HTML template for displaying predictions
├── static/
│   └── style.css          # CSS for styling the table
├── lstm_model.h5          # Saved LSTM model
├── linear_model.pkl       # Saved Linear Regression model
├── predictions.csv        # Predictions DataFrame saved as CSV
└── requirements.txt       # Python package dependencies
```

---

## Installation and Usage

### Prerequisites:
- Python 3.8+

### Steps:
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open the app in your browser at `http://127.0.0.1:5000/`.

---

## Technologies Used
- **Python**: Core programming language.
- **TensorFlow**: For training the LSTM model.
- **Scikit-learn**: For training the Linear Regression model.
- **Flask**: For creating the web application.
- **HTML/CSS**: For styling and displaying predictions.

---

## Conclusion
This project highlights the benefits of combining LSTM and Linear Regression models for hybrid forecasting. By leveraging both sequential and linear patterns in the data, the hybrid model improves prediction accuracy, providing a robust solution for stock price forecasting.

---

## Future Improvements
- Explore additional features like trading volume or moving averages.
- Optimize the hybrid model weights dynamically based on validation metrics.
- Deploy the application to a cloud platform for broader access.

---

## Author
Developed by Abdul Qadir.

