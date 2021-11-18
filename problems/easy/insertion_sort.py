def insertionSort(array):
    	i = 1
	while i < len(array):
		if array[i] < array[i-1]:
			j = i
			while j > 0:
				if array[j] < array[j-1]:
					temp = array[j]
					array[j] = array[j-1]
					array[j-1] = temp
				else:
					break
				j -=1
		i += 1
	return array
