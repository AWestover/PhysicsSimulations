# solves the coin problem 


# { goal: {numcoins: number of ways} }
memorized_stuff = {0: {1: 1}}

def numWays(coinVals, goal, numCoins):
	if goal == 0:
		return 1
	elif numCoins == 0 or goal < 0: #and goal != 0 #(which is obvious because of the elif)
		return 0
	else:
		try:
			return memorized_stuff[goal][numCoins]
		except KeyError:
			withLastCoin = numWays(coinVals, goal, numCoins - 1)
			withoutLastCoin = numWays(coinVals, goal - coinVals[numCoins - 1], numCoins)
			answer = withLastCoin + withoutLastCoin
			try:
				memorized_stuff[goal][numCoins] = answer
			except KeyError:
				memorized_stuff[goal] = {}
				memorized_stuff[goal][numCoins] = answer
			# either you do not use the coin (numCoins -= 1) or you do (goal -= coinVals[numCoins - 1])
			return memorized_stuff[goal][numCoins]	
	
coinVals = [1, 2, 5, 10, 20, 50, 100, 200]
goal = 975
print(numWays(coinVals, goal, len(coinVals)))

