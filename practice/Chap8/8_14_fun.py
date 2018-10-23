def make_car(name, model, **options): 
	car_info = {}
	car_info['name'] = name
	car_info['model'] = model
	for key, value in options.items(): 
		car_info[key] = value
	return car_info
	
car = make_car('subaru', 'outback', color='blue', tow_package='true')
h_car = make_car('hyundai', 'santafe', color='silver')
h_car['tow_package'] = 'true'
print(car)
print(h_car)
