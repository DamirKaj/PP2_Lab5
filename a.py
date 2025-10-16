import re

text = input("Enter a string here : ")
pattern = r'ab*'

if re.fullmatch(pattern, text):
    print(" Match found")
else:
    print(" No match")