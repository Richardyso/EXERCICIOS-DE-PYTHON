import turtle

wn = turtle.Screen()
bird = turtle.Turtle()
bird.speed(10)
bird.pensize(1)
bird.color("OliveDrab")
bird.setpos(-50, 0)
bird.fillcolor("red")


bird.begin_fill()
for i in [0, 1, 2]:
    bird.forward(175)
    bird.left(120)
bird.end_fill()


bird.forward(25)
bird.right(90)

bird.fillcolor("black")
bird.begin_fill()

for i in [0, 1, 2]:
    bird.fd(125)
    bird.left(90)

bird.end_fill()

bird.penup()
bird.fd(62.5)
bird.left(90)
bird.forward(25)
bird.right(90)

bird.pendown()
bird.color("Black")

bird.fillcolor("green")

bird.begin_fill()
bird.circle(15, 360)
bird.end_fill()
bird.hideturtle()

wn.exitonclick()
