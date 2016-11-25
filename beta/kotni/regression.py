# from __future__ import print_function
import pandas as pd
from sklearn import datasets, linear_model
import glob
import re
from os.path import basename

import logging
from optparse import OptionParser
import sys
from time import time
# import matplotlib.pyplot as plt
import logging
import numpy as np
from optparse import OptionParser
import sys
from time import time

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.extmath import density
from sklearn import metrics



# def benchmark(clf):
#     print('_' * 80)
#     print("Training: ")
#     print(clf)
#     t0 = time()
#     clf.fit(X_train, y_train)
#     train_time = time() - t0
#     print("train time: %0.3fs" % train_time)

#     t0 = time()
#     pred = clf.predict(X_test)
#     test_time = time() - t0
#     print("test time:  %0.3fs" % test_time)

#     score = metrics.accuracy_score(y_test, pred)
#     print("accuracy:   %0.3f" % score)

#     if hasattr(clf, 'coef_'):
#         print("dimensionality: %d" % clf.coef_.shape[1])
#         print("density: %f" % density(clf.coef_))

#     clf_descr = str(clf).split('(')[0]
#     return clf_descr, score, train_time, test_time


df1  = pd.read_csv('final_simulations/vajjala_final_train.csv')
df2  = pd.read_csv('final_simulations/vajjala_final_test.csv')


# train_labels = df1['class_y']
y_train = df1['class_y']
X_train = df1.drop('class_y',1)
y_test = df2['class_y']
X_test = df2.drop('class_y',1)
regr = linear_model.LinearRegression()
# benchmark(regr)
model = regr.fit(X_train,y_train)
results = model.predict(X_test)
# print results
accuracy = 0
for i in range(0,len(results)):
    results[i] = int(round(results[i]))
    if (int(results[i]) == y_test[i]):
        accuracy += 1

print 1.0*accuracy/len(y_test)