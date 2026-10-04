from turtle import *

# we want to paint a house

#step 1:draw a square
speed(30)
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)         #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
penup()
goto(0,150)
pendown()
color("black")
begin_fill()
left(120)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(200,150)
pendown()
color("black")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


exitonclick()