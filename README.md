# Phone Data Analysis using data from Yo-Telecom
Analysis of incoming and outgoing calls to gain insight into any issues 


The purpose of this project is to analyze phone data and gain insight to identify issues and suggest improvements. Fortunately, the phone company in use (YoTelecom) provides its users with an interface to view all incoming and outgoing calls. They even have nice colourful visualisations showing number of calls and abandoned calls every 3 hours. This is useful however there is a wealth of information hidden within the data dumps. 
The motivation for this project is to uncover:
- why so many customers are complaining that they can’t get through to the call centre
- to view the answered calls on a daily basis
- to visualize true incoming calls and true abandoned calls.

After comparing the data dump with day-to-day operations, I personally don’t consider a call duration of say 5 seconds to be considered as an abandoned called, rather the customer being impatient or unable to continue with the call. Those people who wait for a reasonable amount of time before they hang up over frustration are the real abandoned callers. Further study of the data showed these interesting "failed capacity" callers. These are customers who fail to connect due to lack of capacity at the side of the call center. This to me is a worrying collection of data that is not made aware to us at the call center. An analysis of this is carried out as well. 

There are three python scripts:
- (1) Single day view of incoming calls
- (2) Average number of calls taken on a day-to-day basis across many days
- (3) failed capacity analysis showing unique individuals attempting and failing to connect until they finally get through.

A sample of the data visualisation is given in fig 1,2,3 respectively.

The Python Pandas library was used with matplotlib

