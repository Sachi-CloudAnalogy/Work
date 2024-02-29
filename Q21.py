#Write a Python program to extract all email addresses from a text file and write them to another file.

import re

with open("email.txt", "r") as f:
    data = f.read()
    email = re.findall("[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", data)     #return a list of matched pattern string

with open("email2.txt", "a") as f:
    for i in email:
            f.write(i)  
            f.write("\n")  