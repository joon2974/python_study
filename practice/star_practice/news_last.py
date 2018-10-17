apart = [[101, 102, 103, 104], [201, 202, 203, 204], 
	[301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]
can_read = []

for line in apart: 
	for room in line: 
		if room in arrears: 
			print(str(room) + " room can't read newspapers.")
		else: 
			can_read.append(room)

print("\nThese rooms can read newspapers: ")
for room in can_read: 
	print(str(room) + " ", end='')
