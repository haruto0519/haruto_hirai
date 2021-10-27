#Make spider body
import turtle as trtl
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#configure legs
n_legs = 8
lengh = 70
angle = 360 / n_legs
spider.pensize(5)
n = 0
#make legs
while (n < n_legs ):
  spider.goto(0,20)
  spider.setheading(angle*n)
  spider.forward(lengh)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()