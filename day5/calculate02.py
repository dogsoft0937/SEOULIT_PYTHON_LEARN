class Calculator :
    result=0
    def __init__(self): #생성자 함수
        self.result=0 #result값 0으로 초기화
    def adder(self, num):
        self.result+=num
        return self.result
    def subtractor(self,num):
        self.result-=num
        return self.result
calculator01=Calculator()
calculator02=Calculator()
calculator03=Calculator()

print(calculator01.adder(100))
print(calculator01.adder(28))

print(calculator02.adder(200))
print(calculator02.adder(2500))

print(calculator03.adder(500))
print(calculator03.subtractor(200))