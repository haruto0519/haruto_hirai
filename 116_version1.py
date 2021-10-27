#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
n_legs = 6
lengh = 70
angle = 360 / n_legs
spider.pensize(5)
n = 0
while (n < n_legs ):
  spider.goto(0,0)
  spider.setheading(angle*n)
  spider.forward(lengh)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()