import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)


## import ridge regressor and scalar pickle

ridge = pickle.load(open('ridge.pkl','rb'))
scalar = pickle.load(open('scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict_data", methods=['GET', 'POST'])
def predict_data():
    if request.method == 'POST':
        
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Prepare data for prediction
        new_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        new_data_scaled = scalar.transform(new_data)

        # Make prediction
        result = ridge.predict(new_data_scaled)

        # Display result in index.html
        return render_template('home.html', result=f'The predicted value is {result[0]:.2f}')

    return render_template('home.html')
        



if __name__ == '__main__':
    app.run(host="0.0.0.0")
