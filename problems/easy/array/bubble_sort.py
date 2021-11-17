def bubbleSort(array):
    	sorted = False
	while not sorted:
        sorted = True
        for i in range(len(array) - 1):
			print(i)
			if array[i] > array[i+1]:
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
				sorted = False
	return array
