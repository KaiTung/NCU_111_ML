import numpy as np
from numpy import random

array1 = np.arange(1,51)

random.seed(0)
array2 = random.randn(10)

print(array1.sum())
print("Min: ",array2.min())
print("Max: ",array2.max())
print("Sum: ",array2.sum())

matrix1 = np.array([3] * 25).reshape(5,5)
print(matrix1.dot(matrix1))