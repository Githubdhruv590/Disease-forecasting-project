# Disease Forecasting using Machine Learning

## Objective

This project analyzes COVID-19 case trends and builds forecasting models
using time-series features.

## Dataset

- COVID-19 dataset (Our World in Data)
- Focused on India
- Google Mobility Dataset (used for exploratory analysis to capture behavioral movement trends)
- Note: Datasets are not included due to size limitations. Please download them separately.
## Methodology

### Data Preprocessing

-   Filtered India data
-   Handled missing values
-   Converted date column to datetime

### Feature Engineering

-   lag_1 (previous day)
-   lag_7 (previous week)
-   lag_14 (two-week lag)
-   rolling_avg (7-day average)

### Models Used

-   Linear Regression (baseline)
-   Random Forest (final model)
-   XGBoost (comparison)

## Results

| Model | MAE |
|------|-----|
| Linear Regression | ~1841 |
| Random Forest | ~19.7 |
| XGBoost | ~501 |
| Random Forest + Mobility | ~586 |

## Key Insights

-   Lag features are the strongest predictors
-   Mobility data did not improve performance
-   Random Forest captured non-linear patterns effectively

## Limitations

-   External factors not included
-   Possible overfitting due to lag features

##  How to Run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the notebook:
   notebooks/eda.ipynb   
## Conclusion
This project demonstrates that historical case trends are the most reliable predictors for disease forecasting. Lag-based features such as previous day and weekly case counts capture strong temporal dependencies in the data.

Among the models tested, Random Forest achieved the best performance, effectively modeling non-linear patterns in the time series. Additional features such as mobility data were explored to incorporate behavioral context, but they did not significantly enhance prediction accuracy in this setup.

Overall, the results highlight that simple, well-engineered temporal features can outperform more complex models or additional external data when forecasting structured time-series data.

## Note
Mobility data was included as an experimental feature to evaluate real-world behavioral impact, demonstrating a systematic approach to feature selection and model evaluation.
