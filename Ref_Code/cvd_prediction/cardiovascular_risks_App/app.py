from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
from sklearn.externals import joblib
import numpy as np
import requests
import json
import pickle
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    response = make_response(render_template("index.html"))
    return response

@app.route("/predict", methods=['POST'])
def predict():
    model = joblib.load("./model.pkl")
    if request.method == 'POST':
        int_features = [int(x) for x in request.form.values()]
        final_features = np.array(int_features).reshape(1,-1)
        prediction = model.predict(final_features)
        outpout = int(prediction[0])

    return render_template("predicted.html", prediction = outpout)


if __name__ == '__main__':
    app.run(debug=True)


