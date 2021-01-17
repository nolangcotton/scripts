#!/usr/local/bin/python3
import os
import re

'''
Good work on unzipping the file!
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-####
Use the Python os module and regular expressions to iterate through each file
, open it, and search for a telephone number.
Good luck!
'''

phone_num_reg  = re.compile(r'\d{3}-\d{3}-\d{4}')

for root,dirs,files in os.walk('/Users/nolancotton/Desktop/dev/python/test/extracted_content'):
    for file_name in files:
        full_file_name= root + '/' + file_name
        file_handle = open(full_file_name, 'r+')
        for LINE in file_handle:
            if re.findall(phone_num_reg, LINE):
                res = re.search(phone_num_reg, LINE)
                print(res.group())
