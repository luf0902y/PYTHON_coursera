"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
C_hour = []
D_hour ={}
lst=[]
for line in handle:
	if line.startswith('From '):
		word = line.split()
		time = word[5]
		hour = time.split(':')
		hour = hour[0]
		C_hour.append(hour)
		
	else:
		continue
for hr in C_hour:
	D_hour[hr] = D_hour.get(hr,0) + 1
for key,val in D_hour.items():
	lst.append((key,val))
	lst.sort()
for a,b in lst:
	print a,b
