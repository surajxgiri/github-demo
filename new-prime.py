def isprime(n):
	if n ==1 :
		print(" 1 is a special case.")
		return False
		for x in range(2,n):
			if n % x == 0:
				print("Not prime number.")
				return False

			else:
				print(n, "is a prime number.")
				return True
				for n in range(1,20):
					isprime(n)