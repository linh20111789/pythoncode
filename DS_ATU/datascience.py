#Libraries for data Manipulation
import numpy as np # linear algebra
import	pandas	as	pd

import matplotlib.pyplot as plt 
import seaborn as sns
from datascience import *

PRSA_data =pd.read_csv("PRSA.csv")

# print(PRSA_data)

# quick view of columns and values 
PRSA_data.head()
# how many columns and rows in dataframe
PRSA_data.shape 
PRSA_data.isnull().sum()
# are there duplicate values? 
format(len(PRSA_data[PRSA_data.duplicated()])) 
# standard statistical measures
standard_statistical = PRSA_data.describe(percentiles = [.25, .5, .75, .90 ,.95, .99])
# print(standard_statistical)


plt.figure(figsize=(12,5))
plt.title("todo")

ax = sns.histplot(PRSA_data["year"])
plt.show()
ax = sns.histplot(PRSA_data["month"])
plt.show()
ax = sns.histplot(PRSA_data["day"])
plt.show()
ax = sns.histplot(PRSA_data["hour"])
plt.show()
ax = sns.histplot(PRSA_data["pm2.5"])
plt.show()
ax = sns.histplot(PRSA_data["DEWP"])
plt.show()
ax = sns.histplot(PRSA_data["TEMP"])
plt.show()
ax = sns.histplot(PRSA_data["PRES"])
plt.show()
ax = sns.histplot(PRSA_data["cbwd"])
plt.show()
ax = sns.histplot(PRSA_data["Iws"])
plt.show()
ax = sns.histplot(PRSA_data["Is"])
plt.show()
ax = sns.histplot(PRSA_data["Ir"])

plt.show()





















