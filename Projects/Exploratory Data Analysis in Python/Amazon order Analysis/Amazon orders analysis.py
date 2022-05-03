#!/usr/bin/env python
# coding: utf-8

# # Amazon Order Analysis

# ### Importing libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings 
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Read the data  

# In[2]:


d=pd.read_excel("amazon orders_data.xlsx")


# ### To view the data

# In[3]:


d


# ### To check how many rows and columns

# In[4]:


d.shape


# ### To print fields name

# In[5]:


d.columns


# ###  The data type of attributes
# 

# In[6]:


d.dtypes


# In[7]:


d['order_date']=pd.to_datetime(d['order_date'])


# In[8]:


d


# In[9]:


d.dtypes


# ## Data Cleaning

# ### To check is there any missing value

# In[10]:


d.isnull()


# In[11]:


d.isnull().sum()


# In[12]:


d


# ### Drop the unwanted columns

# In[13]:


d.drop(['cod','sku'],axis=1 ,inplace=True)


# In[14]:


d


# ### Drop the null values

# In[15]:


d.dropna(inplace=True)
d


# ### Total number of null values in a dataset

# In[16]:


d.isnull().sum().sum()


# ### Print top 5 records

# In[17]:


d.head()


# ### Print bottom 5 records

# In[18]:


d.tail()


# ### Information of a dataset

# In[19]:


d.info()


# ### Statistical information

# In[20]:


d.describe()


# In[21]:


d.describe(include='all')


# In[22]:


d.describe().transpose()


# ### To check is there any duplicated values

# In[23]:


d.duplicated().sum()


# ### Rename the column names

# In[24]:


d.rename(columns={"item_total":"Productcost","ship_city":"city","ship_state":"state"},inplace=True)


# In[25]:


d


# ### Print some random lines

# In[26]:


d.sample(4)


# In[27]:


d


# ### Categorize quantity,productcost,shipping fee under order no.

# In[28]:


order_no_wise=d.groupby(['order_no']).agg({'quantity':'sum','Productcost':'max','shipping_fee':'max'})


# In[29]:


order_no_wise


# In[30]:


order_no_wise.head()


# ### Total no. of products are sold

# In[31]:


d['quantity'].sum()


# In[32]:


d1=d.copy()


# In[33]:


d1


# ### Categorize amount of product under state wise

# In[34]:


d1=d1.groupby(['state'])['quantity'].sum()
d1=pd.DataFrame(d1)
d1


# ### Categorize productcost under statewise

# In[35]:


state_Productcost_d = pd.pivot_table(data=d[['state','Productcost']], 
                        index=['state'], 
                        values='Productcost',
                        aggfunc='max')


# In[36]:


state_Productcost_d.sort_values(by='Productcost', ascending=False)


# ### Pivot table for state,city and buyer

# In[37]:


buyer_state_city_d = pd.pivot_table(data=d[['state','city','buyer']], 
                        index=['state','city'], 
                        values='buyer',
                        aggfunc='sum')


# In[38]:


buyer_state_city_d.head(20)


# In[39]:


d


# ## Data visualization

# ### Visualize quantity of products according to productcost

# In[40]:


plt.figure(figsize=(18,5))
plt.bar('quantity','Productcost', data=d,color='pink')
plt.title('Quantity of products according to Productcost',fontsize=15,color='black')
plt.xlabel('quantity',fontsize=15)
plt.ylabel('Productcost',fontsize=15)

plt.show()


# ### Visualization of which state bought highest amount of products

# In[41]:


print(d['state'].value_counts())
plt.figure(figsize=(15,4))
sns.countplot(x=d['state'])
plt.xticks(rotation=90)
plt.show()


# ### Visualization for order status according to states

# In[42]:


d=d.head(50)
sns.relplot(x='quantity',y='city',hue='order_status',data=d)
plt.show()


# ### Categorize the maximum percentage of products sold in city

# In[44]:


d=d.head(15)
plt.title('City',fontsize=20)
d['city'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True)
plt.show()


# In[ ]:




