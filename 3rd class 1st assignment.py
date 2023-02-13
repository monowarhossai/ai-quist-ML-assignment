#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
import gspread


# In[2]:


import pandas as pd
import gspread


# In[3]:


gc = gspread.service_account(filename="C:\\Users\\hp\\Downloads\\my-1st-project-377705-037084bca848.json")


# In[4]:


gc


# In[6]:


sheet= gc.open_by_url("https://docs.google.com/spreadsheets/d/1NzPnI-u0uvwZJo1NK_XJzNTMPz5IExAS4J_cR1ykZ9o/edit?usp=sharing")


# In[7]:


sheet


# In[8]:


ws = sheet.worksheet('emp1')


# In[9]:


ws


# In[10]:


df = pd.DataFrame(ws.get_all_records())


# In[11]:


df


# In[12]:


ws2 = sheet.worksheet('emp2')
df2 = pd.DataFrame(ws2.get_all_records())
df2


# In[15]:


ws3 = sheet.worksheet('emp3')


# In[16]:


ws3


# In[29]:


df = pd.DataFrame(ws.get_all_records())
df


# In[ ]:




