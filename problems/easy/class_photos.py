def classPhotos(redShirtHeights, blueShirtHeights):
    	if len(redShirtHeights) != len(blueShirtHeights):
		return False
	redShirtHeights.sort()
	blueShirtHeights.sort()
	if blueShirtHeights[-1] == redShirtHeights[-1]:
		return False
	taller = taller = "red" if blueShirtHeights[-1] < redShirtHeights[-1] else "blue"
	for idx in range(len(redShirtHeights)):
		if taller == "red" and redShirtHeights[idx] < blueShirtHeights[idx]:
			return False
		elif taller == "blue" and blueShirtHeights[idx]< redShirtHeights[idx]:
			return False
		elif blueShirtHeights[0] == redShirtHeights[0]:
			return False
	return True