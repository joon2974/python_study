users = ['admin', 'joon', 'in', 'hwang', 'park']
if users: #users가 비었는지 검사
	for user in users: 
		if user == 'admin': 
			print("Hello Admin!, would you see statement?")
		else: 
			print("Hello " + user.title() + " nice to see you again.")
else: 
	print("They should have at least a user.")
#비었다면 예외 발생
