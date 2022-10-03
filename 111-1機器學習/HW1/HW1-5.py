import numpy as np
from numpy import nan as NA
import pandas as pd
import numpy.random as random
random.seed(0)
df2 = pd.DataFrame(np.random.rand(15, 6))
df2.iloc[2,0] = NA
df2.iloc[5:8,2] = NA
df2.iloc[7:9,3] = NA
df2.iloc[10,5] = NA

#drop
t1 = df2.dropna()
print(t1)
#fill0
t2 = df2.fillna(0)
print(t2)
#fill mean
t3 = df2.fillna(df2.mean())
print(t3)

