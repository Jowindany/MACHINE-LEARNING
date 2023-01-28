#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


# In[3]:


data_set=pd.read_csv("loan_predicton.csv")


# In[4]:


data_set.head()


# In[5]:


data_set.shape


# In[6]:


data_set.describe()


# In[11]:


data_set.isnull().sum()


# In[9]:


data_set.replace({'Loan_Status':{'N':0,'Y':1}},inplace=True)


# In[10]:


data_set.head()


# In[12]:


data_set['Dependents'].value_counts()


# In[43]:


sns.countplot(x='Education',hue='Loan_Status',data=data_set,color='lightgreen')


# In[42]:


sns.countplot(x='Gender',hue='Loan_Status',data=data_set,color='lightpink')


# In[45]:


sns.countplot(x='Married',hue='Loan_Status',data=data_set,color='lightblue')


# In[60]:


sns.countplot(x='Self_Employed',hue='Loan_Status',data=data_set,palette='BuPu')


# In[17]:


data_set['Loan_Status'].value_counts()


# In[65]:


sns.countplot(x='Property_Area',hue='Loan_Status',data=data_set,palette='Greens')


# In[56]:


data_set['Credit_History'].value_counts()


# In[59]:


sns.countplot(x='Credit_History',hue='Loan_Status',data=data_set,palette='pastel')


# In[69]:


amount_data=data_set[['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_ID']]


# In[70]:


amount_data


# In[73]:


amount_data['ApplicantIncome'].mean()


# In[77]:


sns.heatmap(amount_data.corr(),cmap="Greens")


# In[84]:


sns.scatterplot(x='LoanAmount',y='ApplicantIncome',hue='Loan_Status',data=data_set)


# In[90]:


sns.scatterplot(x='LoanAmount',y='CoapplicantIncome',hue='Loan_Status',data=data_set)


# In[93]:


x=data_set.drop(columns=['Loan_ID','Loan_Status'],axis=1)
y=data_set['Loan_Status']


# In[94]:


print(x)
print(y)


# In[95]:


x.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)


# In[96]:


print(x)


# In[104]:


x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.1,random_state=2,stratify=y)


# In[106]:


classifier= svm.SVC(kernel='linear')


# In[105]:


x.shape,x_train.shape,x_test.shape


# In[107]:


classifier.fit(x_train,y_train)


# In[108]:


train_data_prediction=classifier.predict(x_train)
train_data_accuracy=accuracy_score(train_data_prediction,y_train)


# In[109]:


print(train_data_accuracy)


# In[110]:


test_data_prediction=classifier.predict(x_test)
test_data_accuracy=accuracy_score(test_data_prediction,y_test)


# In[112]:


print(test_data_accuracy)


# In[ ]:




