responses = {}

#설문이 활성화됐다는 플래그
polling_active = True

while polling_active: 
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb sunday? ")
	 
	#응답을 딕셔너리에 저장
	responses[name] = response
	 
	#다른사람도 참여할지 묻는다
	repeat = input("Would you like to let another person respond? (yes / no) ")
	if repeat == 'no': 
		polling_active = False
		 
#설문 끝. 결과 출력
print("\n---Poll Results ---")
for name, response in responses.items(): 
	print(name.title() + " would like to climb " + response.title() + ".")
