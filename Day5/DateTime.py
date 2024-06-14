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

