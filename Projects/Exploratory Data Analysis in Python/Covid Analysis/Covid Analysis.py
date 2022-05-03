#!/usr/bin/env python
# coding: utf-8

# # Covid Analysis

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


d=pd.read_csv("covid.csv")


# ### View the data

# In[3]:


d


# In[4]:


d.shape


# In[5]:


d.dtypes


# In[6]:


d.isnull().sum()


# In[7]:


d.drop(['Province/State','Last Update','SNo'],axis=1 ,inplace=True)


# In[8]:


d


# In[9]:


d.isnull().sum()


# In[10]:


d['ObservationDate']=pd.to_datetime(d['ObservationDate'])


# In[11]:


d.dtypes


# In[34]:


d


# In[35]:


d.info()


# In[36]:


d.describe()


# In[37]:


d.describe().transpose()


# In[38]:


d.head()


# In[39]:


d.tail()


# ### grouping cases as per the date

# In[40]:


date_wise=d.groupby(['ObservationDate']).agg({'Confirmed':'sum','Deaths':'sum','Recovered':'sum'})


# In[41]:


date_wise


# In[42]:


date_wise.head()


# ### total no.of confirmed cases around the world

# In[43]:


date_wise['Confirmed'].iloc[-1]


# In[44]:


date_wise['Recovered'].iloc[-1]


# In[45]:


date_wise['Deaths'].iloc[-1]


# ### Total no.of active cases

# In[46]:


date_wise['Confirmed'].iloc[-1]-date_wise['Recovered'].iloc[-1]-date_wise['Deaths'].iloc[-1]


# ### Total no.of closed cases

# In[47]:


date_wise['Deaths'].iloc[-1]+date_wise['Recovered'].iloc[-1]


# In[48]:


plt.figure(figsize=(20,10))
sns.barplot(x=date_wise.index,y=date_wise['Confirmed']-date_wise['Recovered']-date_wise['Deaths'])

plt.xticks(rotation=90)
plt.title('Distribution for active cases')
plt.show()


# In[49]:


plt.figure(figsize=(20,10))
sns.barplot(x=date_wise.index,y=date_wise['Recovered']+date_wise['Deaths'])

plt.xticks(rotation=90)
plt.title('Distribution for closed cases')
plt.show()


# In[50]:


date_wise['week']=date_wise.index.weekofyear


# In[51]:


date_wise


# In[52]:


week_num=[]
week_confirmed=[]
week_recovered=[]
week_deaths=[]
w=1
for i in list(date_wise['week'].unique()):
    week_confirmed.append(date_wise[date_wise['week']==i]['Confirmed'].iloc[-1])
    week_deaths.append(date_wise[date_wise['week']==i]['Deaths'].iloc[-1])
    week_recovered.append(date_wise[date_wise['week']==i]['Recovered'].iloc[-1])
    week_num.append(w)
    w=w+1


# In[53]:


plt.figure(figsize=(9,6))
plt.plot(week_num,week_confirmed,linewidth=3)
plt.plot(week_num,week_recovered)
plt.plot(week_num,week_deaths)
plt.xlabel('No. of weeks')
plt.ylabel('No. of cases')
plt.title('Weekly progrss of cases')

plt.show()


# In[54]:


fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(18,7))
sns.barplot(x=week_num,y=pd.Series(week_confirmed).diff().fillna(0),ax=ax1)
sns.barplot(x=week_num,y=pd.Series(week_recovered).diff().fillna(0),ax=ax2)
sns.barplot(x=week_num,y=pd.Series(week_deaths).diff().fillna(0),ax=ax3)
ax1.set_xlabel('Number of weeks')        
ax2.set_xlabel('Number of weeks')        
ax3.set_xlabel('Number of weeks') 
ax1.set_ylabel('Number of confirmed cases')
ax2.set_ylabel('Number of recovered cases')
ax3.set_ylabel('Number of deaths cases')
                               
plt.show()


# ### Average increase in number of confirmed cases everyday

# In[55]:


np.round(date_wise['Confirmed'].diff().fillna(0).mean())


# ### Average increase in number of death cases everyday

# In[56]:


np.round(date_wise['Deaths'].diff().fillna(0).mean())


# ### Average increase in number of recovered cases everyday

# In[57]:


np.round(date_wise['Recovered'].diff().fillna(0).mean())


# In[58]:


plt.figure(figsize=(11,5))
plt.plot(date_wise['Confirmed'].diff().fillna(0),label='Daily increase in Confirmed cases')
plt.plot(date_wise['Recovered'].diff().fillna(0),label='Daily increase in Recovered cases')
plt.plot(date_wise['Deaths'].diff().fillna(0),label='Daily increase in Deaths cases')
plt.xlabel('Time')
plt.ylabel('No.of increases')

plt.show()


# In[59]:


d


# In[60]:


country_wise=d[d['ObservationDate']==d['ObservationDate'].max()].groupby(['Country/Region']).agg({'Confirmed':'sum','Deaths':'sum','Recovered':'sum'}).sort_values(['Confirmed'],ascending=False)
country_wise


# In[62]:


country_wise['Mortality']=(country_wise['Deaths']/country_wise['Recovered'])*100
country_wise


# In[63]:


country_wise['Recovered']=(country_wise['Recovered']/country_wise['Confirmed'])*100
country_wise['Recovered']


# In[64]:


fig,(ax1,ax2)=plt.subplots(1,2,figsize=(20,7))
top15_confirmed=country_wise.sort_values(['Confirmed'],ascending=False).head(15)
top15_death=country_wise.sort_values(['Deaths'],ascending=False).head(15)
sns.barplot(x=top15_confirmed['Confirmed'],y=top15_confirmed.index,ax=ax1)
sns.barplot(x=top15_death['Deaths'],y=top15_death.index,ax=ax2)
ax1.set_title('Top 15 Countries as per Number of Confirmed cases')
ax2.set_title('Top 15 Countries as per Number of Death cases')
plt.show()


# In[ ]:




