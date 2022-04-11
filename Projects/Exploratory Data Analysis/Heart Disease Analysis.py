#!/usr/bin/env python
# coding: utf-8

# ## Introduction To Data

# This data shows details of patients and basically based on an analysis on heart disease . The analysing the basic factors with heart disease in patients . It compares many factors like BMI , physical and mental health of the person , if the person is alcoholic etc ....By analysing this data we can conclude about the relation of factors with heart disease . 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

import warnings 
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# ## To read the data

# In[2]:


df=pd.read_excel('heartdisease.xls')


# In[8]:


df


# ## shape of the data

# In[6]:


df.shape


# ## columns in the data

# In[7]:


df.columns


# ## Data types of each column in the data

# In[8]:


df.dtypes


# ### Observations:-
# It has only 4 columns consist of numerical values and others are objects

# ## To check if there is any null values

# In[9]:


df.isnull()


# In[11]:


df.isnull().sum()


# ### Observations:-
# This shows that tha data donot contain any null values

# ## To get first 5 rows

# In[12]:


df.head()


# ## To get last 5 rows

# In[13]:


df.tail()


# ## Total information about the data

# In[14]:


df.info()


# ### Observations:-
# This gives the all information about the data

# ## To find if there is any duplicates

# In[29]:


df.duplicated().sum()


# In[30]:


d=df.drop_duplicates()


# In[31]:


df


# ### Observations:-
# This gives if there is any duplicate value and to drop that columns

# ## Statistical description of tha data

# In[32]:


df.describe()


# ### Observations:-
# This gives almost all basic functions in statistics.
# * Here,
#   count , mean , standard deviation ,  minimum values , 25 50 75 percentailes and maximum values of all the columns 
#   

# In[33]:


df.nunique()


# ## Correlation

# In[34]:


df.corr()


# ## Covariance

# In[35]:


df.cov()


# ### Observations:-
# all the factors depend each other 

# ## Sort data by Heart Disease

# In[36]:


df.sort_values(by=['HeartDisease'])


# ## Pivot table

# In[16]:


d1=df.copy()
d1=d1.pivot_table('MentalHealth',columns='AgeCategory',aggfunc='max')
d1


# ### Observations:-
# From this we can see that in all category of age the maximum mental health is 30 
# 

# ## Bar graph of BMI and PhysicalHealth

# In[5]:


plt.figure(figsize=(25,10))
plt.bar(df['BMI'],df['PhysicalHealth'])
plt.title('BMI Vs PhysicalHealth',fontsize=15,color='red')
plt.xlabel('BMI',fontsize=15)
plt.ylabel('PhysicalHealth',fontsize=15)
plt.xticks(rotation=90)
plt.grid(True)
plt.show()


# ### Observations:-
# We can see the variation in physical health when the BMI is increasing
# 
# 

# ## Bar graph of Physical health and Mental health

# In[4]:


plt.figure(figsize=(18,15))
plt.bar('PhysicalHealth','MentalHealth',data=df,color='green')
plt.show()


# ## Relplot

# In[6]:


sns.relplot(x='AgeCategory',y='PhysicalHealth',hue='BMI',data=df)
plt.xticks(rotation=90)
plt.show()


# ### Observations:-
# From this we can see that the range of BMI is in 15-60 in all age category , in most age category when mental health is less than 5 it is effecting the BMI
# 
# 

# ##  Bar graph of Age category against BMI and Physical health 

# In[5]:


df.groupby('AgeCategory')[['BMI','PhysicalHealth']].sum().plot.bar(color=['red','blue'],figsize=(8,5))
plt.ylabel('BMI and PhysicalHealth')
plt.show()


# ### Observations:-
# From this it's clear that ages between 60-74 has higher BMI and Physical health
# 

# ## Bar graph of age category and mental health

# In[15]:


plt.figure(figsize=(12,8))

sns.barplot(x='AgeCategory',y='MentalHealth',data=df,palette='coolwarm_r')
plt.xlabel('AgeCategory',fontsize=15)
plt.show()


# ### Observations:-
# Age between 18-24 , have higher Mental health
# 

# ## Bar chart of Sleep time against Mental health and Physical health

# In[6]:


df.groupby('SleepTime')[['MentalHealth','PhysicalHealth']].sum().plot.bar(color=['green','orange'],figsize=(8,5))
plt.xticks(rotation=90)
plt.ylabel('MentalHealth and PhysicalHealth ')
plt.show()


# ### Observations:-
# From this we can see that people who sleep 6-8 hrs has good mental as well as physical health and also we can see that those who sleep more than 8 hrs, doesn't have good physical and mental health 
# 

# ## Heat map

# In[11]:


n_data=['BMI','AgeCategory','MentalHealth','PhysicalHealth']
plt.figure(figsize=(10,5))
sns.heatmap(df[n_data].corr(),annot=True,fmt='.4f',cmap='coolwarm_r',center=0)
plt.show()


# ## Line plot

# In[3]:


plt.figure(figsize=(10,4))
sns.lineplot('MentalHealth','SleepTime',data=df,color='r',label='MentalHealth')
plt.legend()
plt.show()


# ### Observations:-
# We can see that mental health and sleep time are related to each other if there is a good sleep(6-8) there is also good mental health
# 

# ## Histograms

# In[13]:


df.hist(bins=20,figsize=(20,15),color='red')
plt.show()


# ## Pair plot

# In[14]:


sns.pairplot(df,hue='MentalHealth')
plt.show()


# ### Observations:-
# Here we plotted mental health as hue against each column like we seen that good sleep , good physical health and an good BMI can influence  mental health of a person also.

# ## scatter plot

# In[12]:


sns.scatterplot(x='MentalHealth',y='SleepTime',hue='PhysicalHealth',data=df)
plt.show()


# ### Observations:-
# We can see that those who have good mental health and good sleep time (6-8) have good physical health also
# 

# ## Cat plot

# In[18]:


sns.catplot(x='MentalHealth',y='SleepTime',hue='PhysicalHealth',data=df)
plt.xticks(rotation=90)
plt.show()


# ## observations:-

# ## Cat plot of box kind

# In[19]:


sns.catplot(x='MentalHealth',y='SleepTime',kind='boxen',data=df)
plt.xticks(rotation=90)
plt.show()


# ### Observations:-

# ## kde plot

# In[20]:


sns.kdeplot(df['SleepTime'])
plt.show()


# ### Observations:-
# Here we can see that most people have a good sleep time that is 6-8 hrs
# 

# In[4]:


sns.kdeplot(df['SleepTime'],df['MentalHealth'],color='green',shade=True)
plt.show()


# ### Observations:-
# This compares  the sleep time and mental health of each person. Here we can see that sleep time less than 5 hrs and more than 10 hrs doesnot have a good mental health
# 

# ## Voilin plot

# In[5]:


sns.violinplot(x=df.MentalHealth)
plt.show()


# ### Observations:-
# This  shows the value range of mental health .
# The mental health that more people have is between 0-5
