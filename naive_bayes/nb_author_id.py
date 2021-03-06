#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB

#Importing the module to use accurancy_score
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
def trainingNB(features_train, labels_train, features_test, labels_test):
    clf= GaussianNB()

    #Let's measure how much time takes the training
    t0=time()
    clf.fit(features_train, labels_train)
    print("training time: ",round(time()-t0,3),"s")

    t1=time()
    predictions=clf.predict(features_test)
    print("predict time: ",round(time()-t1,3),"s")

    accuracy=accuracy_score(labels_test,predictions)
    return accuracy


#########################################################

#MAIN

print(trainingNB(features_train,labels_train,features_test,labels_test))
