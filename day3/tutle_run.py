import turtle as t
import random

te=t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

ts=t.Turtle()#먹이 (초록 동그라미)
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right(): #우측으로 방향 전환
    t.setheading(0)
def turn_up(): #위로 방향 전환
    t.setheading(90)
def turn_left(): #좌측으로 방향 전환
    t.setheading(180)
def turn_down(): #아래로 방향 전환
    t.setheading(270)

def play():#게임시작함수
    t.forward(10)#주인공 거북이 10만큼 앞으로 이동
    ang=te.towards(t.pos())
    te.setheading(ang)#악당 거북이 방향을 주인
    te.forward(5)#악당 거북이 9만큼 앞으로
    if t.distance(ts)<12:#주인공과 악어사이 거리
        start_x=random.randint(-230,230)
        start_y=random.randint(-230,230)
        ts.goto(start_x,start_y)#먹이를 다른곳으로 옮김
    if t.distance(te)>=12:#주인공과 악당 거리
        t.ontimer(play,100)#0.1초후 play함수 실행
t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle") # "거북이 모양"의 커서를 사용합니다
t.speed(0) # 거북이 속도를 가장 빠르게 지정합니다
t.up()
t.color("white")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.listen() #거북이 그래픽 창이 키보드 입력을 받도록 함
play() # play 함수를 호출해서 게임을 시작합니다.

t.mainloop()


