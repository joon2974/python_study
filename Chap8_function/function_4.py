def greet_users(names): 
	"""리스트 각 사용자에게 단순한 환영 인사 출력"""
	for name in names: 
		msg = "Hello, " + name.title() + "!"
		print(msg)
		
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print("\n")

#--------------------------------------------------------------------

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs: 
	current_design = unprinted_designs.pop()
	
	print("Printing model: " + current_design)
	completed_models.append(current_design)
	
print("\nThe following models have been printed: ")
for completed_model in completed_models: 
	print(completed_model)
