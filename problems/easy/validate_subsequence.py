def isValidSubsequence(array, sequence):
    i = 0;
    for num in array:
	    if i == len(sequence):
		    return True
	    if sequence[i] == num:
		    i +=1
    return i == len(sequence)
