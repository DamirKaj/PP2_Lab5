#10 Write a Python program to convert a given camel case string to snake case.

import re

text = input("Enter a camelCase string here: ")
result = re.sub(r'([A-Z])', r'_\1', text).lower()

print("snake_case:", result)