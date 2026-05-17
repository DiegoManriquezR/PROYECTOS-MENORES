import turtle
wn=turtle.Screen()
wn.bgcolor('black')
jose=turtle.Turtle()

lista=[10,20,30,40,50,60,70,80,90,100]
color=['yellow','red','lightgreen','orange','violet','brown','cyan','white','darkblue','grey']
for i in range(len(lista)):
    jose.pensize(4)
    jose.pencolor(color[i])
    jose.forward(lista[i])
    jose.backward(lista[i])
    jose.right(33)


    wn.exitonclick()