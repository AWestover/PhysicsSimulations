def pfac(n):
	if n >= 1:
		pfacs = [1]
		ct = 2
		while n > 1:
			if n%ct == 0:
				n = n/ct
				pfacs.append(ct)
				ct = 2
			else:
				ct += 1
	else:
		print("Eh thats not really relavent")

	return pfacs


def isPerfect(n):
	return sum(pfac(n)) == 2*n

while True:
	n = int(input("n"))
	print(isPerfect(n))
