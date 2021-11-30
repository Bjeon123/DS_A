def moveElementToEnd(array, toMove):
    	i = 0
	j = len(array) -1
	while i < j:
		if array[j] == toMove:
			j -= 1
		elif array[i] == toMove:
			temp = array[j]
			array[j] = array[i]
			array[i] = temp
		else:
			i +=1
	return array