def print_models(unprinted_designs, completed_models): 
	"""
	남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트합니다.
	출력한 각 디자인을 completed_models로 옮깁니다.
	"""
	while unprinted_designs: 
		current_design = unprinted_designs.pop()
		
		#디자인에서 3D 출력 시뮬레이트
		
		print("Printing model: " + current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models): 
	"""출력이 끝난 모델 표시"""
	print("\nThe following models have been printed: ")
	for completed_model in completed_models: 
		print(completed_model)
		
unprinted_designs = ['iphone case' ,'galaxy case', 'robot']
completed_models = []
print_models(unprinted_designs, completed_models)
#unprinted_designs[:]을 전달하면 원래 리스트를 유지할 수 있음.
show_completed_models(completed_models)
