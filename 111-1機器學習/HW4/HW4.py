#import package
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn import ensemble, metrics
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
import math
from numpy import random

# Read CSV
test_data = pd.read_csv("test.csv")
train_data = pd.read_csv("train.csv")
train_x = train_data[:-1]
train_y = train_data.label


rand_int = random.randint(1,1741,10)

rand_train_x = train_x.iloc[rand_int]

print(rand_train_x)
