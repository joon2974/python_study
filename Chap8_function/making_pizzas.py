#import pizza
#from pizza import *
#pizza모듈의 모든 함수를 임포트, 점표기법 안써도 됨
from pizza import make_pizza as mp  #함수만 임포트, 점표기법 안써도 됨!
#as는 함수 별칭, 모듈에도 별칭을 사용할 수 있다
#make_pizza 그대로 사용 가능
#pizza.py 모듈을 임포트

#pizza.make_pizza(16, 'pepperoni') 모듈 전체를 임포트 했을 때
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
