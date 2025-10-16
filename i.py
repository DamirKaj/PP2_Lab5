# 9 Write a Python program to insert spaces between words starting with capital letters.

import re

text = input("Enter a camelCase or PascalCase string here : ")
result = re.sub(r'([A-Z])', r' \1', text).strip()

print("With spaces:", result)