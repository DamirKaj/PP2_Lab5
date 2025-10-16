#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

text = input("Enter a string here : ")
pattern = r'ab{2,3}'

if re.fullmatch(pattern, text):
    print(" Match found! ")
else:
    print(" No match. ")