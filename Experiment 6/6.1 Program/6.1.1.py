# Type Content here...
d = int(input())
m = int(input())
y = int(input())
if y<=0:
	print("Invalid Date")
elif m<1 or m>12:
	print("Invalid Date")
else:
	leap = False
	if(y%400==0) or (y%4==0 and y%100!=0):
		leap = True
	if m in {1,3,5,7,8,10,12}:
		max_day = 31
	elif m in {4,6,9,11}:
		max_day = 30
	elif m==2:
		if leap:
			max_day = 29
		else:
			max_day = 28
	if d<1 or d>max_day:
		print("Invalid Date")
	else:
		d+=1
		if d>max_day:
			d=1
			m+=1
			if m>12:
				m = 1
				y+=1
		print(f"{d:02d}-{m:02d}-{y}")
