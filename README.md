# Household Electricity Consumption Prediction

## 📌 Project Overview

This project develops a **Machine Learning system to predict the monthly electricity consumption of a household in kWh** based on household characteristics, electrical appliances, usage patterns, environmental conditions, solar PV information, and previous-month electricity consumption.

The project is designed as a practical **Electrical & Electronic Engineering + Machine Learning** application. It demonstrates the complete machine learning workflow, from data preparation and exploratory analysis to model training, evaluation, interpretation, and deployment through a Python-based prediction application.

---

## 🎯 Problem Statement

Household electricity consumption depends on many factors such as:

* Household size
* House area
* Number of electrical appliances
* Air-conditioning usage
* Fan usage
* Television usage
* Cooking duration
* Water heaters
* Solar PV systems
* Temperature
* Previous-month electricity consumption

Accurately estimating monthly electricity consumption can help households and energy-related systems better understand and manage electricity demand.

The objective of this project is to develop a machine learning model that can estimate a household's **monthly electricity consumption in kWh** from these available characteristics.

---

## 🎯 Project Objectives

The main objectives are:

1. Collect and prepare household electricity consumption data.
2. Clean missing and inconsistent data.
3. Perform exploratory data analysis (EDA).
4. Engineer suitable features for machine learning.
5. Preprocess numerical and categorical features.
6. Train multiple machine learning models.
7. Compare model performance using cross-validation and test-set metrics.
8. Select the best-performing model.
9. Analyze important model features.
10. Save the trained machine learning model.
11. Develop a Python prediction application.
12. Generate a prediction report for individual households.

---

# 📊 Dataset

The dataset contains information about households, appliance ownership, appliance usage, environmental conditions, solar PV systems, and previous electricity consumption.

### Main Features

| Feature                       | Description                                    |
| ----------------------------- | ---------------------------------------------- |
| `Month`                       | Month for which consumption is predicted       |
| `Province`                    | Province of the household                      |
| `District`                    | District of the household                      |
| `Household_Type`              | Type of household                              |
| `Household_Size`              | Number of people in the household              |
| `House_Area_m2`               | House area in square metres                    |
| `Bedrooms`                    | Number of bedrooms                             |
| `AC_Units`                    | Number of air-conditioning units               |
| `Fans`                        | Number of fans                                 |
| `Refrigerators`               | Number of refrigerators                        |
| `TVs`                         | Number of televisions                          |
| `Washing_Machines`            | Number of washing machines                     |
| `Water_Heaters`               | Number of water heaters                        |
| `Computers`                   | Number of computers                            |
| `Other_High_Power_Appliances` | Number of other high-power appliances          |
| `Avg_Daily_AC_Hours`          | Average daily AC usage                         |
| `Avg_Daily_Fan_Hours`         | Average daily fan usage                        |
| `Avg_Daily_TV_Hours`          | Average daily TV usage                         |
| `Avg_Daily_Cooking_Hours`     | Average daily cooking usage                    |
| `Solar_PV`                    | Whether the household has solar PV             |
| `Solar_Capacity_kW`           | Solar PV capacity in kW                        |
| `Avg_Temperature_C`           | Average temperature in °C                      |
| `Previous_Month_kWh`          | Previous month's electricity consumption       |
| **Target**                    | Current month's electricity consumption in kWh |

### Target Variable

The machine learning model predicts:

**Monthly Household Electricity Consumption (kWh)**

---

# 🔄 Project Workflow

The complete project follows this workflow:

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Data Preprocessing
     ↓
Model Training
     ↓
Cross-Validation
     ↓
Model Evaluation
     ↓
Model Selection
     ↓
Feature Interpretation
     ↓
Save Trained Model
     ↓
Prediction Application
     ↓
Generate Prediction Report
```

---

# 🧹 1. Data Understanding and Cleaning

The first stage involved understanding the dataset structure and identifying:

* Numerical features
* Categorical features
* Missing values
* Invalid values
* Data types
* Duplicate or inconsistent records
* Relationships between variables

The cleaned dataset is stored in:

```text
data/cleaned_data.csv
```

---

# 📈 2. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the relationships between household characteristics and electricity consumption.

The analysis included:

* Distribution of electricity consumption
* Appliance usage patterns
* Household characteristics
* Temperature relationships
* Previous-month consumption relationships
* Solar PV information
* Correlation analysis
* Feature relationships with electricity consumption

Visualizations were created using **Matplotlib**.

---

# ⚙️ 3. Feature Engineering and Preprocessing

Before training the models, the dataset was prepared using appropriate preprocessing techniques.

### Numerical Features

Numerical features were processed using suitable numerical preprocessing.

Examples include:

* Household size
* House area
* Number of appliances
* Appliance usage hours
* Temperature
* Previous-month consumption

### Categorical Features

Categorical variables such as:

* Province
* District
* Household type
* Solar PV

were converted into machine-learning-compatible representations using preprocessing techniques such as **One-Hot Encoding**.

### Pipeline

Scikit-learn pipelines were used to combine preprocessing and machine learning steps.

This helps ensure that the same preprocessing procedure is applied consistently during both training and prediction.

---

# 🤖 4. Machine Learning Models

Several regression models were trained and evaluated.

The main models included:

### Ridge Regression

Ridge Regression is a regularized linear regression algorithm.

It was selected as the final model because it provided the strongest overall performance among the models in the final comparison.

### Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to produce predictions.

It can model nonlinear relationships and provides feature importance values.

### Gradient Boosting

Gradient Boosting builds models sequentially, with each new model attempting to improve the errors of the previous models.

---

# 🔬 5. Model Evaluation

The models were evaluated using:

### MAE — Mean Absolute Error

MAE measures the average absolute difference between actual and predicted electricity consumption.

```text
MAE = average(|actual - predicted|)
```

A lower MAE is better.

---

### RMSE — Root Mean Squared Error

RMSE gives more importance to larger prediction errors.

```text
RMSE = sqrt(mean((actual - predicted)²))
```

A lower RMSE is better.

---

### R² — R-Squared

R² measures how well the model explains the variation in the target variable.

A value closer to 1 indicates better performance.

---

# 🔁 6. Cross-Validation

Five-fold cross-validation was used to evaluate model performance more reliably.

The dataset was divided into five folds.

```text
Fold 1 → Validation
Fold 2 → Validation
Fold 3 → Validation
Fold 4 → Validation
Fold 5 → Validation
```

Each fold was used as the validation set once while the remaining folds were used for training.

The final cross-validation result was calculated from the performance across the folds.

---

# 🏆 7. Final Model Comparison

The final model comparison produced the following results:

| Model                |    CV MAE |  Test MAE | Test RMSE |    Test R² |
| -------------------- | --------: | --------: | --------: | ---------: |
| **Ridge Regression** | **23.78** | **24.26** | **29.68** | **0.8848** |
| Random Forest        |     29.99 |     29.69 |     37.19 |     0.8190 |
| Gradient Boosting    |     28.18 |     27.99 |     35.48 |     0.8353 |

---

# 🥇 Best Model: Ridge Regression

Based on the final evaluation results, **Ridge Regression was selected as the best-performing model**.

### Ridge Regression Results

```text
Cross-Validation MAE : 23.78 kWh

Test MAE             : 24.26 kWh

Test RMSE            : 29.68 kWh

Test R²              : 0.8848
```

The R² value of approximately **0.885** indicates that the model explains about **88.5% of the variation** in monthly household electricity consumption on the test data.

The average absolute prediction error is approximately **24.26 kWh**.

---

# 🔍 8. Feature Interpretation

Feature interpretation was performed to understand which variables have strong relationships with electricity consumption.

Important variables identified during model analysis included factors such as:

* Previous-month electricity consumption
* Average daily AC usage
* Number of AC units
* Household size
* Solar PV capacity
* Number of fans
* Water heaters
* Other high-power appliances
* House area
* Average temperature

These results are useful because they provide insight into the factors that influence household electricity consumption.

### Random Forest Feature Importance

One important observation from the Random Forest analysis was that:

```text
Previous_Month_kWh
```

had a substantially larger feature importance than the other features.

This indicates that previous-month consumption provides strong predictive information for estimating the current month's consumption.

---

# 💾 9. Trained Model

The final trained model was saved using **Joblib**.

The saved model is located at:

```text
models/electricity_model.pkl
```

This allows the trained model to be reused without retraining it every time a prediction is required.

---

# 🖥️ 10. Prediction Application

A Python command-line prediction application was developed using:

```text
src/predict.py
```

The application collects household information from the user and uses the trained machine learning model to predict monthly electricity consumption.

The application accepts information such as:

* Month
* District
* Household type
* Household size
* House area
* Bedrooms
* Number of appliances
* Appliance usage hours
* Solar PV information
* Solar capacity
* Average temperature
* Previous-month electricity consumption

The entered information is converted into the same feature structure used during model training.

The trained model then generates the predicted monthly electricity consumption.

---

# 📋 11. Prediction Output

The application provides:

```text
Predicted Monthly Electricity Consumption
```

in:

```text
kWh/month
```

It also categorizes the predicted consumption into:

```text
Low
Moderate
High
```

A prediction report is generated and stored in the project's `reports` directory.

---

# 🧪 12. Example Prediction

An example test of the application produced:

```text
Previous Month Consumption : 390 kWh

Predicted Consumption     : 430.18 kWh/month

Usage Level               : High
```

The application successfully generated a report for the prediction.

---

# 📁 13. Project Structure

```text
PROJECT_/
│
├── data/
│   └── cleaned_data.csv
│
├── models/
│   └── electricity_model.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   └── 06_model_interpretation.ipynb
│
├── src/
│   └── predict.py
│
├── reports/
│   └── prediction reports
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ 14. Technologies Used

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib

### Machine Learning

* Scikit-learn

### Model Saving

* Joblib

### Development Environment

* Jupyter Notebook
* Python
* VS Code

---

# 📦 15. Installation

Clone or download the project and open the project directory.

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
pandas
numpy
matplotlib
scikit-learn
joblib
```

---

# ▶️ 16. How to Run the Project

## Step 1 — Open the project

Open the `PROJECT_` folder in VS Code or another Python development environment.

---

## Step 2 — Install dependencies

Run:

```bash
pip install -r requirements.txt
```

---

## Step 3 — Explore the notebooks

The notebooks should be executed in the following order:

```text
01_data_understanding.ipynb
        ↓
02_data_cleaning.ipynb
        ↓
03_eda.ipynb
        ↓
04_feature_engineering.ipynb
        ↓
05_model_training.ipynb
        ↓
06_model_interpretation.ipynb
```

---

## Step 4 — Run the prediction application

From the project root directory:

```bash
python src/predict.py
```

The application will ask for the required household information.

After entering the information, the trained model will generate the predicted monthly electricity consumption.

---

# 📊 17. Key Results

The final machine learning system achieved:

| Metric               |               Result |
| -------------------- | -------------------: |
| Best Model           | **Ridge Regression** |
| Cross-Validation MAE |        **23.78 kWh** |
| Test MAE             |        **24.26 kWh** |
| Test RMSE            |        **29.68 kWh** |
| Test R²              |           **0.8848** |

### Main Finding

The model achieved an R² of approximately **88.5%**, indicating strong predictive performance on the test dataset.

The results also show that previous-month electricity consumption is a particularly useful predictor of current monthly consumption.

---

# 💡 18. Engineering Relevance

This project combines **Electrical & Electronic Engineering** with **Machine Learning**.

Potential applications include:

* Household energy monitoring
* Electricity demand estimation
* Energy management
* Energy-efficiency analysis
* Residential load forecasting
* Smart energy systems
* Solar PV planning
* Electricity consumption analysis

The project demonstrates how machine learning can be applied to an engineering problem involving electrical energy consumption.

---

# 🚀 19. Future Improvements

Possible future improvements include:

### 1. Larger Dataset

Use a larger real-world household electricity dataset to improve generalization.

### 2. Time-Series Features

Include additional temporal information such as:

* Previous 2–3 months consumption
* Seasonal patterns
* Yearly trends
* Rolling averages

### 3. Advanced Models

Future versions could investigate:

* XGBoost
* LightGBM
* Random Forest optimization
* Gradient Boosting optimization
* Neural Networks

### 4. Hyperparameter Optimization

Techniques such as:

```text
GridSearchCV
RandomizedSearchCV
```

could be used to optimize model parameters.

### 5. Web Application

The prediction system could be converted into a web application using technologies such as:

```text
Streamlit
Flask
FastAPI
```

### 6. Real-Time Data

Future versions could integrate smart-meter or IoT data for continuous electricity monitoring and prediction.

### 7. Explainable AI

Methods such as SHAP could be added to provide more detailed explanations of individual predictions.

---

# 👨‍💻 Author

**Electrical & Electronic Engineering Undergraduate**

This project was developed as a practical Machine Learning and Engineering project to demonstrate skills in:

* Python Programming
* Data Analysis
* Data Visualization
* Machine Learning
* Scikit-learn
* Feature Engineering
* Model Evaluation
* Model Interpretation
* Engineering Problem Solving

---

# 📌 Project Status

```text
✅ Data Collection
✅ Data Cleaning
✅ Exploratory Data Analysis
✅ Feature Engineering
✅ Model Training
✅ Cross-Validation
✅ Model Evaluation
✅ Model Selection
✅ Feature Interpretation
✅ Model Saving
✅ Prediction Application
✅ Application Testing
✅ Project Organization
✅ requirements.txt
✅ README.md

⏳ GitHub Upload
⏳ LinkedIn Presentation
```

---

## ⭐ Conclusion

This project successfully developed a machine learning-based system for predicting monthly household electricity consumption.

Among the evaluated models, **Ridge Regression achieved the best overall performance**, with a test MAE of approximately **24.26 kWh**, RMSE of approximately **29.68 kWh**, and R² of approximately **0.8848**.

The project demonstrates a complete end-to-end machine learning workflow and applies machine learning techniques to a practical electrical engineering problem.


