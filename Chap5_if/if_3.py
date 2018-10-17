requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if requested_toppings: #항목이 최소한 하나 있으면 True를 반환!!
	for requested_topping in requested_toppings: 
		if requested_topping == 'green peppers': 
			print("Sorry we are out of green peppers right now.")
		else: 
			print("Adding " + requested_topping + ".")
else: 
	print("Are you sure you want a plain pizza?")
print("\nFinished making your pizza!")
