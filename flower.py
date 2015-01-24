import turtle

def draw_petals(my_turtle):
	my_turtle.forward(80)
	my_turtle.right(45)
	my_turtle.forward(30)
	my_turtle.right(135)
	my_turtle.forward(30)
	my_turtle.right(45)
	my_turtle.forward(80)
	my_turtle.right(90)
	my_turtle.forward(20)

def draw_flower():
	window = turtle.Screen()
	window.bgcolor("blue")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("pink")
	brad.speed(10)
	for i in range(1, 72):
		draw_petals(brad)
		brad.right(10)
	brad.right(290)
	brad.forward(200)
draw_flower()

window.exitonclick()
