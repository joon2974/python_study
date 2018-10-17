favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in favorite_languages.keys(): 
	print(name.title())#for는 기본적으로 key값에 적용! keys생략 가능!!
print("\n")#순서와 상관없이 프린트!

for name in sorted(favorite_languages): 
	print(name.title() + " thank you for taking the poll.")
#소팅해서 프린트!!
print("\n")

for language in favorite_languages.values(): 
	print(language.title())
#값에 접근
print("\n")
for language in set(favorite_languages.values()): 
	print(language.title())
#중복 제거!!, set은 중복을 제거한다
