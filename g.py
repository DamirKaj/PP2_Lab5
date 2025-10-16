#7 Write a python program to convert snake case string to camel case string.

import re

text = input("Enter snake_case string here : ")

def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

print("camelCase:", snake_to_camel(text))
