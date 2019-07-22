import turtle 
turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)
#draw the E:
turtle.penup()
turtle.goto(-300,-200)
turtle.pendown()
turtle.goto(-300,-200+200)
turtle.penup()
turtle.goto(-300,200)
turtle.pendown()
turtle.goto(-300+100,200)
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()
turtle.circle(30)

turtle.mainloop()
