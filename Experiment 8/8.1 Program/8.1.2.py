# Type Content here...
try:
	start = int(input())
	end = int(input())
	primes_found = []
	for num in range(start,end+1):
		if num>1:
			is_prime = True
			for i in range(2,int(num**0.5)+1):
				if num%i == 0:
					is_prime = False
					break
			if is_prime:
				primes_found.append(num)
	if primes_found:
		for prime in primes_found:
			print(prime)
	else:
		print("No primes")
except EOFError:
	pass
