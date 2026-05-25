# Write your code here...
a,b,c,d = map(int,input().split())
total_marks = a+b+c+d
per = (total_marks/4)
print(total_marks)
percentage = f"{per:.2f}"
print(percentage)
if(per>75):
	print("Distinction")
elif(per>=60 and per<75):
	print("First Division")
elif(per>=50 and per<60):
	print("Second Division")
elif(per>=40 and per<50):
	print("Third Division")
else:
	print("Fail")

