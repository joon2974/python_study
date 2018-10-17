people = []

person = {
	'first_name': 'joon',
	'last_name': 'hwang',
	'age': 24,
	'city': 'suwon',
	}
people.append(person)
person = {
	'first_name': 'in',
	'last_name': 'park',
	'age': 24,
	'city': 'seoul',
	}
people.append(person)
person = {
	'first_name': 'jeong',
	'last_name': 'oh',
	'age': 23,
	'city': 'seoul',
	}
people.append(person)
	

for person in people: 
	name = person['first_name'] +  " " + person['last_name']
	age = person['age']
	city = person['city']
	print(name + "'s age is " + str(age) + " and he live in " + 
		city)
