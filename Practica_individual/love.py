import turtle

turtle.penup()
turtle.hideturtle()

def write_love_message():
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.write("I Love You", align="left", font=("Arial", 24, "normal"))

write_love_message()

turtle.exitonclick()
