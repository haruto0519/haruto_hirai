import turtle as trtl
painter = trtl.Turtle()

painter.shape("circle")
painter.pensize(30)
painter.stamp()
for i in range(12):
    
    painter.pendown()
    painter.forward(30)
    painter.penup()
    painter.right(30)