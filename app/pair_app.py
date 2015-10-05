"""
This program creates a Flask application. The Flask application renders
the recommender web application. The index.html is the home where the user
inputs a query. The results are posted on the results.html.

File(s) used: None
Database(s) uses: None
Created: September 30th, 2015
Creator: Rohit Deshpande
"""


import pandas as pd
from model import recommend_model as reco

from flask import Flask, request, render_template
app = Flask(__name__)


# home page
@app.route('/')
def home():
    return render_template('index.html')

# Recommendation page
@app.route('/predict', methods=['POST'])
def predict():
    user_input = str(request.form['user_input'])
    recommend = reco(user_input)

    return render_template('results.html', result=recommend)


# Notes page
@app.route('/notes')
def notes():
    return render_template('notes.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)