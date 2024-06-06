import datetime
'''
# there are 2 types of time 1 Naive and Aware 
# naive is kind of overlook and don't need any detailed info opposite is aware 
tday = datetime.date.today()
print(tday)
print(tday.year) # shows the year of the date 
print(tday.month) # shows the year of the date
print(tday.day) # shows the year of the date
print(tday.weekday()) # for this Monday =0 and Sunday = 6
print(tday.isoweekday()) # this mon = 1 and sun = 7

# deltas Are nothing but the Difference between two times 
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
#print(tday - tdelta) # 7 days before today 
#print(tday + tdelta) # 7 days after today 

# date2 = date1 + timedelta
# timedelta = date1 + date2 

bday = datetime.date(2024,6,14)
till_bday = bday - tday
print(till_bday)
print(till_bday.total_seconds()) # gives in seconds 

# ++++++++++++++++++++++++++++++++++++++++++++

# Now we will look for the time 
import time 
t = datetime.time(9,30,45,100000)
print(t)

# We can have combination of the date and time 
td = datetime.datetime(2024,6,6,12,30,45,10000)
print(td)
print(td.year)

tdelta = datetime.timedelta(days=7)
print(td + tdelta)

tdelta = datetime.timedelta(hours=12)
print(td + tdelta)
'''
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
