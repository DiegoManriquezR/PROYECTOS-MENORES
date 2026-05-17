import turtle

win=turtle.Screen()
win.bgcolor('light yellow')
t=turtle.Turtle()

lista=[10,20,30,40,50,60,70,80,90,100]
colors=['red','blue','yellow','green','orange','brown','violet','cyan','pink','light blue']

for i in range(len(lista)):
    t.pensize(500)
    t.pencolor(colors[i])
    t.forward(lista[i]+40)
    t.shape('turtle')
    t.backward(lista[i]+40)
    t.right(30)

win.exitonclick()