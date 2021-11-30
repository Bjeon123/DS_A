def isMonotonic(array):
    	if len(array) < 2:
		return True
	increasing = None
    if array[0] < array[-1]:
		increasing = True
	else:
		increasing = False
	for idx in range(len(array)-1):
		if increasing and array[idx] > array[idx + 1]:
			return False
		elif not increasing and array[idx] < array[idx + 1]:
			return False
	return True
			