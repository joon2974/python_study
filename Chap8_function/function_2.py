def describe_pet(pet_name, animal_type='dog'): #위치형 매개변수, 순서 신경쓸것
	#기본값을 설정했는데 앞 매개변수 기본값있으면 뒤 매개변수도 있어야함
	"""애완동물에 관한 정보 출력"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + 
		pet_name.title() + ".")
		
describe_pet('choco', 'dog')
describe_pet('harry', 'hamster')
describe_pet(animal_type='dog', pet_name='choco')#키워드 매개변수, 순서X
describe_pet(pet_name='willie') #anumal_type은 기본값 대입
