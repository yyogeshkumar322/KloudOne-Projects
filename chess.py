import turtle
turtle.bgcolor("orange")
def Board(color):
    i = 0
    turtle.begin_fill()
    turtle.down()
    turtle.color(color)
    while i< 4:
        turtle.forward(40)
        turtle.left(90)
        i += 1
    turtle.up() 
    turtle.end_fill()
def tforward():
    turtle.forward(40)
def horizon(value):
    if(value):
        for i in range(0, 8):
            if(i > 0 and i % 2 != 0):
                tforward()
                Board("white")
            if(i > 0 and i % 2 == 0):
                tforward()
                Board("black")
            if(i == 0):
                Board("black")
    else:
        for i in range(0, 8):
            if(i > 0 and i % 2 != 0):
                tforward()
                Board("black")
            if(i> 0 and i% 2 == 0):
                tforward()
                Board("white")
            if(horizon == 0):
                Board("white")

for j in range(0, 8):
    turtle.setx(0)
    turtle.sety(40 * j)
    if(j % 2 == 0):
        horizon(value=True)
    else:
        horizon(value=False)

turtle.setx(0)
turtle.sety(0)
turtle.done()
