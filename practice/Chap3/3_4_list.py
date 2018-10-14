invite_dinner = ['froyo', 'gingerbread', 'lollipop', 'icecream']
print("Hello "+ invite_dinner[0] + " let's join dinner with me!")
print("Hello "+ invite_dinner[1] + " let's join dinner with me!")
print("Hello "+ invite_dinner[2] + " let's join dinner with me!")
print("Hello "+ invite_dinner[3] + " let's join dinner with me!")
print("\n")

#한명 불참. 참가인원 바꾸기
cannot_join = invite_dinner.pop(1)#pop하면 제거됨!
print(cannot_join+" can't join us.")
invite_dinner.insert(1, 'kiwi')
print(invite_dinner)
print("\n")

#자리가 더 나서 사람 추가
invite_dinner.insert(0,'americano')
invite_dinner.insert(2, 'cafelatte')
invite_dinner.append('coffee')
print(invite_dinner)
print("The number of invited people is "+str(len(invite_dinner)))
print("\n")

#자리가 2자리로 줄었음
print('We can invite only two people. sorry.')
pop_1 = invite_dinner.pop()
print(pop_1+" Sorry.")
pop_2 = invite_dinner.pop()
print(pop_2+" Sorry.")
pop_3 = invite_dinner.pop()
print(pop_3+" Sorry.")
pop_4 = invite_dinner.pop()
print(pop_4+" Sorry.")
pop_5 = invite_dinner.pop()
print(pop_5+" Sorry.")
print(invite_dinner)
print(invite_dinner[0]+", "+invite_dinner[1]+" can join us.")
del invite_dinner[0]
del invite_dinner[0]
print(invite_dinner)
