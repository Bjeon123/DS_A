def arrayOfProducts(array):
    	solutionArr = []
    for i in range(len(array)):
		currProduct = 1
		for j in range(len(array)):
			if i != j:
				currProduct *= array[j]
		solutionArr.append(currProduct)
	return solutionArr