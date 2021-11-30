def threeNumberSum(array, targetSum):
    	array.sort()
	if len(array) < 3:
		return []
	solutions = []
	for i in range(len(array)-1):
		j = i + 1
		k = len(array) -1
		while j < k and k < len(array) and j > i:
			if array[i] + array[j] + array[k] == targetSum:
				solutions.append([array[i], array[j], array[k]])
				j +=1
				k-=1
			elif array[i] + array[j] + array[k] < targetSum:
				j += 1
			else:
				k -= 1
	return solutions