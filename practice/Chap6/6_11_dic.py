cities = {
	'seoul': {
		'population': 10000000,
		'country': 'korea',
		'capital': True,
		},
	'london': {
		'population': 5000000,
		'country': 'england',
		'capital': True,
		},
	'newyork': {
		'population': 3000000,
		'country': 'usa',
		'capital': False,
		},
	}
	
for city, city_info in cities.items(): 
	print("\n" + city.title() + " is city of " + 
	city_info['country'].title() + " and there live " + 
	str(city_info['population']) + " people.") 
	if city_info['capital'] == True: 
		print(city.title() + " is capital of " + 
		city_info['country'].title())
	else: 
		print(city.title() + " is not capital of " + 
		city_info['country'].title())
	
