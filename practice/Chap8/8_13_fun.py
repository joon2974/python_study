def build_profile(first, last, **user_info): 
	# ** : 빈 딕셔너리를 만들고 키-값 쌍을 모두 저장
	"""사용자에 관해 아는 것을 모두 딕셔너리로 만듬"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items(): 
		profile[key] = value
	return profile
	
my_profile = build_profile('joon', 'hwang', location='cheonan',
	field='programmer', isstudent='yes')
print(my_profile)
