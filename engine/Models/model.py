from sklearn.externals import joblib
import sys
import warnings
import pandas as pd 
import numpy as np
import time

if not sys.warnoptions:
    warnings.simplefilter("ignore")

def load():
	print(time.ctime())
	print("Engine loading.....")
	classifier1 = joblib.load('final_modelLR.pkl')
	classifier2 = joblib.load('final_modelET.pkl')
	char_vec = joblib.load('char_vectorizer.pkl')
	word_vec = joblib.load('word_vectorizer.pkl')
	print("Engine loading done")
	print(time.ctime())
	return [classifier1,classifier2,char_vec,word_vec]

def Extarct_percentage(text_data,classifier1,classifier2,char_vec,word_vec):
	test_text = str(text_data)
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

def main():
	classifier1,classifier2,char_vec,word_vec = load()
	text_data = (sys.argv[1])
	output = Extarct_percentage(text_data,classifier1,classifier2,char_vec,word_vec)
	print ("The comment is {} % non_toxic and {} % toxic".format(output[0],output[1]))
	print(time.ctime())

if __name__ == '__main__':
	main()
