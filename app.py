import flask
import numpy as np
import pandas as pd
import pickle as pk
from flask import Flask, render_template, request

app=Flask(__name__)

def init():
    global data_encoder, random_forest_model

    print("initializing... ") 
    data_encoder = pk.load(open("models/label_encoder_map.pkl", "rb"))
    random_forest_model = pk.load(open("models/model.pkl", "rb")) 
    print("initialized") 
  
@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    # Get values from html form
    to_predict_values = request.form.to_dict()
    to_predict_values = list(to_predict_values.values())
    to_predict = np.array(to_predict_values).reshape(1,8)

    # Conver values to dataframe
    df = pd.DataFrame(to_predict, columns = ['Age','Gender','Education Level','Job Title','Years of Experience', 'Country', 'Race', 'Senior']) 
    
    # Replace values using encoder
    df.replace(data_encoder, inplace=True)

    # Rearrange order of columns
    new_column_order = ['Age','Education Level','Years of Experience','Senior','Gender','Job Title','Country','Race']
    df_reordered = df[new_column_order]

    # Need to rename columns
    column_name_mapping = {
    'Country': 'Country_Encoded',
    'Gender': 'Gender_Encoded',
    'Job Title': 'Job Title_Encoded',
    'Race': 'Race_Encoded'
    }
    df_reordered.rename(columns=column_name_mapping, inplace=True)

    # Predict salary using model
    y_pred = random_forest_model.predict(df_reordered)

    # Return value to the result.html file
    return render_template('result.html', prediction=y_pred)
 

if __name__ == '__main__':
    init()
    app.run(debug=True, port=9090)
   