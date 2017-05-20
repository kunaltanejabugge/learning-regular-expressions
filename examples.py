import re 

#search for lines that start with 'From'
file = open("mbox-short.txt")
for line in file:
    line = line.rstrip()
    if re.search('^From:',line):
        print(line)
        
        
# Search for lines that start with 'F', followed by 
# 2 characters, followed by 'm:'
file = open("mbox-short.txt")
for line in file:
    line = line.rstrip()
    if re.search('^F..m:',line):
        print(line)
        
# Search for lines that start with From and have an at sign
file = open("mbox-short.txt")
for line in file:
    line = line.rstrip()
    if re.search('^From:.+@',line):
        print(line)

#we are looking for substrings that have at least one non-whitespace character, 
#followed by an at-sign, followed by at least one more non-whitespace character. The “\S+” matches as many non-whitespace characters as possible.        
s = 'A message from kunaltanejabugge@gmail.com to kunaltaneja60@gmail.com @2PM'
ls = re.findall('\S+@\S+',s)
print(ls)


# Search for lines that have an at sign between characters
file = open("mbox-short.txt")
for line in file:
    line = line.rstrip()
    if len(re.findall('\S+@\S+',line))>0:
        print(re.findall('\S+@\S+',line))

# Search for lines that have an at sign between characters # The characters must be a letter or number
file = open("mbox-short.txt")
for line in file:
    line = line.rstrip()
    if len(re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]',line))>0:
        print(re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]',line))



# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
hand = open('mbox-short.txt') 
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
        
# Search for lines that start with 'X' followed by any # non whitespace characters and ':' followed by a space # and any number. The number can include a decimal.
# Then print the number if it is greater than zero. import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line) 
    if len(x) > 0:
        print(x)
        
# Search for lines that start with 'Details: rev=' # followed by numbers and '.'
# Then print the number if it is greater than zero import re
hand = open('mbox-short.txt') 
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line) 
    if len(x) > 0:
        print(x)

# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':' # Then print the number if it is greater than zero
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line) 
    if len(x) > 0: 
        print(x)
        
import re
hand = open('mbox-short.txt')
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
