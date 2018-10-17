users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': { 
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		}
	}
#딕셔너리 안에 딕셔너리를 넣음.
for username, user_info in users.items(): 
	print("\nUsername: " + username)
	full_name = user_info['first'] + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
