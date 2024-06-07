import datetime

# there are 2 types of time 1 Naive and Aware 
# naive is kind of overlook and don't need any detailed info opposite is aware 

'''
# there are 2 types of time 1 Naive and Aware 
# naive is kind of overlook and don't need any detailed info opposite is aware 

tday = datetime.date.today()
print(tday)

print(tday.year) # shows the
=====================
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

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow) # it is also not a time aware 

# we have explicitly made the timezone 
# pip install pytz 
# The standard library has the timezone class for handling the fixed offset and timezone.utc as UTC timezobe instance. 
import pytz 
dt = datetime.datetime(2024,7,27,12,30,45,tzinfo=pytz.UTC)
print(dt)

#dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
#print(dt_utcnow)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now) # it is timezone aware at last + 

dt_mytime = dt_now.astimezone(pytz.timezone('ASIA/kolkata'))
print(dt_mytime)


# to see all the timezones 
for tz in pytz.all_timezones:
    print(tz)
'''
'''
import pytz
dt_now = datetime.datetime.now(tz=pytz.UTC)
#print(dt_now) # it is timezone aware at last + 

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn= mtn_tz.localize(dt_mtn)
print(dt_mtn)


dt_east = dt_mtn.astimezone(pytz.timezone('Asia/kolkata'))
print(dt_east)

'''
import pytz 

dt_mtn = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
print(dt_mtn.strftime('%B %d,%Y')) # searchg format codes for the dates and print it out

#opposite is if you have datetime and you want to do it into datetime 

dt_str = 'June 14, 2024'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime -- datetime to string 
# strptime -- string to datetime 
