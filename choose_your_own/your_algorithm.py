#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.savefig('temp.png')
plt.show()
################################################################################

### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

print "features_train: {}".format(len(features_train))
print "features_test: {}".format(len(features_test))
print "labels_train: {}".format(len(labels_train))
print "labels_test: {}".format(len(labels_test))

from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

try:
    clf = AdaBoostClassifier(n_estimators=100)
    clf = clf.fit(features_train, labels_train)
    accuracy = accuracy_score(labels_test, clf.predict(features_test))
    print "AdaBoostClassifier accuracy: {}".format(accuracy)
    prettyPicture(clf, features_test, labels_test, "adaboost_test.png")
except NameError:
    pass

try:
    clf = RandomForestClassifier()
    clf = clf.fit(features_train, labels_train)
    accuracy = accuracy_score(labels_test, clf.predict(features_test))
    print "RandomForestClassifier accuracy: {}".format(accuracy)
    prettyPicture(clf, features_test, labels_test, "randomforest_test.png")
except NameError:
    pass

try:
    clf = GradientBoostingClassifier()
    clf = clf.fit(features_train, labels_train)
    accuracy = accuracy_score(labels_test, clf.predict(features_test))
    print "GradientBoostingClassifier accuracy: {}".format(accuracy)
    prettyPicture(clf, features_test, labels_test, "gradientboosting_test.png")
except NameError:
    pass

try:
    clf = KNeighborsClassifier(n_neighbors=10)
    clf = clf.fit(features_train, labels_train)
    prettyPicture(clf, features_test, labels_test, "knn_test.png")
    print "KNeighborsClassifier accuracy: {}".format(accuracy)
    prettyPicture(clf, features_test, labels_test, "gradientboosting_test.png")
except NameError:
    pass
