from turtle import pd
import pandas as pd
from pandas import Series,DataFrame

attri_data1 = {'ID':['1','2','3','4','5'],
'Sex':['F','F','M','M','F'],
'Money':[1000,2000,500,300,700],
'Name':['Alice','Bob','Candy','David','Ella']}

attri_data_frame1 = DataFrame(attri_data1)
print(attri_data_frame1[attri_data_frame1['Money'] >= 500])

print('-'*40)
print(attri_data_frame1.groupby('Sex')['Money'].mean())


attri_data2 = {'ID':['3','4','7'],
'Math':[60,30,40],
'English':[80,20,30]}
attri_data_frame2 = DataFrame(attri_data2)

print('-'*40)
print(pd.merge(attri_data_frame1,attri_data_frame2))

print('-'*40)
print(pd.merge(attri_data_frame1,attri_data_frame2).mean())