#Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.
#We can again use the re module to convert the date string as shown below:

import re
def transform_date_format(date):
   return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date_input = "2023-09-17"
print(transform_date_format(date_input))



