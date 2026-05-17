import turtle
wn=turtle.Screen()
wn.bgcolor('black')
wn.title('Carreras de tortugas')

jose=turtle.Turtle()
jose.pencolor('blue')
jose.pensize(4)
jose.stamp()
jose.shape('turtle')
angela=turtle.Turtle()
angela.pencolor('pink')
angela.pensize(4)
angela.shape('turtle')
x=True
n=0
while x==True:
    jose.left(5)
    angela.right(5)
    jose.forward(10)
    angela.forward(10)
    angela.speed(6)
    n+=1
    if n==80:
        break
jose.penup()
jose.goto(-250,0)
jose.pendown()
angela.penup()
angela.goto(250,0)
angela.pendown()   
for i in range(360):
    jose.left(1)
    angela.right(1)
    jose.forward(100)
    angela.backward(100)
    jose.backward(100)
    angela.forward(100)











wn.exitonclick()