# ML-based tool for predicting car price
Dataset used: https://www.kaggle.com/code/mohaiminul101/car-price-prediction/data

Production-level examples with similar ML model: 
https://www.autotrader.ca/a/honda/accord%20sedan/toronto/ontario/5_55980460_on20080611094525059/?showcpo=ShowCpo&ncse=no&ursrc=pl&urp=3&urm=8&sprx=100 

- wrapped into Streamlit App
- basic logging with Loguru
- Containerized with Docker: deploy anywhere!

# Car Price Predictor 🚗

An end-to-end Machine Learning web application that predicts used car prices,
with a fully automated CI/CD pipeline deploying to AWS Elastic Beanstalk.

## Live Demo
Deployed on AWS Elastic Beanstalk via GitHub Actions CI/CD

## Features
- Predicts car price based on brand, year, fuel type, km driven, and transmission
- REST API built with Flask
- Automated testing and deployment on every push to main branch
- Machine Learning model trained on real car dataset

## Tech Stack
- **ML Model:** Scikit-learn (Linear Regression)
- **Backend:** Python, Flask
- **CI/CD:** GitHub Actions
- **Cloud:** AWS Elastic Beanstalk
- **Version Control:** Git
