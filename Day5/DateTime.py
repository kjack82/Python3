from datetime import datetime

birthday = datetime(1982, 2, 17, 21, 30)  ##this creates a date time object. 
## start with year, then month, then date in month, then hours, minutes, seconds and so on. Can change timezone too 

print(birthday.year)  #prints 1982
print(birthday.month)  #prints 2 for Feb 
print(birthday.day) #prints 17
print(birthday.weekday()) ##prints 2 which represents Wednesday as starts Monday = 0 

print(datetime.now())  #this prints the time right now 

print(datetime(2024, 6,14) - datetime(2023, 6, 14))
### can use subtraction to find difference in the days. This prints to 366 as had a leap year 

print(datetime.now() - datetime(2020, 3, 20))  ## difference between now and first day of lockdown 
##printed 1547 days, 11:11:15.34893 seconds 

##3 cannot do any other maths only subtraction 


## strptime  this takes a string and converts to a date 

parsed_date = datetime.strptime('Jan 15, 2018', '%b, %d, %y') ###  can parse dates and change the date, time etc to different formats
print(parsed_date)  ## will give a parsed result 

## strftime  means formatting strings based on a date time. Takes a time, date etc and converts to a string 

date_string = datetime.strftime(datetime.now(), '%b, %d, %y')

####

# creating date objects 
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

####

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01