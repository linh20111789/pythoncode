# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 20:59:58 2021

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt
from rplidar import RPLidar
from sklearn.cluster import DBSCAN
import pandas as pd

from sklearn import linear_model
from sklearn.model_selection import train_test_split

# ============================================
aaa=np.load('record_scans.py.npy',allow_pickle=True)
# print("aaa \n",aaa)


x = []
y = []
data=[]
data_1=[]
for i in range(len(aaa)):
    for ii in range(len(aaa[i])):
        point=aaa[i][ii]
        x.append(point[2]*np.sin(point[1]*3.14/180))
        y.append(point[2]*np.cos(point[1]*3.14/180))
for i in range(len(x)):
    data.append([x[i],y[i]])
    if ((x[i]*x[i]+y[i]*y[i])<1500000):
        data_1.append([x[i],y[i]])
myarray=np.asarray(data)
data=myarray.reshape(len(data),2)
myarray_1=np.asarray(data_1)

# print("myarray_1 \n",myarray_1)


data_1=myarray_1.reshape(len(data_1),2)
# print("x \n",x)
# print("y \n",y)
# print("data_1 \n",data_1)

plt.figure("data below threshold 1500000", figsize=(30., 30.))
plt.plot(data_1[:,0],data_1[:,1], marker='o', label='Input points', color='#008000', linestyle='None', alpha=0.8)
#plt.scatter(x, y)



# print("data_1[:,0] \n",data_1[:,0])
# print("data_1[:,1] \n",data_1[:,1])
# print("len(data_1) \n",len(data_1))
# X = data_1[:,0].reshape(len(data_1),1)
# y = data_1[:,1].reshape(-1)

# print("X \n",X)
# print("y \n",y)

X_train, X_test, y_train, y_test = train_test_split(data_1[:,0], data_1[:,1].reshape(-1), test_size=0.2, random_state=0)

# Robustly fit linear model with RANSAC algorithm
ransac = linear_model.RANSACRegressor()
ransac.fit(X_train, y_train)




# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
print("line_X \n",line_X)

line_y_ransac = ransac.predict(line_X)
print("line_y_ransac \n",line_y_ransac)

plt.plot(
    line_X,
    line_y_ransac,
    color="cornflowerblue",
    linewidth=2,
    label="RANSAC regressor",
)




plt.show()

