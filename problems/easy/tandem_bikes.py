def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    	if fastest == True:
		num_bikes = len(redShirtSpeeds)
		red_and_blue = redShirtSpeeds + blueShirtSpeeds
		red_and_blue.sort()
		return sum(red_and_blue[-num_bikes:])
	else:
		total = 0
		redShirtSpeeds.sort()
		blueShirtSpeeds.sort()
		for idx in range(len(redShirtSpeeds)):
			if redShirtSpeeds[idx] > blueShirtSpeeds[idx]:
				total += redShirtSpeeds[idx]
			else:
				total += blueShirtSpeeds[idx]
		return total