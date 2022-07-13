def SCAN(arr, head, direction):
	seek_count = 0
	distance, cur_track = 0, 0
	left = []
	right = []
	seek_sequence = []
	if (direction == "left"):
 		left.append(0)
	else:
		right.append(199)

	for i in range(len(arr)):
		if (arr[i] < head):
			left.append(arr[i])
		else:
			right.append(arr[i])
	
	left.sort()
	right.sort()
	
	a = 2
	while (a != 0):
		if (direction == "left"):
			for i in range(len(left) - 1, -1, -1):
				cur_track = left[i]
				seek_sequence.append(cur_track)
				print(cur_track)
				distance = abs(cur_track - head)
				seek_count += distance
				head = cur_track

			direction = "right"
			print("Reversing Direction. Going ",direction)

		elif (direction == "right"):
			for i in range(len(right)):
				cur_track = right[i]

				seek_sequence.append(cur_track)
				print(cur_track)
				distance = abs(cur_track - head)
				seek_count += distance
				head = cur_track
			direction = "left"
			print("Reversing Direction. Going ",direction)


		a -= 1
		
	print("\nTotal number of seek operations: ",
	seek_count)


requests = [ 146, 89, 45, 110, 95, 12, 43, 123, 15, 26, 93];
head_pos = 70;
direction = "right"

print("Initial Head Position:",head_pos,"\tDirection:",direction,"\n")
SCAN(requests, head_pos, direction) 