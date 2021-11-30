def firstDuplicateValue(array):
    hSet = set()
	for num in array:
		if num in hSet:
			return num
		else:
			hSet.add(num)
    return -1
