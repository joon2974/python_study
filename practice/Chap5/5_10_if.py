current_users = ['adam', 'bred', 'charlie', 'dave', 'elice']
new_users = ['charlie', 'valencia', 'pogba', 'martial', 'elice']

current_users_lower = [user.lower() for user in current_users]#!!!!!

for new_user in new_users: 
	if new_user.lower() in current_users_lower: 
		print("You have to need another name.")
	else: 
		print("You can use that name.")
