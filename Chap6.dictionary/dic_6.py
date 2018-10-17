pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}#딕셔너리 안에 리스트 넣기

print("You ordered a " + pizza['crust'] + "-crust pizza" + 
	" with the following toppings: ")
for topping in pizza['toppings']: 
	print("\t" + topping)

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name, languages in favorite_languages.items(): 
	if len(languages) == 1: #좋아하는 언어가 1개면 다르게 출력
		print("\n" + name.title() + "'s favorite language is: " + 
			languages[0].title())
	else: 
		print("\n" + name.title() + "'s favorite languages ara:")
		for language in languages: 
				print("\t" + language.title())
	
