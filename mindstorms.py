import turtle

def draw_square(my_turtle):
	for i in range(1, 5):
		my_turtle.forward(100)
		my_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("blue")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	for i in range(1, 100):
		draw_square(brad)
		brad.right(5)

draw_art()

window.exitonclick()
