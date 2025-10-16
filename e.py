#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

text = input("Enter a string here: ")
pattern = r'a.*b$'

if re.fullmatch(pattern, text):
    print(" Match found!.. yra.. ")
else:
    print(" No match.. mm.. ")