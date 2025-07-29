## 📊 Student Performance Prediction Dashboard (Python + Streamlit)
This project analyzes and predicts student academic performance using exam scores and demographic information. The analysis includes visualizations and a machine learning model deployed through an interactive Streamlit dashboard.
## 🎯 What the Dashboard Offers
Filter students by gender, test preparation, parental education, lunch type, and group

View average scores across genders

Predict performance (High/Low) using a trained Random Forest Classifier

Interactive data table and visual insights

## 🧰 Dataset
File: StudentsPerformance.csv
Includes:

Student demographics (gender, race/ethnicity, parental education, lunch, test preparation)

Exam scores in math, reading, and writing

Preprocessing steps:

Added an average_score column

Encoded categorical variables for modeling

Removed missing/irrelevant values 

## ⚙ Technologies & Libraries Used

- **Python 3**
- **Streamlit** (for dashboard/web app)
- **pandas** (data handling)
- **matplotlib & seaborn** (data visualization)
- **scikit-learn** (for building the Random Forest model)
- **joblib** (for saving and loading the model)

## 🚀 How to Run

1. Clone or download this repository.
2. Install dependencies:
3. pip install streamlit pandas matplotlib seaborn scikit-learn joblib

## 📁 Project Structure
```
student-performance-dashboard/
├── app.py                      # Streamlit Dashboard
├── StudentsPerformance.csv     # Dataset
├── random_forest_model.joblib  # Trained ML model
├── analysis.ipynb              # Data exploration & model training
└── README.md                   # Project documentation
```
## Outcome
A user-friendly dashboard for data exploration

Machine learning model to classify students as high or low performers

Key patterns visualized for educators and analysts

