from math import sqrt

for i in range(2, 10):
	if (i*(i+1)/2 % 3 != 0):
		print(i, i*(i+1)/2)




def isPrime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


def permute(nums):
	outs = []
	if len(nums) == 1:
		return [nums]

	for i in range(0, len(nums)):
		cp = permute(nums[0:i] + nums[i+1:len(nums)])
		for ccp in cp:
			outs.append([nums[i]] + ccp)
	return outs
	

def genPans(length):
	nums = range(1, length + 1)
	ps = permute(list(nums))
	outs = []
	for p in ps:
		outs.append(int(''.join([str(ai) for ai in p])))
	return outs


biggestPanPrime = 2143



for pan4 in genPans(4):
	if isPrime(pan4) and pan4 > biggestPanPrime:
		biggestPanPrime = pan4
		print(pan4)

for pan7 in genPans(7):
	if isPrime(pan7) and pan7 > biggestPanPrime:
		biggestPanPrime = pan7
		print(pan7)

print("\n\n")
print(biggestPanPrime)
