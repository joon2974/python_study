height = input("How tall are you in inches? ")
height = int(height)#항상 문자열로 인식하므로 캐스팅을 해줘야함.

if height >= 36: 
	print("\nYou're tall enough to ride!")
else: 
	print("\nYou'll be able to ride when you're a little older.")
