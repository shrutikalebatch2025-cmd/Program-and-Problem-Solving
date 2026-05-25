# Type Content here...
text = input()
vowels = "aeiouAIEOU"
vowel_count = 0
for char in text:
	if char in vowels:
		vowel_count +=1
print(vowel_count)
