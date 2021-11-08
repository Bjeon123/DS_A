def twoNumberSum(array, targetSum):
    s = set()
    for num in array:
	    if (targetSum - num) in s:
		    return [num, targetSum - num]
	    else:
		    s.add(num)
    return []
