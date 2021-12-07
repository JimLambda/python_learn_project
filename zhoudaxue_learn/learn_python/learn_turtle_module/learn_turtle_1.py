import turtle

# turtle.setup(400, 600, 100, 200)
# turtle.screensize(400, 600, 'red')
# turtle.screensize(400, 600, '#4D41D8')

# t = turtle.Turtle()
# t.pensize(10)
# t.pencolor('#B6B8E1')
# t.speed(1)
# for i in range(10):
#     t.forward(i * 5)
#     # t.left(90)
#     t.lt(90)
#     t.goto(100, 100)
# t.penup()
# t.goto(-100, 100)
# t.pendown()
# t.goto(100, 100)

t = turtle.Turtle()
t.pensize(10)
t.pencolor('#B6B8E1')
t.speed(8)

# t.setheading(170)
# t.seth(-60)
# t.circle(100, steps=10)

t.fillcolor('#B6B2A2')
# t.begin_fill()
# t.circle(100)
# t.end_fill()

t.begin_fill()
t.left(240)
t.forward(100)
t.left(120)
t.forward(100)
t.left(130)
t.forward(100)
t.end_fill()

turtle.Screen().exitonclick()
