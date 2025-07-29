import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# File paths
DATA_PATH = r'C:\Users\user\Desktop\student performance project\StudentsPerformance.csv'
MODEL_PATH = r'C:\Users\user\Desktop\student performance project\random_forest_model.joblib'

# Load data and model
df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

# Calculate average score
if 'average_score' not in df.columns:
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

st.title("Student Performance Dashboard")

# Sidebar filters
st.sidebar.header("Filter Students")
gender = st.sidebar.selectbox("Gender", options=['All'] + sorted(df['gender'].unique()))
test_prep = st.sidebar.selectbox("Test Preparation Course", options=['All'] + sorted(df['test preparation course'].unique()))
group = st.sidebar.selectbox("Race/Ethnicity", options=['All'] + sorted(df['race/ethnicity'].unique()))
lunch_filter = st.sidebar.selectbox("Lunch", options=['All'] + sorted(df['lunch'].unique()))
parental_edu = st.sidebar.selectbox("Parental Level of Education", options=['All'] + sorted(df['parental level of education'].unique()))

# Apply filters
filtered_data = df.copy()
if gender != 'All':
    filtered_data = filtered_data[filtered_data['gender'] == gender]
if test_prep != 'All':
    filtered_data = filtered_data[filtered_data['test preparation course'] == test_prep]
if group != 'All':
    filtered_data = filtered_data[filtered_data['race/ethnicity'] == group]
if lunch_filter != 'All':
    filtered_data = filtered_data[filtered_data['lunch'] == lunch_filter]
if parental_edu != 'All':
    filtered_data = filtered_data[filtered_data['parental level of education'] == parental_edu]

st.subheader(f"Showing {filtered_data.shape[0]} students")
st.dataframe(filtered_data)

# Visualization
st.subheader("Average Scores by Gender")
fig, ax = plt.subplots()
sns.boxplot(data=filtered_data, x='gender', y='average_score', ax=ax)
st.pyplot(fig)
st.subheader("Gender Distribution")
gender_counts = filtered_data['gender'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
st.pyplot(fig1)


# Prediction
st.subheader("Predict Student Performance")

math_score = st.number_input('Math Score', min_value=0, max_value=100, value=50)
reading_score = st.number_input('Reading Score', min_value=0, max_value=100, value=50)
writing_score = st.number_input('Writing Score', min_value=0, max_value=100, value=50)
lunch = st.selectbox('Lunch', options=sorted(df['lunch'].unique()))
test_prep_course = st.selectbox('Test Preparation Course', options=sorted(df['test preparation course'].unique()))
gender_input = st.selectbox('Gender', options=sorted(df['gender'].unique()))
parental_education = st.selectbox('Parental Level of Education', options=sorted(df['parental level of education'].unique()))
ethnicity = st.selectbox('Race/Ethnicity', options=sorted(df['race/ethnicity'].unique()))

if st.button('Predict Performance'):
    # Manual encoding (should match training phase)
    gender_enc = 0 if gender_input == 'female' else 1
    lunch_enc = 0 if lunch == 'standard' else 1
    test_prep_enc = 0 if test_prep_course == 'none' else 1
    parental_education_enc = list(df['parental level of education'].unique()).index(parental_education)
    ethnicity_enc = list(df['race/ethnicity'].unique()).index(ethnicity)

    # Create input DataFrame
    input_df = pd.DataFrame({
        'gender': [gender_enc],
        'race/ethnicity': [ethnicity_enc],
        'parental level of education': [parental_education_enc],
        'lunch': [lunch_enc],
        'test preparation course': [test_prep_enc],
        'math score': [math_score],
        'reading score': [reading_score],
        'writing score': [writing_score]
    })

    # Add average score
    input_df['average_score'] = input_df[['math score', 'reading score', 'writing score']].mean(axis=1)

    # Predict
    prediction = model.predict(input_df)
    result = 'High Performer' if prediction[0] == 0 else 'Low Performer'
    st.success(f"🎯 Predicted Performance: **{result}**")
