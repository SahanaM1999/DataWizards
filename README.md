# Pulmonary Fibrosis Progression Predictor Application

# Application overview
Pulmonary Fibrosis is a lung disease that is caused by scarring of tissues in the lungs.Over time,the scar tissue can destroy the normal lungs and make it hard for oxygen to get into blood.It is difficult for clinicians to predict the prognosis of the disease even with the help of CT Scans.This application provides a way to assist doctors by providing the prediction of the disease's prognosis so that the doctors can plan optimal treatment options.

# Application Objective 
To develop a deep learning model to predict a patient's severity of decline in lung function based on the CT scan of lungs,patient's clinical information and a parameter called Forced Vital Capacity(FVC) which is the amount of air that can be forcibly exhaled from lungs after taken the deepest breath possible, as measured by spirometry.It can help doctors assess the progression of lung disease and evaluate the effectiveness of treatment.

# Software requirements
1. Python Integrated Development Environment (IDE) - Spyder/PyCharm/Google Colaboratory
2. Data Science libraris - pandas,numpy,tensorflow,sklearn,XGBoost
3. Image processing libraries - pillow,pydicom 

# Steps to run the application
1. Unzip the project folder to your local machine
2. Install all the necessary python libraries
3. Run app.py 

# Training models and error analysis file
Ensemble of Convoluional neural networks and XGBoost model - cnn_xgb_pulmonaryfibrosis.ipynb

# Information regarding the files and folders
1. app.py - integrates the backend models to the frontend web application which accepts data from the user and provides report.
2. templates/ - This folder contains all the .html files required for the website.
3. static/ - This folder contains all the css,js and bootstrap template files
4. cnn_new.h5,reg_model.pkl - saved deep learning and machine learning models.
5. fvc_ranges.txt - This file displays the normal FVC values based on age and gender.




