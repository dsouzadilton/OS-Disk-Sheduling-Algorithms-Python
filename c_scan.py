def CSCAN(arr, head):
	seek_count = 0
	distance = 0
	cur_track = 0
	left = []
	right = []
	seek_sequence = []
	left.append(0)
	right.append(199) 
	for i in range(len(arr)):
		if (arr[i] < head):
			left.append(arr[i])
		else:
			right.append(arr[i]) 

	left.sort()
	right.sort()

	for i in range(len(right)):
		cur_track = right[i]
		seek_sequence.append(cur_track)
		distance = abs(cur_track - head)
		seek_count += distance
		head = cur_track
	
	head = 0
	# adding seek count for head returning from 199 to 0
	seek_count += 199
	for i in range(len(left)):
		cur_track = left[i]
		seek_sequence.append(cur_track)
		distance = abs(cur_track - head)
		seek_count += distance
		head = cur_track

	print("\nTotal number of seek operations: ",seek_count)
	print("Seek Sequence is: ")
	for i in range(len(seek_sequence)):
		print(seek_sequence[i]);


requests = [ 146, 89, 45, 110, 95, 12, 43, 123, 15, 26, 93];
head_pos = 70;
print("Initial position of head:", head_pos)
CSCAN(requests, head_pos) 