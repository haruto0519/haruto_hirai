import turtle as t

t.pensize(2021)
t.forward(1)
t.backward(1)
list = ["limegreen", "yellow", "orange", "red", "magenta", "blue"]

def spirograph():
    t.pensize(5)
    t.speed(0)
    for i in range(12):
        for color in list:
            t.color(color)
            t.circle(120)
            t.right(5)



t.penup()
t.goto(0,0)
t.pendown()
spirograph()




wn = t.Screen()
wn.mainloop()