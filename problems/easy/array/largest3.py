def findThreeLargestNumbers(array):
    largest3 = [None,None,None]
	for num in array:
		if largest3[0] == None:
			largest3[0] = num
		elif largest3[1] == None:
			largest3[1] = num
		elif largest3[2] == None:
			largest3[2] = num
		else:
			largest3.sort()
			if num > largest3[0]:
				largest3[0] = num
	largest3.sort()
	return largest3
