num = int(input("Enter a number: "))

# Type Content here...
digit_sum = 0
temp_num = abs(num)
while temp_num > 0:
	digit = temp_num % 10
	digit_sum += digit
	temp_num//=10

print("Sum of digits:",digit_sum)
