from sklearn import datasets
from joblib import load
import numpy as np
import json

from flask import request, jsonify
import pandas as pd
UPLOAD_FOLDER='.'

#This will return a string with information about this model
def model_info():
    return 'We are using a Random Forest classifier to predict our result!'

#This will allow a file to be uploaded (it is used in file_predict)
def upload(file_key):
    if file_key not in request.files:
        raise KeyError(f"File key '{file_key}' not found in request.files")
    f = request.files[file_key]
    filename = f.filename
    filepath = f"{UPLOAD_FOLDER}/{filename}"
    f.save(filepath)
    return filepath

#This function will load a model in the app directory, read in the csv
#test data provided by the upload and return a jsonified list of 
#predictions from the test data set given.
def file_predict():
    try:
        #filename = request.args.get('filename')
        #if not filename:
        #    return jsonify({"error": "Invalid input"}), 405

        my_model = load('random_forest_model_with_pipe(2).pkl')
        name = upload('file') #this is the name of the object in the request body
        test_data = pd.read_csv(name, index_col = False)
        test_np = test_data.to_numpy()
        pred = my_model.predict(test_np)
        pred_list = pred.tolist()
        json_str = json.dumps(pred_list)
        return json_str
    except KeyError as e:
        return jsonify({"error": str(e)}), 400

def model_accuracy():
    try:
        #filename_x = request.args.get('filename_x')
        #filename_y = request.args.get('filename_y')
        
        #if not filename_x or not filename_y:
        #    return jsonify({"error": "Invalid input"}), 405
        
        name_x = upload('file_x') #this is the name of the object in the request body
        name_y = upload('file_y') #this is the name of the object in the request body
        
        my_model = load('random_forest_model_with_pipe(2).pkl')
        x_test = pd.read_csv(name_x, index_col= False)
        x_test_np = x_test.to_numpy()
        y_test = pd.read_csv(name_y, index_col= False)
        y_test_np = y_test.to_numpy()
        
        accuracy = my_model.score(x_test_np, y_test_np)

        return jsonify({"accuracy": accuracy}), 200
    
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
