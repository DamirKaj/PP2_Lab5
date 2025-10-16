#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

text = input("Enter a sentence here : ")
pattern = r'[ ,.]'

result = re.sub(pattern, ':', text)
print("Result:", result)