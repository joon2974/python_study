fav_nums = {
	'adam': [7, 17],
	'bred': [100, 960],
	'charlie': [5],
	'dave': [25, 7],
	'elice': [1000],
	}
for name, nums in fav_nums.items(): 
	if len(nums) == 1: 
		print("\n" + name.title() + "'s favorite number is: " + str(nums[0]))
	else: 
		print("\n" + name.title() + "'s favorite numbers are: ")
		for num in nums: 
			print("\t" + str(num))
