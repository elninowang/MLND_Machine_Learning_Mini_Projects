#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy as np


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
max_salary = np.amax(data[:,0])
print "max_salary = %d"%max_salary
for k,v in data_dict.items():
    if v["salary"] == max_salary:
        print "the max salary person is %s -- %s"%(k,v["salary"])

## remove the TOTAL
data_dict.pop("TOTAL", 0)
data = featureFormat(data_dict, features)

for k,v in data_dict.items():
    if v["salary"] == 'NaN' or v["bonus"] == 'NaN':
        continue
    if v["salary"] > 1000000 and v["bonus"] > 5000000:
        print "the 2 max salary abd bonus is %s -- %s,%s"%(k,v["salary"],v["bonus"])

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
