# Find all numbers in a text document and sum them

import re

file = open("sample.rtf")

total = 0
numbers = list()
for line in file:
    line = line.strip()
    if len(re.findall('[0-9]+',line))>0:
        for i in re.findall('[0-9]+',line):
            numbers.append(i)
       
for i in numbers:
    total = total + int(i)

print(total)