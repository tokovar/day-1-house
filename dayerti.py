from turtle import*

#house structure 
#---------------#
width(5)

color("blue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#door
#---------------#
width(5)

left(90)
forward(75)
left(90)
color("purple")
forward (80)
right(90)
forward(50)
right(90)
forward(80)

#roof
#---------------#
fillcolor("red")
color("red")
width(5)
penup()
goto(200, 200) #<--------- position
pendown()

left(215) #<---------- side #1
forward (170)
left(108)
forward (170)
fillcolor("red")




exitonclick()


