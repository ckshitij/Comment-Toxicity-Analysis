
import joblib
import os
import numpy as np
import sys

inp = sys.argv[1]

#os.system('touch commentinput.txt')
#fs = open('commentinput.txt','r+')
#inp = fs.readline()
#print(inp)
df = joblib.load('finalized_model.pkl')
#string = 'Thanks for you contribution, you did a great job!'
string = str(inp)
ans = df.predict([string])
final = bool(ans)

#open('commentinput.txt', 'w').close()
if(final == False):
	print("Not Toxic")
else :
	print("Toxic")
#print(final)
#print('tr')
