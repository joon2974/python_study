motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')#위랑 같은 배열

motorcycles[0] = 'ducati' #다른 언어와 같음
print(motorcycles)

motorcycles.append('city') #이어붙이기
print(motorcycles)

motorcycles.insert(0, 'kia')#뒤의 값들은 한칸씩 미뤄짐
print(motorcycles)

del motorcycles[0] #해당하는 인덱스의 값을 지움
print(motorcycles)

popped_motocycle = motorcycles.pop()#리스트를 stack으로 생각하고 맨 위에꺼를 빼옴
print(motorcycles)#맨 마지막 항목 빠진 리스트
print(popped_motocycle)#빠진 맨 마지막 항목을 출력
second_motocycle = motorcycles.pop(1)#매개인자를 주면 그 index값을 빼올 수 있음
print(motorcycles)#pop을 쓰면 그 값은 리스트에서 제거됨!!! 중요!
print(second_motocycle)

print(motorcycles)
motorcycles.remove('ducati')#값만 알고 있을 때 제거법, 같은값이 여러개면 첫항목만 제거!
print(motorcycles)

