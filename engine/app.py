from flask import Flask, redirect,render_template, url_for, request,jsonify
from sklearn.externals import joblib
import sys
import warnings
import pandas as pd 
import numpy as np
import time
import os
from flask_mail import Mail, Message
from nltk.corpus import wordnet
import data_preprocess as dp 
import math


app = Flask(__name__)


if not sys.warnoptions:
    warnings.simplefilter("ignore")

def load():
	print('Engine loading start.')
	print(time.ctime())
	classifier1 = joblib.load('Models/final_modelET.pkl')
	classifier2 = joblib.load('Models/final_modelLR.pkl')
	char_vec = joblib.load('Models/char_vectorizer.pkl')
	word_vec = 	joblib.load('Models/word_vectorizer.pkl')
	print('Engine loading done.')
	print(time.ctime())
	return [classifier1,classifier2,char_vec,word_vec]

def Extarct_percentage(test,classifier1,classifier2,char_vec,word_vec):
	test_text = dp.process(test);
	test_word_features = word_vec.transform([test_text]).toarray()
	test_char_features = char_vec.transform([test_text]).toarray()

	test_features = np.hstack([test_char_features, test_word_features])
	test_predicted1 = classifier2.predict_proba(test_features)
	test_predicted2 = classifier1.predict_proba(test_features)  
	ans = (test_predicted1 + test_predicted2)/2
	toxic,not_toxic = ans.item(0),ans.item(1)
	val = list()
	val.append(toxic);
	val.append(not_toxic);
	return val

classifier1,classifier2,char_vec,word_vec = load()


@app.route('/')
def index():
	return render_template('test.html')
   
@app.route('/contact',methods=['GET','POST'])
def contact():
	name = request.form.get("name")
	print(name)


@app.route('/process', methods=['POST'])
def process():
	test = request.form['name']
	if test:
		output = Extarct_percentage(test,classifier1,classifier2,char_vec,word_vec)
		toxic_val =  output[1] * 100;
		toxic_val = round(toxic_val,3);
		ans = str(toxic_val) + " %"
		return jsonify({
			'toxic' : ans
			})
	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug = True)









