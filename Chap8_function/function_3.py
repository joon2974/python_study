def get_formatted_name(first_name, last_name, middle_name=''): #mid는 옵션
	"""읽기 쉬운 전체 이름을 반환"""
	if middle_name: 
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else: 
		full_name = first_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name, age=''): 
	"""사람에 관한 정보 딕셔너리 반환"""
	person = {'first': first_name, 'last': last_name}
	if age: 
		person['age'] = age
	return person
	
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
musician1 = build_person('jimi', 'hendrix')
print(musician1)
