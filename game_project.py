
#-----import statements-----
import random as rand
import turtle as trtl
spot = trtl.Turtle()
import turtle as score_writter

spot.showturtle()
spot.shape("circle")
spot.shapesize(2)
spot.color("red")
spot.speed(8)
score = 0

#def update_score():
    




def clicked(x, y):
    score =+ 1
    new_xpo = rand.randint(-380,380)
    new_ypo = rand.randint(-280,280)
    spot.penup()
    spot.goto(new_xpo, new_ypo) 
    #update_score
    spot.pendown()




spot.onclick(clicked)

#-----game configuration----


#-----initialize turtle-----


#-----game functions--------


#-----events----------------


wn = trtl.Screen()
wn.mainloop()