# Type Content here...
input_string = input()
result = ""
for char in input_string:
	if char.isalnum() or char.isspace():
		result += char
print(result)
