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

for i in range(1, 20):
	print(pfac(i))


bigNumsPfac = []
bigNum = 1

for i in range(1, 20):
	cPfac = pfac(i)
	for j in range(0, len(cPfac)):
		needed = cPfac.count(cPfac[j])
		have = bigNumsPfac.count(cPfac[j])
		
		print(needed, have)

		if needed > have:

			for k in range (0, needed - have):
				bigNumsPfac.append(cPfac[j])
				bigNum *= cPfac[j]
print(bigNumsPfac, bigNum)
