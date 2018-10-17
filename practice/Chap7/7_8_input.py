sandwich_orders = ['bulgogi', 'pastrami' 'sanghai', 'mozarella', 'pastrami']
finished_sandwiches = []

print("pastrami is sold out!")
while sandwich_orders: 
	while 'pastrami' in sandwich_orders: 
		sandwich_orders.remove('pastrami')
	
	sandwich = sandwich_orders.pop()
	print(sandwich + " is maked.")
	finished_sandwiches.append(sandwich)

print("\n---maked sandwiches---")
for sandwich in finished_sandwiches: 
	print(sandwich)
