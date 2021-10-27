import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

x = -200
while (x < 200): 
  x = x + 50
  y = 200
  painter.goto(-y,x)
  painter.color("purple")
  painter.stamp()

  while (y > 0):
     y = y - 50
     painter.goto(-y,x)
     painter.color("orange")
     painter.stamp()

wn = trtl.Screen()
wn.mainloop()