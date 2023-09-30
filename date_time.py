#Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.
#We can again use the re module to convert the date string as shown below:

import re
def transform_date_format(date):
   return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date_input = "2023-09-17"
print(transform_date_format(date_input))

#Write a Python script to display the various Date Time formats.
#a) Current date and time
#b) Current year
#c) Month of year
#d) Week number of the year
#e) Weekday of the week
#f) Day of year
#g) Day of the month
#h) Day of week

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

#Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


