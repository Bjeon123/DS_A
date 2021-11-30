def productSum(array, depth = 1):
    prodSum = 0
	for data in array:
		if isinstance(data, int):
			prodSum += data
		else:
			prodSum += productSum(data, depth + 1)
	return prodSum * depth