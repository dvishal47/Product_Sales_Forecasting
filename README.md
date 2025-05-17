🛍️ Product Sales Forecasting
📌 Problem Statement
In the competitive retail industry, the ability to accurately forecast product sales is critical for effective inventory management, staffing, marketing, and overall business strategy. This project develops a predictive model to estimate future product sales across multiple stores by leveraging historical sales data and important factors such as store type, location, promotions, holidays, and seasonality.

🎯 Objective & Target Metric
Goal: Build a reliable model to forecast product sales with high accuracy across various stores.

Primary Evaluation Metric:
Mean Absolute Percentage Error (MAPE) — chosen for its interpretability and relevance in expressing forecast errors as percentages.

🧠 Approach & Methodology
1. Exploratory Data Analysis (EDA)
Examined the distribution of stores by type and region.

Analyzed sales distribution and identified outliers.

Explored temporal trends and seasonality in sales.

Assessed the impact of promotions and holidays on sales.

2. Hypothesis Testing
Tested if promotions lead to significant sales increases — confirmed true.

Evaluated the effect of holidays on sales — found sales often decline on holidays.

Verified if urban stores outperform rural stores — accepted.

Explored if different store types show varying sales trends — accepted.

3. Feature Engineering
Created temporal features such as day of week, month, holiday flags, and lagged sales.

Encoded categorical variables for store type, location type, and region.

Added rolling averages and previous sales metrics to capture trends.

4. Machine Learning Modelling
Trained classical time series models: ARIMA (14.93% MAPE), SARIMAX (8.51%), Prophet (19.63%)

Developed machine learning models:

Linear Regression: 9.02% MAPE

Random Forest Regressor: 9.44% MAPE

XGBoost Regressor: 2.58% MAPE (best performer)

📊 Key Insights
Store and Location Distribution:
Store Type S1 and Location Type L1 dominate, with Region R1 having the highest number of stores.

Sales Distribution:
Sales are right-skewed, mostly between ₹10,000 and ₹60,000. Extreme outliers (₹247k max) heavily influence total revenue.

Performance by Store and Location:
Store Type S4 and Location Type L2 achieve the highest average sales, while Store Type S2 and Locations L3, L4, L5 underperform.

Discount and Holiday Effects:
Sales increase on discount days but drop on holidays compared to regular days.

Sales Over Time and Order Correlation:
Sales show seasonal fluctuations without clear growth trends. There is a strong positive correlation between order count and total sales.

🚀 Deployment Summary

The final XGBoost model (2.58% MAPE) was serialized using pickle.

A Flask API was developed for serving predictions locally.

No cloud platforms (AWS) or web-based UI (Streamlit) were used.

The API accepts feature inputs and returns forecasted sales for integration with other systems.

**📌 Recommendations**

Align promotional campaigns with store types and regions exhibiting high responsiveness.

Leverage sales forecasts to optimize inventory and staffing during peak periods.

Review underperforming store types and locations for targeted operational improvements.

Monitor and manage extreme sales outliers to better anticipate inventory needs.






