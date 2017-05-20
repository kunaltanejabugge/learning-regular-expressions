import re

file=input("enter file name: ")
hand = open(file)

sumation=list()
count=0
total=0

for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision:.*([0-9][0-9][0-9][0-9][0-9])',line)
    if len(x)>0:
        sumation = sumation + x
        count = count + 1
        
sumation = [int(i) for i in sumation]

for i in sumation:
    total = i + total

average = float(total) / float(count)

print(average) 
