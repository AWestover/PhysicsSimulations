#NOT FINISHED

possibles = []

primes = [2, 3, 5, 7, 11, 13, 17]



def gen_all_nexts(prime1, prime2):
	nums = []
	num = 0
	while num + prime1 < 1000:
		num += prime1
		for j in range(0, 10):
			cnum = 10*(num % 100) + j
			if cnum % prime2 == 0:
				nums.append(cnum)
				print(num, cnum)
	return nums


def recursive_gen_all_things(primes):
	
	for i in range(0, len(primes)):
		clist = get_all_nexts(primes[i], primes[i+1])
