import turtle

turtle.speed(500)
turtle.bgcolor("black")
turtle.pensize(10)

def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

def write_love_message():
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.color("yellow")
    turtle.write("I Love You", align="left", font=("Arial", 24, "normal"))

turtle.color("white", "red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
func()
turtle.left(140)
func()
turtle.forward(111.65)
turtle.end_fill()

write_love_message()

turtle.hideturtle()
turtle.done()
turtle.penup()
turtle.hideturtle()

