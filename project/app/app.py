from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import config
import pickle


from markupsafe import Markup



crop_recommendation_model = pickle.load(
   open(crop_recommendation_model_path, 'rb'))
# with open(r'C:\Users\DELL\Desktop\other\crop-rec\project\app\models\randomforest.pkl', 'rb') as file:
#     loaded_object = pickle.load(file)
app = Flask(__name__)
@app.route('/login')
def login():
    return render_template('login.html', title='Login Page')

@app.route('/about-us')
def aboutus():
    return render_template('aboutus.html', title='About Us')

@ app.route('/')
def home():
    title = 'Harvestify - Home'
    return render_template('index.html', title=title)


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Crop Recommendation'
    return render_template('crop.html', title=title)


@ app.route('/crop-predict', methods=['GET','POST'])
def crop_prediction_result():  
    title = 'Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        Temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        data = np.array([[N, P, K, Temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]

        return render_template('crop-result.html', prediction=final_prediction, title=title)
    else:
        return render_template('try_again.html', title=title)
    
@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'Harvestify - Disease Detection'
    return render_template('Login.html', title=title)

# ... (rest of the code) ...
@ app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'Harvestify - Fertilizer Suggestion'
    return render_template('fertilizer.html', title=title)

if __name__ == '__main__':
    app.run(debug=False)

