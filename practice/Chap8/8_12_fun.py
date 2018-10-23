def sandwich_veg(*veg_list): 
	for veg in veg_list: 
		print(veg + ' ', end='')
	print("\n")
		
sandwich_veg('eggs', 'bacon')
sandwich_veg('watermelon')
sandwich_veg('ham', 'bacon', 'sosage', 'eggs')
