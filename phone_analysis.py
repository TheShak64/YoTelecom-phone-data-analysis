#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#opening csv file provided by company - may need to clean up
dfraw = pd.read_csv("phonesystem.csv", usecols=np.arange(14))
#dfraw = dfraw.reset_index()
#store number of rows and cols
row, col = dfraw.shape
print ("row num: " + str(row) + " || col num: " + str(col))


# In[3]:


list(dfraw)


# In[4]:



#dfraw


# In[5]:


#after looking at the data we want to clean it up
#lets drop un-needed cols.
#del dfraw['Unique ID','Caller Extension','Caller Comments','Called Comments','Answering Extension','Information','Reporting Group','Report Flag']
#del dfraw['Unique ID']
del dfraw['Unique ID']
del dfraw['Caller Extension']
del dfraw['Caller Comments']
del dfraw['Called Comments']
del dfraw['Answering Extension']
del dfraw['Information']
del dfraw['Reporting Group']
del dfraw['Report Flag']


# In[6]:


row, col = dfraw.shape
print ("row num: " + str(row) + " || col num: " + str(col))


# In[7]:


dfraw.head()


# In[ ]:





# In[ ]:
