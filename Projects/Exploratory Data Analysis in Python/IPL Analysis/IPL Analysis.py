#!/usr/bin/env python
# coding: utf-8

# # IPL Analysis

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


d=pd.read_csv('IPL Matches 2008-2020.csv')


# In[4]:


d


# In[4]:


d.shape


# In[5]:


d.dtypes


# In[6]:


d.columns


# In[7]:


d.isnull()


# In[8]:


d.isnull().sum()


# In[9]:


d.isnull().sum().sum()


# In[10]:


d.shape


# In[11]:


d=d.drop(['method'],axis=1)


# In[12]:


d


# In[13]:


d.isnull().sum()


# In[14]:


d.dropna(axis=0,inplace=True)


# In[15]:


d


# In[16]:


d.isnull().sum()


# In[17]:


d.head()


# In[18]:


d.head(10)


# In[19]:


d.tail()


# In[20]:


d.info()


# In[35]:


d.describe()


# In[36]:


d.describe().transpose()


# In[23]:


d.duplicated().sum()


# In[24]:


d.sample(4)


# In[25]:


d.nunique()


# In[28]:


d.head()


# In[30]:


d.rename(columns={'toss_decision':'decision'},inplace=True)


# In[31]:


d.head()


# In[33]:


d.drop(['id','neutral_venue'],axis=1,inplace=True)


# In[34]:


d.head()


# In[39]:


d['result'].value_counts()


# In[40]:


d.sort_values(by=['city'])


# In[47]:


d['player_of_match'].nunique()


# In[48]:


d['player_of_match'].unique()


# In[49]:


d[d['venue']=='Sheikh Zayed Stadium']


# In[55]:


ven_grp = d.groupby('venue')
print(ven_grp)


# In[56]:


max_ven = ven_grp['winner','result_margin'].max().sort_values(by='result_margin',ascending=False)
max_ven


# In[57]:


n=d.groupby('winner').result_margin.max().sort_values(ascending=False)
n


# In[58]:


n=d.groupby('winner').player_of_match.max().sort_values(ascending=True)
n


# In[59]:


n=d.groupby('winner').player_of_match.max()
n


# In[60]:


winner_wise = d.groupby('winner')
mean_res = winner_wise['winner','result_margin'].mean().sort_values(by='result_margin',ascending=False)
mean_res


# In[61]:


pd.crosstab(d['venue'],d['winner'])


# In[63]:


d.groupby("decision").winner.value_counts()


# In[65]:


d.info()


# In[66]:


d['year'] = pd.DatetimeIndex(d['date']).year


# In[68]:


d.head()


# In[69]:


d.info()


# In[70]:


pd.crosstab(d['team1'],d['team2'])


# In[72]:


d.groupby('winner').result.value_counts()


# In[73]:


teams_per_year = d.groupby('year')['winner'].value_counts()
teams_per_year


# In[76]:


teams_per_year.head(25)


# In[77]:


teams_per_year.tail(25)


# In[83]:


s=d.sort_values(by=['result_margin'])['winner']


# In[85]:


s.head(50)


# In[78]:


d.head()


# In[79]:


d.drop(['umpire1','umpire2'],axis=1,inplace=True)
d


# In[87]:


winner_per_year = d.groupby(['winner','year'])['result'].value_counts()
winner_per_year.head(50)


# In[89]:


d3=d.copy()
d3=d3.pivot_table('result_margin',columns='winner',aggfunc='max')
d3


# In[91]:


d.pivot_table('decision',columns='year',aggfunc='max')


# In[92]:


print(d['winner'].value_counts())
plt.figure(figsize=(10,6))
sns.countplot(x=d['winner'])
plt.xticks(rotation=90)
plt.show()


# In[93]:


plt.title('Winner',fontsize=20)
d['winner'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,figsize=(12,12))
plt.show()


# In[95]:


plt.figure(figsize=(25,10))
plt.bar(d['winner'],d['venue'],color='red')
plt.title('winner Vs venue')
plt.xlabel('winner',fontsize=15)
plt.ylabel('venue',fontsize=15)
plt.show()


# In[96]:


d.pivot_table('year',columns='city',aggfunc='min')


# In[98]:


sns.countplot('venue', data=d)
plt.xticks(rotation='vertical')
plt.show()


# In[99]:


plt.title('toss_winner',fontsize=20)
d['toss_winner'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,figsize=(22,12))
plt.show()


# In[100]:


d[d['city']=="Bangalore"].player_of_match.unique()


# In[101]:


sns.kdeplot(d['result_margin'])
plt.show()


# In[107]:


d.groupby('city')[['result_margin']].max().plot.bar(color=['orange'],figsize=(8,5))
plt.ylabel('cityvswinner')
plt.show()


# In[108]:


sns.violinplot(x='year',y='result_margin',data=d)
plt.show()


# In[ ]:




