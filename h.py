#8 Write a Python program to split a string at uppercase letters.

import re

text = input("Enter a string here: ")
result = re.split(r'(?=[A-Z])', text)

print("Split result:", [s for s in result if s])