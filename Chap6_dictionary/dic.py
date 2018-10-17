alien_0 = {} #키, 값으로 이루어짐, 빈 딕셔너리로 시작 가능
#키는 숫자, 문자열, 리스트, 다른 딕셔너리도 가능!!
alien_0['color'] = 'green'#{'color': 'green'}
alien_0['points'] = 5
print(alien_0)
print("\n")

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print("\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 25 #딕셔너리에 값 추가하는 방법!
print(alien_0)
#키-값 쌍의 순서는 중요X, 각 키-값 연결만을 중시!!
alien_0['color'] = 'yellow' #값 수정. 값추가와 방법 같음.
print(alien_0)
