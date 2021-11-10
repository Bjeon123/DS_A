def sortedSquaredArray(array):
	sol = []
	for num in array:
		sol.append(num**2)
	sol.sort()
	return sol
