import turtle
window = turtle.Screen()
window.bgcolor('white')
pen = turtle.Turtle()
pen.speed(10)
penSize = 10
pen.pensize(penSize)
radiusOuter = 300
pen.up()
pen.goto(0,-(radiusOuter))
pen.down()
pen.circle(radiusOuter)
pen.up()
pen.pensize(5)
pen.goto(0,0)
pen.down()
for j in range(10):
	pen.begin_fill()  
	pen.right(360/10)
	pen.color('black')
	for i in range(4):
		pen.forward(210)
		pen.left(90)
	pen.end_fill()


pen.up()
pen.goto(0,-220)
pen.down()
pen.color("black")
pen.fillcolor("white")
pen.begin_fill()
pen.circle(220)
pen.end_fill()
pen.up()
pen.pensize(5)
pen.goto(0,0)
pen.down()

pen.up()
pen.goto(0,-200)
pen.down()
pen.color("black")
pen.fillcolor("white")
pen.begin_fill()
pen.circle(200)
pen.end_fill()
pen.color('black')

pen.up()
pen.goto(0,0)
pen.down()

for j in range(8):
	pen.begin_fill()  
	pen.right(360/8)
	pen.color('black')
	for i in range(8):
		pen.forward(75)
		pen.left(360/8)
	pen.end_fill()

pen.up()
pen.goto(0,0)
pen.down()

pen.color('black')
pen.fillcolor('white')
pen.up()
pen.goto(0,-150)
pen.down()
pen.begin_fill()
pen.circle(150)
pen.end_fill()

pen.up()
pen.goto(0,0)
pen.down()
pen.color("black")
pen.fillcolor("white")
for j in range(8):
    pen.begin_fill()
    pen.goto(0,0) 
    pen.right(360/8)
    for i in range(8):
        pen.begin_fill()
        pen.forward(50)
        pen.left(360/8)
        pen.end_fill()
    pen.end_fill()
    pen.goto(0,0)

pen.hideturtle()
turtle.exitonclick()  