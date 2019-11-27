# awestover
# solution to project euler problem 69
# maximize n/phi(n) for n <= 1 000 000

# useful functions
import pdb


# euclidean algorithm
def gcd(a, b):
	a, b = min(a, b), max(a, b)
	while a != 0:
		a, b = b%a, a
	return b


# calculates Euler's phi function
def phi(n):
	ct = 0
	for i in range(1, n+1):
		if gcd(n, i) == 1:
			ct += 1
	return ct


# groups the same number together in an array with multiplication (grouping factors is the use here)
def group_nums(nums):
	out_nums = []
	for a_num in set(nums):
		out_nums.append(a_num**(nums.count(a_num)))
	return out_nums


# calculates phi(n) utilizing the fact that phi(a*b) = phi(a)*phi(b)  when gcd(a, b) = 1
# and our pro factoring skills, and the fact that phi(prime) = prime - 1
# and the fact that phi(prime^k) = prime^k - prime^(k-1) = prime^k(1-1/prime)
# which is true because there are prime^k numbers from 1 to prime^k
# and if we want to count how many of those are relatively prime to prime^k we note
# that prime, 2*prime, 3*prime, ... prime^k-1 * prime is the only way to get gcd(prime^k, m) not equal to 1
# there are prime^k-1 of those numbers so that is how many we must exclude from our count leaving phi as we said it
# extending this fact to numbers that are procuts of primes (every number is a produvt of primes!)
# we get phi(n) = n*prod(1-1/p) for all prime factors p of n
def fast_phi_over_n(n):
	p_fac = prime_factorization(n)
	answer = 1
	for fac in set(p_fac):
		answer *= (1-1/fac)
	return answer


# uses the result above to get phi
def fast_phi(n):
	return int(n*fast_phi_over_n(n))


# returns the prime factorization of a number
def prime_factorization(x):
	p_facs = []
	div = 1
	c = x
	while c != 1:
		div += 1
		if c % div == 0:
			p_facs.append(div)
			c = c/div
			div = 1
	return p_facs


# calculates the division that we are interested in
def quantity(n):
	return n/phi(n)


# execution
max_val = 0
achieved = 0
for n in range(1, 1000001):
	if n % 1000 == 0:
		print(n)
	c_val = 1/fast_phi_over_n(n)
	if c_val > max_val:
		max_val = c_val
		achieved = n

print("Max achieved = {}".format(max_val))
print("n = {}".format(achieved))
