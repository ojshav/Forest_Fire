## Fire Weather Index (FWI) Prediction App 🌄🔥
A Machine Learning-powered web application to predict the Fire Weather Index (FWI), an essential metric for assessing wildfire risks. This tool can help 
decision-makers and responders take preventive action by estimating FWI based on input parameters like temperature, humidity, and wind speed. 
This application is designed for cloud deployment, making it accessible for real-time wildfire risk prediction.

![image](https://github.com/user-attachments/assets/22a7d17f-b565-49a1-9833-6f9cd1e9ea5c)

## 🚀 Features
- Interactive Web Form: Users can input key meteorological data to get FWI predictions.
- Machine Learning Pipeline: Built with a pre-trained Ridge regression model for accurate FWI predictions.
- Scalable & Deployable: Ready for deployment on cloud platforms like AWS, Google Cloud, or Heroku.

## Project Structure
```
.
├── app.py               # Flask application and prediction logic
├── ridge.pkl            # Pre-trained Ridge regression model
├── scaler.pkl           # StandardScaler for data normalization
├── templates/
│   └── index.html       # HTML template for the app's frontend
├── static/              # Static resources (CSS, JS, images)
├── README.md            # Project overview and setup instructions
└── requirements.txt     # Python dependencies
```


## ⚙️ Installation
Clone the repository:

`
git clone https://github.com/username/fwi-prediction-app.git
cd fwi-prediction-app
`
Install dependencies:
`
pip install -r requirements.txt
`

Run the app:
`
python app.py
`
Access the application at http://127.0.0.1:5000 in your web browser.




## 🖥️ Usage
Open the app in your browser and input the following values:

- Temperature: Atmospheric temperature in °C
- RH: Relative Humidity in %
- Ws: Wind Speed in km/h
- Rain: Rainfall in mm
- FFMC: Fine Fuel Moisture Code
- DMC: Duff Moisture Code
- ISI: Initial Spread Index
- Classes: Class indicator for categorizing inputs
- Region: Region identifier
Click Predict to get the FWI value, which will appear on the same page.

## 📈 Model Pipeline
- Data Scaling: Uses StandardScaler (stored as scaler.pkl) to normalize input data.
- Prediction: A pre-trained Ridge regression model (ridge.pkl) for generating FWI predictions.

