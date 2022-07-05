#!/usr/bin/env python
# coding: utf-8

# <h1 align="center">PUMPKIN SEEDS</h1>
Pumpkin seeds are frequently consumed as confection worldwide because of their adequate amount of protein, fat, carbohydrate, and mineral contents. This study was carried out on the two most important and quality types of pumpkin seeds, ‘‘Urgup_Sivrisi’’ and ‘‘Cercevelik’’, generally grown in Urgup and Karacaoren regions in Turkey. However, morphological measurements of 2500 pumpkin seeds of both varieties were made possible by using the gray and binary forms of threshold techniques. Considering morphological features, all the data were modeled with five different machine learning methods: Logistic Regression (LR), Support Vector Machine (SVM) and Random Forest (RF), Decision Tree classifier and Naive Bayes.
# ![shutterstock_229783426.jpg](attachment:shutterstock_229783426.jpg)

# ## Problem Solving
Fetching the details to identify the varities of seeds.
# ## Reference
https://www.kaggle.com/datasets/muratkokludataset/pumpkin-seeds-dataset
# ### Functions:
# - STEP 1:Importing Libraries
# - STEP 2:Reading and Preparing the dataset
# - STEP 3:Exploring the data
# - STEP 4:Cleaning the data
# - STEP 5:Exracting the data
# - STEP 6:Visualizing the data
# - STEP 7:Creating a model
# - STEP 8:Conclusion

# ## STEP 1:Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# ## STEP 2:Reading and Preparing the dataset

# ### Read the data

# In[2]:


d=pd.read_excel('Pumpkin_Seeds_Dataset.xlsx')


# ### View the data

# In[3]:


d


# ## STEP 3:Exploring the data

# ### To check how many rows and columns

# In[4]:


d.shape


# ### Column names

# In[5]:


d.columns


# ### Top 5 datas

# In[6]:


d.head()


# ### Bottom 5 datas

# In[7]:


d.tail()


# ### Information of data

# In[8]:


d.info()


# ### Datatypes

# In[9]:


d.dtypes


# ### Statistical information

# In[10]:


d.describe().transpose()


# ### Correlation of dataset

# In[11]:


d.corr()


# ### Covariance of dataset

# In[12]:


d.cov()


# ## STEP 4:Cleaning the data

# ### To check is there any null values

# In[13]:


d.isnull().sum()


# ### To check is there any duplicated

# In[14]:


d.duplicated().sum()


# ## STEP 5:Exracting the data

# ### Unique values

# In[15]:


d.nunique()


# ### Unique value for class

# In[16]:


d['Class'].unique()


# ### Class value counts

# In[17]:


d['Class'].value_counts()


# ## STEP 6:Visualizing the data

# ### Piechart for Class

# In[18]:


plt.title('Class',fontsize=20)
d['Class'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True)
plt.show()


# ### Countplot for Class

# In[19]:


sns.countplot(x='Class',data=d,palette='tab10')
plt.show()


# ### Heatmap

# In[20]:


n_data=['Area','Perimeter','Major_Axis_Length','Minor_Axis_Length']
plt.figure(figsize=(10,5))
sns.heatmap(d[n_data].corr(),annot=True,fmt='.4f',cmap='coolwarm_r',center=0)
plt.show()


# In[21]:


d.hist(bins=20 ,figsize=(20,15),color='blue')
plt.show()


# ## STEP 7:Creating a model

# - Target(Class)
# - Features (Area,Perimeter,Major_Axis_Length,Minor_Axis_Length,Convex_Area,Equiv_Diameter,Eccentricity,Solidity,Extent,Roundness,Aspect_Ration,Compactness).

# In[22]:


x=d.drop(['Class'],axis=1)


# In[23]:


x


# In[24]:


y=d.Class


# In[25]:


y


# ### Train Test Split

# In[26]:


from sklearn.model_selection import train_test_split


# #### Splitting the dataset:
# - test_size = 0.25 so that data is split into 75% and 25%
# - random_state is applied so that each time we run we get the same result

# ### Model Creation

# In[27]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=2)


# In[28]:


x_train.shape


# In[29]:


x_test.shape


# In[30]:


y_train.shape


# In[31]:


y_test.shape


# #### Training the data with Some of the ML approaches:
# - Logistic Regression
# - Decision Tree Classifier
# - Random Forest Classifier
# - Naive Bayes

# ### Logistic Regression

# In[71]:


plt.xlabel("Area")
plt.ylabel("Class")
plt.scatter(d.Area,d.Class,marker="*",color="green")
plt.show()


# In[72]:


from sklearn.linear_model import LogisticRegression


# In[75]:


model_l= LogisticRegression()


# In[77]:


model_l.fit(x_train,y_train)


# In[80]:


model_l.score(x_train,y_train)


# In[81]:


model_l.score(x_test,y_test)


# In[82]:


y_predict=model_l.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_predict)
print('The Testing Accuracy of the algorithm is ', accuracy_score(y_test, y_predict))


# #### Confusion matrix

# In[83]:


from sklearn.metrics import confusion_matrix
perfomance=confusion_matrix(y_test,y_predict)
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(model,x_test,y_test)
plt.show()


# #### Classification report

# In[40]:


from sklearn.metrics import classification_report
performance_report=classification_report(y_test,y_predict)
print(performance_report)


# ### Decision tree classifier

# In[41]:


from sklearn.tree import DecisionTreeClassifier


# In[42]:


model_d=model=DecisionTreeClassifier()


# In[43]:


model_d.fit(x_train,y_train)


# In[44]:


model_d.score(x_test,y_test)


# In[45]:


y_predict=model_d.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_predict)
print('The Testing Accuracy of the algorithm is ', accuracy_score(y_test, y_predict))


# #### Confusion matrix

# In[46]:


from sklearn.metrics import confusion_matrix
perfomance=confusion_matrix(y_test,y_predict)
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(model,x_test,y_test)
plt.show()


# #### Classification Report

# In[47]:


from sklearn.metrics import classification_report
performance_report=classification_report(y_test,y_predict)
print(performance_report)


# ### Random Forest Classifier

# In[48]:


from sklearn.ensemble import RandomForestClassifier


# In[49]:


model_r=RandomForestClassifier()


# In[50]:


model_r.fit(x,y)


# In[51]:


model_r.score(x_test,y_test)


# In[52]:


y_predict=model_r.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_predict)
print('The Testing Accuracy of the algorithm is ', accuracy_score(y_test, y_predict))


# #### Confusion matrix

# In[53]:


from sklearn.metrics import confusion_matrix
perfomance=confusion_matrix(y_test,y_predict)
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(model_r,x_test,y_test)
plt.show()


# #### Classification report

# In[54]:


from sklearn.metrics import classification_report
performance_report=classification_report(y_test,y_predict)
print(performance_report)


# ### Naive Bayes

# In[55]:


from sklearn.naive_bayes import GaussianNB


# In[56]:


model_N=GaussianNB()


# In[57]:


model_N.fit(x_train,y_train)


# In[58]:


model_N.score(x_test,y_test)


# In[59]:


y_predict=model_N.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_predict)
print('The Testing Accuracy of the algorithm is ', accuracy_score(y_test, y_predict))


# In[60]:


from sklearn.metrics import confusion_matrix
perfomance=confusion_matrix(y_test,y_predict)
from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(model_N,x_test,y_test)
plt.show()


# #### Classification Report

# In[61]:


from sklearn.metrics import classification_report
performance_report=classification_report(y_test,y_predict)
print(performance_report)


# ## STEP 8:Conclusion

# In[66]:


results = pd.DataFrame(columns = [ 'Testing Accuracy Base Model'],index = ['Logistic Regression', 'Decision Tree Classifier', 'Random Forest Classifier', 'Naive Bayes'])


# In[84]:


results.loc['Logistic Regression'] = model_l.score(x_test,y_test) ;
results.loc['Decision Tree Classifier'] = model_d.score(x_test,y_test);
results.loc['Random Forest Classifier'] = model_r.score(x_test,y_test);
results.loc['Naive Bayes'] = model_N.score(x_test,y_test);


# In[85]:


results


# I have achieved good accuracy in <b> Random Forest Algorithm </b>
# 

# In[ ]:




