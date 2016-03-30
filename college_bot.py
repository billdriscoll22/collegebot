import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Imputer

#silly stub program for neil

data = pd.read_csv('spreadsheet.csv', index_col = 0)
X = data[['gpa', 'gender', 'first_gen', 'is_urm', 'sat']]
y = data['status']
imp = Imputer()
X = imp.fit_transform(X)
log_reg_engine = LogisticRegression()
log_reg_engine.fit(X, y)
#test = [4.0, 1, 1, 1, 2400]
#print log_reg_engine.predict([test])
print "Welcome to College Bot, now with null value protection!"
gpa = raw_input("enter gpa ")
gender = raw_input("enter gender. 0 is male, 1 is female ")
first_gen = raw_input("is the student first gen? 1 if yes, 0 if no ")
urm =  raw_input("is the student urm? 1 if yes, 0 if no ")
sat = raw_input("enter sat ")
test_array = [float(gpa), float(gender), float(first_gen), float(urm), float(sat)]
prediction = log_reg_engine.predict([test_array])
prediction = prediction[0]
if prediction == 0:
  print "rejected"
elif prediction == 1:
  print "deferred"
else:
  print "accepted"
