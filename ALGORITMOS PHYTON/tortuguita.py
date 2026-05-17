import turtle
wn=turtle.Screen()
wn.bgcolor('lightblue')

jose=turtle.Turtle()
jose.pencolor('red')
jose.pensize(4)
jose.stamp()

for i in range (50):
    jose.right(30)
    jose.forward(150)
    jose.left(5)
    jose.backward(150)
    if i==30:
        jose.penup()
        jose.goto(200,-200)
        jose.pendown()
        for j in range(3):
            jose.pencolor('blue')
            jose.right(120)
            jose.forward(120)

wn.exitonclick()