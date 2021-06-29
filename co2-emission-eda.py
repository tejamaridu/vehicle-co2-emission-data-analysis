#!/usr/bin/env python
# coding: utf-8

# # DAB103_Project01_Group07
# 
# ## Source link -
# https://www.kaggle.com/debajyotipodder/co2-emission-by-vehicles?select=CO2+Emissions_Canada.csv

# # **Importing Libraries**

# In[1]:

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


# # **Changing Directory and importing dataset**

# In[2]:

path = 'D:\WorkSpace\DAB103\Project01\'
os.chdir(path)

Co2_Emissions_Data = pd.read_csv("CO2_Emissions_Canada.csv")


# # **The Shape of the dataset is as follow**

# In[3]:

Co2_Emissions_Data.shape


# 
# The imported dataset has 7385 Rows and 12 Columns.

# # **We are viewing the first few rows of dataset**

# In[5]:

Co2_Emissions_Data.head()


# # **Column names and their data types**

# In[4]:


Co2_Emissions_Data.info()


# # **Summary of statistics of Data**

# In[5]:

Co2_Emissions_Data.describe()


# # **Missing values in data**

# In[6]:

Co2_Emissions_Data.isnull().sum()


# From the above outcome we can say that there are no null values in the dataset

# # **Visualizing that there are no Null values**

# In[7]:


ax = msno.bar(Co2_Emissions_Data, color="dodgerblue", figsize=(10,5), fontsize=12)
ax.set_title("Plot for displaying null values",color ="Darkred" ,fontsize = 26,loc = "Left")
plt.xlabel("Total number of non-null values within resective column",fontsize=14,color = "Darkblue")
plt.ylabel("Number of rows", fontsize=17,color = "Blue")


# We can infer from the above bar plot that there are no null values in any column as there is no empty space shown in them.

# # **Duplicate Values**
# 
# ### Count of duplicated rows

# In[8]:

Co2_Emissions_Data.duplicated().sum()


# ### Rows which are duplicated in dataset

# In[9]:

Co2_Emissions_Data.loc[Co2_Emissions_Data.duplicated(), :]


# # **Finding the outliers by using box plot**

# In[10]:

ax = sns.boxplot(x="CO2 Emissions(g/km)", data = Co2_Emissions_Data)
ax.set(xlabel="CO2 Emissions in gms/km")
ax.set_title("Box plot for checking outliers in CO2 emissions",color ="Darkred" ,fontsize = 20)
plt.xlabel("Co2 emission in g/km",fontsize=17,color = "Blue")


# From the above box plot we can infer that there is a single outlier in the given data, for which the co2 emission is above 500g/km .

# # **Correlation between columns in our dataset**

# In[11]:

corr = Co2_Emissions_Data.corr()

ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
ax.set_title("Plot for displaying correlation between various columns",color ="Darkred" ,fontsize = 22)
plt.xlabel("Column Names",fontsize=17,color = "Blue")


# In the above plot, Blue means positive and red means negitive. The darker the colour the stronger is the magnitude of correlation between them.

# # **Preliminary Visualizations**

# ## Count of different Vehicle Class spread over data

# In[12]:

ax = sns.countplot(y ='Vehicle Class', data = Co2_Emissions_Data)
ax.set_title("Number of vehicles for respective vehicle class", fontsize = 20,color ="Darkred")
plt.xlabel("Count",fontsize=17,color = "DarkBlue")
plt.ylabel("Vehicle Class", fontsize=17,color = "DarkBlue")
plt.show()


# From the above plot we can infer the number of various vehicle classes spread over the data.

# ## Number of cylinders across data

# In[13]:

ax = sns.countplot(x ='Cylinders', data = Co2_Emissions_Data)
ax.set_title("Count of cars using respective number of cylinders",color ="Darkred" ,fontsize = 20)
plt.xlabel("Number of cylinders",fontsize=17,color = "DarkBlue")
plt.ylabel("Count", fontsize=17,color = "DarkBlue")
plt.show()


# We can say that the maximum number of cars are using 4 cylinders.

# ## Fuel Types used among number of cars

# In[14]:

ax = sns.countplot(x ='Fuel Type', data = Co2_Emissions_Data)
ax.set_title("Count of cars using respective type of fuel ",color ="Darkred",fontsize = 20)
plt.xlabel("Type of fuel",fontsize=17,color = "DarkBlue")
plt.ylabel("Count", fontsize=17,color = "DarkBlue")
plt.show()


# **Code Refrences**

# * https://towardsdatascience.com/

# * https://coderzcolumn.com/

# * https://stackoverflow.com/
