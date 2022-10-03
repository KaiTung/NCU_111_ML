import numpy as np
from numpy import random

random.seed(1)
m1 = random.randn(16).reshape(4,4)
print(m1)

random.seed(2)
m2 = random.randn(16).reshape(4,4)
print(m2)

print(m1*m2)
print(np.dot(m1,m2))