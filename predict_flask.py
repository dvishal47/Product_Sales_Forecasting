from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle
from datetime import datetime, timedelta

app = Flask(__name__)

# Load model and feature names
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)

# Load historical sales data
historical_df = pd.read_csv('train.csv')
historical_df['Date'] = pd.to_datetime(historical_df['Date'])

# Preprocessing function with lag features
def preprocess(df):
    df['Date'] = pd.to_datetime(df['Date'])

    # Combine with history
    df_combined = pd.concat([historical_df, df], ignore_index=True)
    df_combined = df_combined.sort_values(by=['Store_id', 'Date'])

    # Extract date features
    df_combined['Year'] = df_combined['Date'].dt.year
    df_combined['Month'] = df_combined['Date'].dt.month
    df_combined['Day'] = df_combined['Date'].dt.day
    df_combined['DayOfWeek'] = df_combined['Date'].dt.dayofweek
    df_combined['IsWeekend'] = df_combined['DayOfWeek'].isin([5, 6]).astype(int)

    # Discount conversion
    df_combined['Discount'] = df_combined['Discount'].map({'Yes': 1, 'No': 0})

    # Lag features
    df_combined['Sales_lag_1'] = df_combined.groupby('Store_id')['Sales'].shift(1)
    df_combined['Sales_lag_7'] = df_combined.groupby('Store_id')['Sales'].shift(7)
    df_combined['Sales_lag_14'] = df_combined.groupby('Store_id')['Sales'].shift(14)

    # Rolling averages
    df_combined['Sales_last_3'] = df_combined.groupby('Store_id')['Sales'].shift(1).rolling(window=3, min_periods=1).mean().reset_index(level=0, drop=True)
    df_combined['Sales_last_7'] = df_combined.groupby('Store_id')['Sales'].shift(1).rolling(window=7, min_periods=1).mean().reset_index(level=0, drop=True)

    # One-hot encode
    categorical_cols = ['Store_Type', 'Location_Type', 'Region_Code']
    df_combined = pd.get_dummies(df_combined, columns=categorical_cols, drop_first=True)

    # Filter rows to predict
    prediction_dates = df['Date'].unique()
    df_predict = df_combined[df_combined['Date'].isin(prediction_dates)]

    # Align columns with model
    for col in feature_names:
        if col not in df_predict.columns:
            df_predict[col] = 0
    df_predict = df_predict[feature_names]
    df_predict.fillna(0, inplace=True)

    return df_predict

@app.route("/")
def homepage():
    return "Welcome to Product Sales Forecasting"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Parse period from request (default 30 days)
        period = int(data.get("period", 30))
        if period <= 0 or period > 90:
            return jsonify({"error": "Forecast period must be between 1 and 90 days."}), 400

        base_date = pd.to_datetime(data['Date'])
        future_dates = [base_date + timedelta(days=i) for i in range(1, period + 1)]

        # Prepare forecast input records
        records = []
        for d in future_dates:
            record = data.copy()
            record['Date'] = d.strftime('%Y-%m-%d')
            record.pop("period", None)  # remove 'period' from input to avoid issues
            records.append(record)

        df = pd.DataFrame(records)
        df_processed = preprocess(df)

        # Predict
        preds = model.predict(df_processed)
        preds_list = [round(float(p), 2) for p in preds]
        return jsonify({f"prediction for next {period} days": preds_list})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
