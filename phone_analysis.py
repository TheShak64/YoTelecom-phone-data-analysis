#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
from datetime import datetime, time, date, timedelta
import sys 


# In[2]:


#opening csv file provided by company - may need to clean up
dfraw = pd.read_csv("phonesystem_mod.csv", usecols=np.arange(14))
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


# In[6]:


row, col = dfraw.shape
print ("row num: " + str(row) + " || col num: " + str(col))


# In[7]:


#we can use normal python string methods to extract parts of a string,
#if we suddenly get a strange format the loop will break and show an error in the data. but generally
#we assume the data is all formmatted in the same way


# In[8]:


#ok we can extract the date and time now. We need to construct the datetime object (YYYY,MM,DD,hour,min,sec)
#from the data -- we extract:year month day time 

#create new column after index col with same number of index:
dfraw["datetime"] = '' #empty col ready to transfer formatted datetime values


dt_col = dfraw["Date/Time"] # store the rows of data into this pandas series


dt_col_new = dfraw["datetime"]
i = 0


for dt_ele in dt_col:
    
    # "dt_ele" contains a string: dd/mm/yyyy hh:mm:ss <-- lets extract this
    #by looping through each point of our date/time col and extracting individual data:
    year = dt_ele[6:10]
    month = dt_ele[3:5]
    day = dt_ele[0:2]
    hour = dt_ele[11:13]
    mini = dt_ele[14:16]
    sec = dt_ele[17:21]
    
    #create a datetime object for that element
    formatted_dt = datetime(int(year),int(month),int(day),int(hour),int(mini),int(sec))

    #plug this formatted datetime value into our new col called datetime by appending.
    #as we are looping from the begining of the col
    dfraw.loc[i,"datetime"] = formatted_dt
    
    i = i + 1




# In[9]:


#drop the unformatted date/time col
del dfraw['Date/Time']
#re-arrage the cols
collist = ["datetime","Type","Dial Status","Caller Number","Called Number","Duration"]
dfraw = dfraw[collist]


# In[10]:


dfraw = dfraw.sort_values("datetime")

#we sorted the datetimes. so we know first datetime[] row is earliest and last row is latest. store these dates and print.
firstdate = dfraw.loc[0,"datetime"]
lastdate = dfraw.loc[row-1,"datetime"]
print("Date range is between {} and {}.".format(firstdate,lastdate))


# In[11]:


#### PARAMETERS ####
usr_choose_day = "30/01/2019"
param_starttime = "08:00"
param_endtime = "18:30"
#### PARAMETERS ####

#convert into datetime object
def conv2Date_nullTime (givendate):
    #expect a string in the format: dd/mm/yyyy
    thedate = datetime(int(givendate[6:10]),
                    int(givendate[3:5]),
                    int(givendate[0:2]),)
    return thedate

#check if usr given date is of format dd/mm/yyyy
try:
    usr_date = conv2Date_nullTime(usr_choose_day)
except ValueError:
    print("Date given in parameters is not of form: dd/mm/yyyy ")
    sys.exit()
    
print(usr_date)

#in our function "ckDateRng" we test if the "usr_choose_day" is within the range 
#of the dates in dfraw. we need to compare the usr_date with FirstDate however 
#firstdate includes a specific time so the function would break if a time less
#than the firstdate time is given. to overcome this issue, we use a usr_date
#that has a time right at the end of the day to ensure this is greater than the
#first date.


#firstdate_dateonly time 00:00. for the use of comparing 
#WHAT ARE WE DOING: create a new df. rows=time  col freq. add up. 
#3 codes:  single date analysis, cloud all days super imposed, 


# what are we doing?
# get a count of answered calls per 1 minute. superimpose data for each day.  
#define x-axis time params. from 8:00 - to 18:00 for examples
# create new df: time (8:00 - 18:30)  vs count
#starttime = datetime() 
#endtime =
#determine firstdate and enddate from the data.
#x = dfraw.


# In[12]:


def ckDateRng(FirstDate,LastDate,UsrDate):
    #set the dates so the time is set to 00:00 using .replace
    #if date not in rage, error is given + program exits
    #try this function and except systemexit
    print(FirstDate)
    print(LastDate)
    print(UsrDate)
    if UsrDate <= LastDate and UsrDate >= FirstDate:
        print("IN RANGE")
    else:
        sys.exit()


# In[13]:


# we want to check if our date is in range. 
#correct all dates to have same times to maintain consistancy.
usr_day_dateonly = usr_date.replace(hour=0,minute=0,second=0)
firstdate_dateonly = firstdate.replace(hour=0,minute=0,second=0)
lastdate_dateonly = lastdate.replace(hour=0,minute=0,second=0)

#check if the usr given date is within the range of dates given in our dataset
try:
    ckDateRng(firstdate,lastdate,usr_date)
except SystemExit:
    print("Hi wrong date given script stopped")

