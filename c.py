#3 Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

text = input("Enter a string here : ")
pattern = r'[a-z]+_[a-z]+'

matches = re.findall(pattern, text)
print("Found sequences :", matches)