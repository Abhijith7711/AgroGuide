# AgriGuide - 
A smart guide to better farming

[Live demo](https://croprcommend.streamlit.app/)
## A Smart Crop Recommender

## Problem Statement
Choosing the right crop based on soil conditions and climate is a challenge for farmers. Traditional methods often rely on experience rather than data-driven insights, leading to inefficiencies. This project provides a machine learning-based crop recommendation system using real-time weather data to assist farmers in making better decisions.

## Methods
- Integrated real-time weather data (temperature, humidity, rainfall) via an external API.
- Performed data preprocessing, including handling missing values.
- Performed Exploratory Data Analysis (EDA) to understand data distribution and patterns, identifying key trends such as correlations between soil nutrients and crop suitability.
- Applied label encoding to categorical target variables.
- Built and trained a Random Forest Classifier using soil and climate data, achieving 99.5% accuracy.
- Developed an interactive Streamlit-based UI for easy user input and recommendations.

## Technologies Used
- **Programming:** Python
- **Machine Learning:** Scikit-learn, Random-Forest,NumPy, Pandas
- **Web Framework:** Streamlit
- **API Integration:** Requests (Weather API)


## Features
 **Real-time Weather Integration** – Fetches temperature, humidity, and rainfall.  
 **Accurate ML-Based Predictions** – Suggests the best crop based on inputs.  
 **User-Friendly Interface** – Simple web app for easy use.  
 **Fast & Efficient** – Provides instant recommendations.

## Future Enhancements
-  Improve accuracy using Deep Learning models.
-  Incorporate soil moisture data for better precision.

