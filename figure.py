from sklearn import datasets
from joblib import load
import numpy as np
import json
import matplotlib.pyplot as plt
from flask import Flask, send_file, render_template
import os
import io
from flask import request, jsonify
import pandas as pd

UPLOAD_FOLDER='.'

def upload(filename):
    f = request.files['file']
    f.save(filename)
    return filename

def gen_plot(filename):
    try:
        # This will look for a file ALREADY on the server
        # with the name entered in the query parameter - called filename.
        name = request.args.get('filename') # this is the name of the query parameter
        if not name:
            return jsonify({"error": "Invalid input"}), 405
        test_data = pd.read_csv(name, index_col = False)
        test_data.plot(kind='hist').get_figure()    #Change this if you want!
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format = 'png')
        bytes_image.seek(0)
        return bytes_image
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    

def disp_plot(filename):
    plot = gen_plot(filename)
    return send_file(plot, mimetype='image/png')

def html(filename):
    try:
        # This will look for a file ALREADY on the server
        # with the name entered in the query parameter - called filename.
        name = request.args.get('filename')  # this is the name of the query parameter
        if not name:
            return jsonify({"error": "Invalid input"}), 405
        
        test_data = pd.read_csv(name, index_col= False)
        plot = test_data.plot(kind='hist').get_figure()
        plot_path = os.path.join('static', 'images', 'plot.png')    #Change this if you want!
        plot.savefig(plot_path)
        return render_template('new.html')
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

def html_hello():
    return render_template('hello_template.html')
