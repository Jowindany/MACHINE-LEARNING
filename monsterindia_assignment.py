#!/usr/bin/env python
# coding: utf-8

# In[10]:


import json
import pandas as pd
import time
from faker import Factory,Faker
import numpy as np


# In[11]:


get_ipython().system('pip install faker')


# In[12]:


pd.read_json("online-json-editor.json")


# In[13]:


with open("online-json-editor.json",encoding='utf-8') as datafile:
    for line in datafile:
        data = json.loads(line)
    ww = pd.DataFrame(data)
ww.head()    


# In[14]:


df = pd.read_json("online-json-editor.json")


# In[15]:


df.describe()


# In[16]:


get_ipython().system('pip install pandas-profiling==2.7.1')


# In[17]:


from pandas_profiling import ProfileReport


# In[18]:


ProfileReport(df)


# In[19]:


df.columns


# In[20]:


# column names had space which is not able to read in notebook so changing space to underscore


# In[21]:


# some error occured while renaming in a single command. That is why renamed each column seperately


# In[33]:


dff = df.rename(columns={'altran technologies india pvt ltd' : 'altran_technologies_india_pvt_ltd'})


# In[34]:


dff1 = dff.rename(columns={'L&T Technology Services Ltd.' : 'L&T_Technology_Services_Ltd'})


# In[35]:


dff2 = dff1.rename(columns={'Ultra-Scan Corporation' : 'Ultra-Scan_Corporation'})


# In[36]:


dff3 = dff2.rename(columns={'Adani Gas' : 'Adani_Gas'})


# In[37]:


dff4 = dff3.rename(columns={'Graphene Semiconductors' : 'Graphene_Semiconductors'})


# In[38]:


dff5 = dff4.rename(columns={'Mercedes-Benz Research and Development India' : 'Mercedes-Benz_Research_and_Development_India'})


# In[39]:


dff6 = dff5.rename(columns={'Ceat Tyres Limited' : 'Ceat_Tyres_Limited'})


# In[40]:


dff7 = dff6.rename(columns={'Global Edge Software' : 'Global_Edge_Software'})


# In[41]:


dff8 = dff7.rename(columns={'Zenith Software' : 'Zenith_Software'})


# In[42]:


dff9 = dff8.rename(columns={'Delta Power Electronics' : 'Delta_Power_Electronics'})


# In[43]:


dff10 =dff9.rename(columns={'mts technologies ltd' : 'mts_technologies_ltd'})


# In[44]:


dff11 = dff10.rename(columns={'Tech Mahindra' : 'Tech_Mahindra'})


# In[45]:


dff11.head()


# In[46]:


new_data = dff11.T


# In[47]:


new_data


# In[48]:


# exported this data to excel and worked on columns like count of employees , iit count, iit fresher count, nit count, nit fresher count, is score calculated, tire 1 college density, tire 1  college fresher density using power query & categoreized them into required category based on count. Unable to find tire 1 college strength and tire 1 college fresher strength column field in the given data.


# In[49]:


pd.read_excel("Book3.xlsx")


# In[50]:


#now working on companies they hire from seperately as it is a nested json file. parsing the data 


# In[51]:


companies_they_hire_from = new_data["companies_they_hire_from"]


# In[52]:


companies_they_hire_from


# In[53]:


new_data.companies_they_hire_from.values


# In[54]:


cn = pd.DataFrame(new_data.companies_they_hire_from.values.tolist())['company_name']


# In[55]:


kn = pd.json_normalize(cn)


# In[56]:


kn.columns


# In[57]:


kn


# In[58]:


knn = kn.T


# In[59]:


knn


# In[60]:


knc = knn.rename(columns={'0' : 'altran_technologies_india_pvt_ltd','1' : 'L&T_Technology_Services_Ltd','2' : 'Amdocs','3' : 'Xperia','4' : 'Ultra-Scan_Corporation','5' : 'Adani_Gas','6' : 'Benecke-Kaliko','7' : 'Graphene_Semiconductors','8' : 'Mercedes-Benz_Research_and_Development_India','9' : 'Ceat_Tyres_Limited','10' : 'Global_Edge_Software','11' : 'Zenith_Software','12' : 'Delta_Power_Electronics','13' : 'Siemens','14' : 'mts_technologies_ltd','15' : 'Tech_Mahindra'},inplace=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[61]:


knc


# In[62]:


#now looking on data companies where their ex employees work.


# In[63]:


companies_their_ex_employees_work = new_data["companies_where_their_ex_employees_work"]


# In[66]:


companies_their_ex_employees_work


# In[67]:


new_data.companies_their_ex_employees_work.values


# In[68]:


# unable to sort out the attribute error.


# In[69]:


new = pd.read_json("online-json-editor.json")


# In[70]:


new


# In[71]:


new = new.rename(columns={'altran technologies india pvt ltd' : 'altran_technologies_india_pvt_ltd','L&T Technology Services Ltd.' : 'L&T_Technology_Services_Ltd','Ultra-Scan Corporation' : 'Ultra-Scan_Corporation','Adani Gas' : 'Adani_Gas','Graphene Semiconductors' : 'Graphene_Semiconductors','Mercedes-Benz Research and Development India' : 'Mercedes-Benz_Research_and_Development_India','Ceat Tyres Limited' : 'Ceat_Tyres_Limited','Global Edge Software' : 'Global_Edge_Software','Zenith Software' : 'Zenith_Software','Delta Power Electronics' : 'Delta_Power_Electronics','mts technologies ltd' : 'mts_technologies_ltd','Tech Mahindra' : 'Tech_Mahindra'},inplace=True)


# In[72]:


neww = new.T


# In[73]:


neww


# In[74]:


companies_where_their_ex_employees_work = neww["companies_where_their_ex_employees_work"]


# In[75]:


companies_where_their_ex_employees_work


# In[76]:


neww.companies_where_their_ex_employees_work.values


# In[77]:


exemployee = pd.DataFrame(neww.companies_where_their_ex_employees_work.values.tolist())['company_name']


# In[78]:


# attribute error is still there unable to form a list of company names where the previous employees are working.


# In[79]:


#all the other data which i formed are categorized in excel sheet.


# In[80]:


ProfileReport(knn)


# In[ ]:





# In[ ]:




