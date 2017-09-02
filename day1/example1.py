import turtle as t

t.shape('turtle')
t.bgcolor('black')
t.speed(10)
forward=100
left1=120
left2=90
#삼각형 그리기
t.color('red') # 색 추가
t.forward(forward)
t.color('orange')
t.left(left1)
t.color('orange')
t.forward(forward)
t.color('green')
t.left(left1)
t.color('yellow')
t.forward(forward)
t.color('purple')
t.left(left1)
t.color('green')

#사각형 그리기
t.forward(forward)
t.color('white')
t.left(left2)
t.color('red')
t.forward(forward)
t.color('orange')
t.left(left2)
t.color('orange')
t.forward(forward)
t.color('green')
t.left(left2)
t.color('yellow')
t.forward(forward)
t.color('purple')
t.left(left2)
t.color('green')
#원 그리기
t.color('green')
t.forward(forward/2)
t.color('white')
t.circle(forward/2)
t.color('lightblue')
t.left(9999999)