import turtle

def draw_square():
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed(3)
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

	jake = turtle.Turtle()
	jake.color("yellow")
	jake.triangle(120)

	window.exitonclick()

draw_art()