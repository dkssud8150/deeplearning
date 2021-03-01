# 자료형 데이터
## 자료형
type(10) # int 정수
type(2.718) # float 실수
type("hello") # str 문자열형

# - 파이썬 -> 동적 언어 => 변수의 자료형을 상황에 맞게 자동으로 결정하는 것. 즉, 변수 x에 숫자를 저장하면 자동으로 int형태임을 판단한다.





class Man:
    def __init__(self,name):
        self.name = name
        print("initialized")
    
    def hello(self):
        print("Hello " + self,name + "!")
    
    def goodbye(self):
        print("goodbye " + self.name + "!")

    
m = Man("David")
m.hello()
m.goodbye()





