def minimumWaitingTime(queries):
    	queries.sort()
	curr_queue_time = 0
	total_waiting_time = 0
	for idx in range(len(queries)-1):
		curr_queue_time += queries[idx]
		total_waiting_time += curr_queue_time
	return total_waiting_time
    # Write your code here.
    return 0
