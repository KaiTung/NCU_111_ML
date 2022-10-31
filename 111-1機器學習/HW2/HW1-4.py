import numpy as np
from numpy import random
import pandas as pd
from pandas import DataFrame

np.random.seed(2)
array2 = np.random.randint(2, size=100)

np.random.seed(3)
array3=np.random.normal(1000, 10, size=100)

Generated_Matrix = {
    'ID':np.arange(1,101),
    'Sex':np.where(array2==0,'F','M'),
    'Money':array3
    }

G_M = DataFrame(Generated_Matrix)

print(G_M)
print('-'*40)
print("Problem 1:")
print(G_M[G_M['Money'] == G_M['Money'].min()])

print('-'*40)
print("Problem 2:")
print(G_M[ G_M['Money'] >= 1010 ])

print('-'*40)
print("Problem 3:")
print(G_M[ G_M['Money'] >= 1010 ].sort_values('Money',ascending=False))

