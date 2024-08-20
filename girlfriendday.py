import turtle

def draw_layers(color, radius, y_position):
    turtle.penup()
    turtle.goto(0, y_position)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(radius)
    turtle.end_fill()
    
    
def draw_text(text, y_position, text_color):
    turtle.penup()
    turtle.goto(0, y_position)
    turtle.pendown()
    turtle.color(text_color)
    turtle.write(text, align="center", font=("Calibri", 25, "bold"))
    
screen = turtle.Screen()
screen.bgcolor("pink")

draw_layers("brown", 150, -200)
draw_text("Happy", -180, "blue")

draw_layers("lightblue", 120, -50)
draw_text("Girlfriend's", -25, "red")

draw_layers("yellow", 90, 100)
draw_text("Day", 120, "purple")

turtle.penup()
turtle.goto(0, 150)
turtle.setheading(0)
turtle.pendown()
turtle.color("red")
for _ in range(8):
    turtle.forward(70)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.backward(70)
    turtle.right(45)
    
turtle.penup()
turtle.goto(0, 250)
turtle.pendown()
turtle.color("purple")
turtle.write("code with Nick", align="center",  font=("Calibri", 12, "bold"))
 
turtle.hideturtle()
turtle.done()