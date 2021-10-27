#-----import statements-----
import random as rand
import turtle as trtl
spot = trtl.Turtle()
import turtle as score_writter


wn = trtl.Screen()
wn.addshape('halloween_picture.gif')
trtl.shape('halloween_picture.gif')



spot.speed(8)
score = 0


    




def clicked(x, y):
    score =+ 1
    new_xpo = rand.randint(-300,300)
    new_ypo = rand.randint(-250,250)
    spot.penup()
    spot.goto(new_xpo, new_ypo) 
    #update_score
    spot.pendown()




spot.onclick(clicked)

wn.addshape('bats.gif_picture.gif')
spot == trtl.shape('bats.gif_picture.gif')
wn.mainloop()