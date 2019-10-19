#first import datetime
import datetime


##################
#MANIPULATE A SPECIFIED DATE
##################

#'''
#assign a function call in datetime to a variable
#the "date" function always takes a date. E.g (yyyy,mm,dd)
#
mydate = datetime.date(2019,6,16)
#we can decide to use only the year/month/day value by;
#mydate.year     or mydate.month     or mydate.day
print(mydate)

#'''







##############
#MANIPULATING THE CURRENT DATE
##############

'''
#assign a function call in datetime to a variable
currentDate = datetime.date.today()

#Print the default output. Output in (yyyy-mm-dd) format
#print(currentDate)

#We can target a single value of the current date. E.g.
#print(currentDate.weekday()) #mon =0, sun =6
print(currentDate.isoweekday()) #mon=1, sun=7
'''







##############
#TIMEDELTAS
##############

'''
#Timedeltas are simply the difference between two dates or time. They are extremely useful when we want to do operations on our dates or time.

#E.g. if we want to know the date it will be after 7 days from a specific day;

today = datetime.date.today()

#specify the number of days with a keyword argument
tdelta = datetime.timedelta(days=7)

#print the date it will we in 7 days
print(today + tdelta) #we can add or subtract to get the future date or past date
'''






##############
#SOMETHING TO NOTE
##############

'''
#furtherDate = laterDate + timedeltas
#timedeltas = furtherDate - laterDate

#E.g
date1 = datetime.date(2019,6,16)
date2 = datetime.date.today()
diff = date2-date1
print(diff) # or print(diff.day)
'''





#############################
########### DATETIME.TIME
#############################

'''
#we will bw dealing with hour, minutes, seconds, and micro-seconds


##################
#MANIPULATE A SPECIFIED TIME
##################

#create a ime using the code: datetime.time(hh,mm,ss,ms)
myTime = datetime.time(4,30,0,00)
print(myTime)

#we can also do print(mytime.hour)/print(mytime.minutes)
print(myTime.minute)
'''




'''

#############################
########### DATETIME.DATETIME
#############################


#Here we get to access the date and time at onceself.
#syntax is;
#datetime.datetime(yyyy,mm,dd,hh,mm,ss,ms)
#E.g.
#dateAndTime = datetime.datetime.today()
#or
dateAndTime = datetime.datetime(1999, 6, 16, 0,0,0,0)
print(dateAndTime)


#We can also do timedeltas calculation with datetime.datetime
#E.g.
tdelta = datetime.timedelta(days=7) #or tdelta = datetime.timedelta(hours=10)
print()
'''




'''
#############################
########### .TODAY, .NOW, .UTCNOW
#############################

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()


print(dt_today)
print(dt_now)
print(dt_utcnow)
'''
