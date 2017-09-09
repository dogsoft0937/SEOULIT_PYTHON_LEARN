import turtle as t
def turn_right(): # 오른쪽으로 이동하는 함수
    t.setheading(0) #t.seth(0) 가능
    t.forward(10) #t.fd(10) 가능
    
def turn_up(): # 위로 이동하는 함수
    t.setheading(90)
    t.forward(10)
def turn_down():  # 아래로 이동하는 함수
    t.setheading(-90)
    t.backward(-10)
def turn_left():
    t.setheading(180) #왼쪽으로 이동하는 함수
    t.forward(10)
def blank():
    t.clear()

t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(blank,"Escape")
t.listen()
t.mainloop()