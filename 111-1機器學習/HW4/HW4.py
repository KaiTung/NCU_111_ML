#import package
# from select import KQ_FILTER_PROC
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import KFold
from sklearn import ensemble, metrics
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
import math
from numpy import random

# Read CSV
testset = pd.read_csv("test.csv")
dataset = pd.read_csv("train.csv")

dataset = shuffle(dataset)
label = dataset.label
dataset = dataset[:-1]

#svm
#Import library
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from numpy import random

def print_acc(expected,predicted):
    print(metrics.classification_report(expected,predicted))
    print(metrics.confusion_matrix(expected, predicted))
    accuracy = accuracy_score(expected, predicted)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))

    # print("Average = macro")
    print('precision:',metrics.precision_score(expected, predicted,average='macro')) 
    print('recall:',metrics.recall_score(expected, predicted,average='macro'))
    print('F1-score:',metrics.f1_score(expected, predicted,average='macro'))

#10-fold cross-validation
kfold = KFold(10)
predicted = []
expected = []
svm = OneVsRestClassifier(SVC(gamma='scale'))
#Train model
for train,valid in kfold.split(dataset):
    X_train = dataset.iloc[train]
    Y_train = label.iloc[train]

    X_valid = dataset.iloc[valid]
    Y_valid = label.iloc[valid]

    svm.fit(X_train,Y_train)
    expected.extend(Y_valid)
    predicted.extend(svm.predict(X_valid))

# test
rand_int = random.randint(0,1741,10) # 0~1741 選10筆

X_test = dataset.iloc[rand_int]
Y_test = label.iloc[rand_int]

SVM_expected_test = Y_test
SVM_predicted_test = svm.predict(X_test)
print("SVM_expected_test = {}".format(SVM_expected_test.values))
print("SVM_predicted_test = {}".format(SVM_predicted_test))

print_acc(SVM_expected_test,SVM_predicted_test)

#ramdom forest
#Import library
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from numpy import random

#10-fold cross-validation
kfold = KFold(10)
predicted = []
expected = []
forest = RandomForestClassifier(n_estimators = 100)
#Train model
for train,valid in kfold.split(dataset):
    X_train = dataset.iloc[train]
    Y_train = label.iloc[train]

    X_valid = dataset.iloc[valid]
    Y_valid = label.iloc[valid]

    forest.fit(X_train,Y_train)
    expected.extend(Y_valid)
    predicted.extend(forest.predict(X_valid))

# test
rand_int = random.randint(0,1741,10) # 0~1741 選10筆

X_test = dataset.iloc[rand_int]
Y_test = label.iloc[rand_int]

forest_expected_test = Y_test
forest_predicted_test = forest.predict(X_test)

print_acc(forest_expected_test,forest_predicted_test)







