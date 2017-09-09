import turtle as t

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)
def polygon2(n,a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)

polygon(3)#삼각형
polygon(5)#오각형
polygon(7)#7각형
polygon(9)#9각형
polygon(11)#11각형

t.up()
t.forward(150)
t.down()
polygon2(3,75)
polygon2(5,100)