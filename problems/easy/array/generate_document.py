def generateDocument(characters, document):
    hash_map = {}
	for char in characters:
		if not char in hash_map:
			hash_map[char] = 1
		else:
			hash_map[char] +=1
	for char in document:
		if not char in hash_map:
			return False
		else:
			if hash_map[char] > 0:
				hash_map[char] -=1
			else:
				return False
	return True