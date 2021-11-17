import math
def binarySearch(array, target):
    if len(array) == 0:
		return None
	mid = math.floor(len(array)-1/2)
	if array[mid] == target:
		return mid
	elif array[mid] < target:
		right = binarySearch(array[mid + 1:], target)
		if right == None:
			return -1
		else:
			return right + mid + 1
	else:
    	left = binarySearch(array[0:mid], target)
		if left != None:
			return left
		else:
			return -1