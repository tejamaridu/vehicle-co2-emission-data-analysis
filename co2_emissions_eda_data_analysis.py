#!/usr/bin/env python
# coding: utf-8

# # DAB103_Project1_Group7
# 
# ## Source link -
# https://www.kaggle.com/debajyotipodder/co2-emission-by-vehicles?select=CO2+Emissions_Canada.csv

# # **Importing Libraries**

# In[2]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


# # **Changing Directory and importing dataset**

# In[57]:


path = 'D:\DAB\DAB-103 Analytic tools and decision making\Project\Proj1'
os.chdir(path)

Co2_Emissions_Data = pd.read_csv("CO2 Emissions_Canada.csv")


# # **The Shape of the dataset is as follow**

# In[58]:


Co2_Emissions_Data.shape


# 
# The imported dataset has 7385 Rows and 12 Columns.

# # **We are viewing the first few rows of dataset**

# In[6]:


Co2_Emissions_Data.head()


# # **Column names and their data types**

# In[7]:


Co2_Emissions_Data.info()


# # **Summary of statistics of Data**

# In[8]:


Co2_Emissions_Data.describe()


# # **Missing values in data**

# In[9]:


Co2_Emissions_Data.isnull().sum()


# From the above outcome we can say that there are no null values in the dataset

# # **Visualizing that there are no Null values**

# In[11]:


ax = msno.bar(Co2_Emissions_Data, color="dodgerblue", figsize=(10,5), fontsize=12)
ax.set_title("Plot for displaying null values",color ="Darkred" ,fontsize = 26,loc = "Left")
plt.xlabel("Total number of non-null values within resective column",fontsize=14,color = "Darkblue")
plt.ylabel("Number of rows", fontsize=17,color = "Blue")


# We can infer from the above bar plot that there are no null values in any column as there is no empty space shown in them.

# # **Duplicate Values**
# 
# ### Count of duplicated rows

# In[12]:


Co2_Emissions_Data.duplicated().sum()


# ### Rows which are duplicated in dataset

# In[13]:


Co2_Emissions_Data.loc[Co2_Emissions_Data.duplicated(), :]


# # Data Segmentation

# In[15]:


transmission = Co2_Emissions_Data['Transmission'].sort_index()
transmission.value_counts()


# In[17]:


engineSize = Co2_Emissions_Data['Model'].sort_index()
engineSize.value_counts()


# In[19]:


Make = Co2_Emissions_Data['Make'].sort_index()
Make.value_counts()


# The above mentioned data respresents how the data segments are distributed accross the data. We have considered 3 features which are Transmission, Engine size and Makers Respectively.

# # **Finding the outliers by using box plot**

# In[21]:


ax = sns.boxplot(x="CO2 Emissions(g/km)", data = Co2_Emissions_Data)
ax.set(xlabel="CO2 Emissions in gms/km")
ax.set_title("Box plot for checking outliers in CO2 emissions",color ="Darkred" ,fontsize = 20)
plt.xlabel("Co2 emission in (grams/km)",fontsize=17,color = "Blue")


# From the above box plot we can infer that there is a single outlier in the given data, for which the co2 emission is above 500g/km .

# In[23]:


ax = sns.boxplot(x="Fuel Consumption City (L/100 km)", data = Co2_Emissions_Data)
ax.set_title("Box plot for checking outliers of Fuel Consumption in City",color ="Darkred" ,fontsize = 20)
plt.xlabel("Fuel Consumption in City (Litres/100 km)",fontsize=17,color = "Blue")


# This box plot visualizes the mileage in city by different vehicles outliers.

# In[25]:


ax = sns.boxplot(x="Fuel Consumption Hwy (L/100 km)", data = Co2_Emissions_Data)
ax.set_title("Box plot for checking outliers of Fuel Consumption in Highway",color ="Darkred" ,fontsize = 20)
plt.xlabel("Fuel Consumption in Highway (Litres/100 km)",fontsize=17,color = "Blue")


# This box plot visualizes the mileage on highway by different vehicles outliers.

# # **Correlation between columns in our dataset**

# In[28]:


columns = ['CO2 Emissions(g/km)','Fuel Consumption City (L/100 km)']
subset = Co2_Emissions_Data[columns]
subset.corr()


# In[30]:


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


# This heatmap gives a graphical    representation of the correlation between various features. In this plot, Blue means positive and red means negative. The darker the color the stronger is the magnitude of correlation between them.

# # **Preliminary Visualizations**

# ## Count of different Vehicle Class spread over data

# In[32]:


ax = sns.countplot(y ='Vehicle Class', data = Co2_Emissions_Data)
ax.set_title("Number of vehicles for respective vehicle class", fontsize = 20,color ="Darkred")
plt.xlabel("Count",fontsize=17,color = "DarkBlue")
plt.ylabel("Vehicle Class", fontsize=17,color = "DarkBlue")
plt.show()


# From the above plot we can infer the number of various vehicle classes spread over the data.

# ## Number of cylinders across data

# In[34]:


ax = sns.countplot(x ='Cylinders', data = Co2_Emissions_Data)
ax.set_title("Count of cars using respective number of cylinders",color ="Darkred" ,fontsize = 20)
plt.xlabel("Number of cylinders",fontsize=17,color = "DarkBlue")
plt.ylabel("Count", fontsize=17,color = "DarkBlue")
plt.show()


# We can say that the maximum number of cars are using 4 cylinders.

# ## Fuel Types used among number of cars

# In[36]:


ax = sns.countplot(x ='Fuel Type', data = Co2_Emissions_Data)
ax.set_title("Count of cars using respective type of fuel ",color ="Darkred",fontsize = 20)
plt.xlabel("Type of fuel",fontsize=17,color = "DarkBlue")
plt.ylabel("Count", fontsize=17,color = "DarkBlue")
plt.show()


# # Data Cleaning / Transformation

# ### The number of Rows and Columns before removing the duplicates

# In[37]:


Co2_Emissions_Data.shape


# ## Duplicated Rows

# In[59]:


Co2_Emissions_Data[Co2_Emissions_Data.duplicated()]


# ## Dropping Duplicated Rows

# In[60]:


Co2_Emissions_Data = Co2_Emissions_Data.drop_duplicates()


# ### The Number of Rows and Columns after removing Duplicates

# In[61]:


Co2_Emissions_Data.shape


# ## Missing Values in the Dataset

# In[62]:


Co2_Emissions_Data[Co2_Emissions_Data.isnull()]


# ### Count of Missing Values

# In[63]:


Co2_Emissions_Data.isnull().sum()


# From the above count and the table it is evident that there are no missing values

# ### Transforming Fuel Type names in Fuel types column

# Creating a dictionary for transforming Fuel Types names

# In[64]:


Fuel_Types = {
    "X" : "Regular Gasoline",
    "Z" : "Premium Gasoline",
    "D" : "Diesel",
    "E" : "Ethanol (E85)",
    "N" : "Natural Gas"
}


# In[65]:


Co2_Emissions_Data["Fuel Type"] = Co2_Emissions_Data["Fuel Type"].map(Fuel_Types)


# We have used map function here to change the names of fuel types from fuel type codes( X,Z,D,E,N) to names which are more human readable

# ### Exporting Data in Excel Format for visualizing data in Tableau

# In[67]:


Co2_Dataset_Excel = Co2_Emissions_Data.to_excel("CO2_Emissions_Canada1.xlsx")


# ## **Code Refrences**

# * https://towardsdatascience.com/

# * https://coderzcolumn.com/

# * https://stackoverflow.com/

# * https://www.geeksforgeeks.org/countplot-using-seaborn-in-python/

# * https://towardsdatascience.com/better-heatmaps-and-correlation-matrix-plots-in-python-41445d0f2bec

# * https://towardsdatascience.com/visualizing-the-nothing-ae6daccc9197
