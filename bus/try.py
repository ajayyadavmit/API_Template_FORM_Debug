
import pandas as pd 

value = {
    'name' : ["a", "b", "c", "d"],
    'marks' : [11, 44, 89, 98],
    'city' : ["K" , "TTKT", "MMM" ,"dkdk"]
}
print(type(value))

print(pd.DataFrame())

df = pd.DataFrame(value)
print(df)

df.to_csv('new.csv')
# print(dir(df))
# df.to_csv('new1.csv', index= 5)
print("$$$$$")
print(df.head(2))
print(df.tail(2))
print(df.describe())

df1 = pd.DataFrame(value)
print(df1)
# df1.to_csv('new4.csv', index= False)
print(df1.head(2))
print(df1.tail(1))
print(df1.describe())  # statistical analysis of data 

df1.index = ['first','2nd', '3rd', '4th']  #df1. index >> it shows the Index values in the dataframe types... 
print(df1)
df1.index = ['1st','3rd','5th','6th']
print(df1)

# print(pd.read_csv('new4.csv'))
# data1 = pd.read_csv("new4.csv")
# print(data1['name'][2])  # reading clumns in the data framew of the CSV File for OUTPUTS ... 

# data1['name'][2] = "dgood thigns"
# print(data1['name'][2])  # reading clumns in the data framew of the CSV File for OUTPUTS ... 
# print(type(data1))  # Thus you can change the values of the dataframew values here >>> Pandas.COre.Frame.DataFrame 

# a = eval(input("Enter the values "))
# print(a, type(a))
# pandas uses the numpy ,  as numpy uses the power of C languages... 
# series and data framew in the Pandas 

import numpy as np 

print(np.random.rand(34))
print(pd.Series(np.random.rand(22)))

ax = pd.Series(np.random.rand(44))
print(type(ax))

# Loc () function to set the values in the Pandas so that memory can be managed well... 

x = np.array([[3,4,56,89]])   ##no space is there in the array 
print(x[0][3])
print(x.shape)
print(x.dtype)
x[0][3] = 444
print(x)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a.size)


value1 = {
    'name' : ["a", "b", "c", "d", "e"],
    'marks' : [11, 44, 89, 98,768],
    'city' : ["K" , "TTKT", "MMM" ,"dkdk","LLL"]
}

xy = pd.DataFrame(value1)
print(xy.to_csv('try.csv'))
print(xy.head(2))
print(xy.tail(2))
print(xy.describe()) # it describes the Marks columns here with MIN Max Q! A2 q3 a4 and median values...  >> 

# Data Frame is the tool to use the CSV files.. 

l = [[3,4,5],[5,6,7],[5,47,8]]
# scalar , vector, matrix, Ndim Tensor data's here x = 3 scalar y = [4,5]

a = np.array(l)
print(a.T)
 # T stands for Transpose the data here ...  T stands for transpose the data here... 

x = 66
x1 = np.array(x)
print(a.ndim)
print(x1.ndim)
print(type(x1))

import random 

for _ in range(9):
    # print(random.randint(4,9))
    random.seed(10)
    print(random.random())

# random.seed(10) SETS the generate the random no at one time specific same values irrespceiive of gpram users.. 
# 0.5714025946899135
