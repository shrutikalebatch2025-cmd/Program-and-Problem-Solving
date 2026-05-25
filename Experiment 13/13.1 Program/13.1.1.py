 # Write your code here......
import fibonacci_module
n = int(input())

if n > 0:
	fib_series = fibonacci_module.generate_fibonacci_sequence(n)
	print(' '.join(map(str, fib_series)))
else:
	print("Please enter a positive integer")

# Write your code here.....
def generate_fibonacci_sequence(max_value):
	fib_list = []
	a,b = 0,1
	while a<= max_value:
		fib_list.append(a)
		a,b = b, a+b
	return fib_list
