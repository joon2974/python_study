person = {
	'first_name': 'joon',
	'last_name': 'hwang',
	'age': 24,
	'city': 'suwon',
	}
for inf in person.values(): 
	print(inf)
#for문도 사용가능!! keys(), values(), items()
print("\n")

fav_nums = {
	'adam': 7,
	'bred': 100,
	'charlie': 5,
	'dave': 25,
	'elice': 1000,
	}
for name, num in fav_nums.items(): 
	print(name.title() + "'s favorite number is: " + str(num))
