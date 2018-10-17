prompt = "If you could visit one place in the world wher would you go? "

poll_go = True

places = {}

while poll_go: 
	name = input("What's your name? ")
	place = input(prompt)
	
	places[name] = place #키 값에 따옴표 필요X!!!
	go_on = input("Would you like to let another people join respond? (yes / no): ")
	
	if go_on == 'no': 
		poll_go = False
print("\n")

for name, place in places.items(): 
	print(name.title() + " want's to go " + place.title())
