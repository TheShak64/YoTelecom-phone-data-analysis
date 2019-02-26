#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
from datetime import datetime, time, date


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


# In[5]:


# clean up:
# split date and time into two seperate cols
#using ReGex extract the times and put into a new col?


# In[6]:


row, col = dfraw.shape
print ("row num: " + str(row) + " || col num: " + str(col))


# In[8]:


#we can use normal pything string methods to extract parts of a string, but we will use regex to make sure the data is consistant.
#if we suddenly get a strange format the loop will break and show an error in the data. but generally
#we assume the data is all formmatted in the same way


# In[9]:



#ok we can extract the date and time now we need to construct the datetime object (YYYY,MM,DD,hour,min,sec
#from data -- extract the year month etc.. *we assume it will always be in this format.

#create new column after index:
#df["datetime"] = "" #empty
def dt_convert():
    print ("heyo")
    
print ("fun dun")
#year = data[6:10]
#month = data[3:5]
#day = data[0:2]
#hour = data[11:13]zl
#mini = data[14:16]
#sec = data[17:21]

#x = datetime(int(year),int(month),int(day),int(hour),int(mini),int(sec))
#x1 = datetime(int(data1[6:10]),int(data1[3:5]),int(data1[0:2]),int(data1[11:13]),int(data1[14:16]),int(data1[17:21]))


# In[10]:


col_arr = ['Duration','Date/Time','Type','Dial Status','Caller Number','Called Number']
dfraw = dfraw[col_arr_list]
dfraw


# In[ ]:




