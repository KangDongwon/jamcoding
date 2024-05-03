import turtle as t


def right() :
	t.setheading(0)
	t.forward(10)

def up() :
	t.setheading(90)
	t.forward(10)

def left() :
	t.setheading(180)
	t.forward(10)

def down() :
	t.setheading(270)
	t.forward(10)

def pen_up() :
	t.penup()

def pen_down():
	t.pendown()

def delete() :
	t.clear()

t.shape("turtle")
t.speed(10)

t.onkeypress(right, "Right")
t.onkeypress(up, "Up")
t.onkeypress(left, "Left")
t.onkeypress(down, "Down")
t.onkeypress(pen_up, "q")
t.onkeypress(pen_down, "w")
t.onkeypress(delete, "d")

t.listen()
t.mainloop()
