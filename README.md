# Real-Estate-Price-Prediction Model with NLP and FastAPI
This is a sample project for price prediction of Real Estate Property. Model is trained on dataset with Property Price as the Target Variable. The model takes into account the important factors such as Sub-Area, Propert Type, Property Area in Sq. Ft, Price in lakhs, Price in Millions and Total TownShip Area in Acres and other features as ClubHouse, School/University in Township, Hospital in TownShip, Mall in TownShip, Park/Jogging track,	Swimming Pool and Gym.

## Installation
```
$ git clone https://github.com/sudhanshusinghaiml/Real-Estate-Price-Prediction-Model-with-NLP-and-FastAPI.git
$ cd Real-Estate-Price-Prediction-Model-with-NLP-and-FastAPI
$ python -m venv venv/
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```

## Tech Stack:
 - **Language**: Python
 - **Libraries**: FAST API, gunicorn, scipy, linear regression, Ridge Regression, Lasso Regression, joblib, seaborn, scikit_learn, NLTK
 - **Services:** FAST API, Deployment on Heroku Platform

## Project Approach:
 - Create the repository in github in local
 - **Application Code**
    - Flask app (app.py) is created to predict Price for Real Estate Price Prediction. It will accept the features from webpage for single property and predict the price of the property.

 - **Model Deployment**
    - runtime.txt - is used to create python images for model deployment
    - Procfile - is used for running the FAST API on Heroku Platform.
    - requirements.txt - is used to install library for deploying the models.

- Exploratory Data Analysis:

  * ***[No of Property in each sub Area](https://github.com/sudhanshusinghaiml/Real-Estate-Price-Prediction-Model-with-NLP-and-FastAPI/blob/develop/images/subArea_propertyCount.png)***
    
  ![Images No of Property in each sub Area](https://github.com/sudhanshusinghaiml/Real-Estate-Price-Prediction-Model-with-NLP-and-FastAPI/blob/develop/images/subArea_propertyCount.png)


  * ***[HousesBuildbyEachCountry](https://github.com/sudhanshusinghaiml/Real-Estate-Price-Prediction-Model-with-NLP-and-FastAPI/blob/develop/images/HousesBuildbyEachCountry.png)***
    
  ![Images HousesBuildbyEachCountry](https://github.com/sudhanshusinghaiml/Real-Estate-Price-Prediction-Model-with-NLP-and-FastAPI/blob/develop/images/HousesBuildbyEachCountry.png)

