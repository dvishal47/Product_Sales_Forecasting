**🛍️ Product Sales Forecasting**

**📌 Problem Statement**
In the competitive retail industry, the ability to accurately forecast product sales is critical for effective inventory management, staffing, marketing, and overall business strategy. This project develops a predictive model to estimate future product sales across multiple stores by leveraging historical sales data and important factors such as store type, location, promotions, holidays, and seasonality.

**🎯 Objective & Target Metric**

**Goal: **Build a reliable model to forecast product sales with high accuracy across various stores.

**Primary Evaluation Metric:**
Mean Absolute Percentage Error (MAPE) — chosen for its interpretability and relevance in expressing forecast errors as percentages.

**🧠 Approach & Methodology**

**1. Exploratory Data Analysis (EDA)**
   a. Examined the distribution of stores by type and region.
   b. Analyzed sales distribution and identified outliers.
   c. Explored temporal trends and seasonality in sales.
   d. Assessed the impact of promotions and holidays on sales.

**2. Hypothesis Testing**
     a. Discount Day Average Sales are higher than average sales on Non-Discount Days
     b. Holiday Average Sales are lesser than average sales on Non-Holidays
     c. Average Sales of Store Type S4 is higher and is followed by S3 , S1 ,S2.
     d. Average Sales of Region_Code R1 is higher and is followed by R3 , R2 ,R1.
     e. A higher number of orders strongly and significantly correlates with higher sales. The relationship is positive and monotonic — as order count increases, so does sales.

**3. Feature Engineering**
     a. Created temporal features such as day of week, month, holiday flags, and lagged sales.
     b. Encoded categorical variables for store type, location type, and region.
     c. Added rolling averages and previous sales metrics to capture trends.

**4. Machine Learning Modelling**
     a. Trained classical time series models: ARIMA (14.93% MAPE), SARIMAX (8.51%), Prophet (19.63%)
     b. Developed machine learning models:

  Linear Regression: 9.02% MAPE
  Random Forest Regressor: 9.44% MAPE
  XGBoost Regressor: 2.58% MAPE (best performer)

**📊 Key Insights**
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


**🚀 Deployment Summary**

The final XGBoost model (2.58% MAPE) was serialized using pickle.

A Flask API was developed for serving predictions locally.

No cloud platforms (AWS) or web-based UI (Streamlit) were used.

The API accepts feature inputs and returns forecasted sales for integration with other systems.


**Recommendations**

* **Boost Underperforming Stores and Locations**

Focus on Store Type S2 and locations L3, L4, L5 by analyzing local challenges and tailoring marketing, product assortment, and staff training to improve sales.

* **Manage High-Value Outliers**

Investigate extreme high-value sales separately to understand their causes. Use insights to target premium customers or bulk buyers while managing associated risks.

* **Expand Discount Campaigns Strategically**

Leverage the success of discount days by carefully increasing targeted promotions, focusing on products and customers that respond well without hurting profit margins.

* **Enhance Holiday Promotions**

Create holiday-specific offers and marketing to boost sales during periods when demand typically drops, using special deals or local event tie-ins.

* **Align Operations with Seasonality**

Plan inventory, staffing, and supply chain based on seasonal sales trends—ramping up for peaks and optimizing costs during slower periods.

* **Drive More Orders to Increase Sales**

Encourage higher transaction volumes through loyalty programs, upselling, and personalized experiences, as more orders strongly correlate with higher sales.


