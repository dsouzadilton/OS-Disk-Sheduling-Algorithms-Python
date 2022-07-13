def FCFS(arr, head):
	seek_count = 0;
	distance, cur_track = 0, 0;
	for i in range(len(arr)):
		cur_track = arr[i];
		distance = abs(cur_track - head);
		seek_count += distance;
		head = cur_track;

	print("Total number of seek operations: ", seek_count);
	print("Seek Sequence is:");
	for i in range(len(arr)):
		print(arr[i]);



requests = [ 146, 89, 45, 110, 95, 12, 43, 123, 15, 26, 93];
head_pos = 70;
FCFS(requests, head_pos);