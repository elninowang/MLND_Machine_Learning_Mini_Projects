#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

from sklearn import svm
from sklearn.metrics import accuracy_score

#Cs = [1.0, 10.0, 100., 1000., 10000.]
Cs = [10000.]

for c in Cs:
    t0 = time()
    #clf = svm.SVC(kernel="linear")
    clf = svm.SVC(kernel="rbf", C=c)
    clf_model = clf.fit(features_train, labels_train)
    print "C={} training time: {}s".format(c, round(time()-t0, 3))
    t1 = time()
    lables_pred = clf_model.predict(features_test)
    print "C={} predicting time: {}s".format(c, round(time()-t1, 3))

    accuracy = accuracy_score(labels_test, lables_pred)
    print("C={} accuracy: {}".format(c, accuracy))
    
    checks = [10,26,50]
    for check in checks:
        print("test: {}: {}".format(check, labels_test[check]))
        print("pred: {}: {}".format(check, lables_pred[check]))

    sum_0 = 0
    sum_1 = 0
    for r in lables_pred:
        if r == 0: sum_0 += 1
        elif r == 1: sum_1 += 1

    print("sum (0,1) = ({},{})".format(sum_0, sum_1))

#########################################################


