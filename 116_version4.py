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
  spider.setheading(angle*n + 22.5)
  spider.forward(lengh)
  n = n + 1




spider.penup()
spider.goto(-10,-17)
spider.pendown()
spider.fillcolor("red")
spider.begin_fill()
spider.circle(8)
spider.goto(15,-17)
spider.circle(8)
spider.end_fill()

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()