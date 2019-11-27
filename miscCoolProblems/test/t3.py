# turns out a circular prime is not just all permutations,
#it is  acutally rotations...


# yo this works but prime cheking funciton is real sketch

from math import sqrt

def pfac(n):
	pfacs = [1]
	if n >= 1:
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
		return 0

	return pfacs


def primeProhibitivelySlow(n):
	return len(pfac(n)) == 2

def prime(n):
	if n == 1:
		return False
	for i in range(2, 1 + int (sqrt(n))):
		if n % i == 0:
			return False
	return True


def circular_prime(n):
	digs = list(str(n))
	combos = perms(digs)
	for perm in combos:
		num = int(''.join(perm))
		if not prime(num):
			return False
	return True

def legit_circular_prime(n):
		for rot in rotations(n):
			if not prime(rot):
				return False
		return True

def rotations(num):
	digs = list(str(num))
	combos = []
	for i in range(0, len(digs)):
		last = digs.pop(0)
		digs = digs + [last]
		combos.append(int(''.join(digs)))
	return combos


def perms(alist):
	outlist = []
	if len(alist) == 1:
		return [alist]
	else:
		for i in range(0, len(alist)):
			clist = perms(alist[0:i] + alist[ i+1 : len(alist) ] )
			for cel in clist:
				curAdd = [alist[i]]
				for caddd in cel:
					curAdd.append(caddd)
				outlist.append(curAdd)
		return outlist


ct = 0
for i in range(2, 10**6):
	if legit_circular_prime(i):
		ct += 1
		print(i)
	if i % 1000 == 0:
		print(i)

print(ct)
