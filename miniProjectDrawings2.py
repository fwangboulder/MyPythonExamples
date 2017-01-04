import turtle
def draw_rhombus(some_turtle,length,angle):
    for i in range(1,3):
        some_turtle.forward(length)
        some_turtle.left(180-angle)
        some_turtle.forward(length)
        some_turtle.left(angle)
def draw_shapes():
    window=turtle.Screen()
    window.bgcolor("pink")
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("purple")
    angie.speed(0)
    for i in range(1,73):
        draw_rhombus(angie,100,140)
        angie.right(5)
    angie.right(90)
    angie.forward(300)
    angie.right(150)
    draw_rhombus(angie,150,140)
    angie.right(100)
    draw_rhombus(angie,150,140)
    angie.hideturtle()
    window.exitonclick()
draw_shapes()
