#Libraries for data Manipulation
import numpy as np # linear algebra
import	pandas	as	pd

import matplotlib.pyplot as plt 
import seaborn as sns
from datascience import *
# scaling
from sklearn.preprocessing import MinMaxScaler 
from sklearn.preprocessing import StandardScaler

# linear regression
from sklearn import linear_model

Pov_data = pd.read_csv("Poverty_LifeExp.csv") # quick view of columns and values Pov_data.head()
# how many columns and rows in dataframe
Pov_data.shape 
Pov_data.isnull().sum()
# are there duplicate values? format(len(Pov_data[Pov_data.duplicated()])) # standard statistical measures
Pov_data.describe(percentiles = [.25, .5, .75, .90 ,.95, .99])
plt.figure(figsize=(12,5))
plt.title("Child Mortality: Death of children under 5 years of age per 1000 live births")
ax = sns.histplot(Pov_data["child_mort"])
plt.show()