#import the turtle module and see the documentation for it
import turtle

wind= turtle.Screen()
wind.title("Ping Pong game by Naganigo")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)   # prevent the window from autoupdate itself

#madrab 1
madrab1= turtle.Turtle() #create a turtle object
madrab1.speed() #no animation take place
madrab1.shape("square")
madrab1.color("red")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-350,0)
#madrab2
madrab2= turtle.Turtle() #create a turtle object
madrab2.speed() #no animation take place
madrab2.shape("square")
madrab2.color("blue")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)
#kora
kora= turtle.Turtle() #create a turtle object
kora.speed() #no animation take place
kora.shape("square")
kora.color("white")
kora.shapesize(stretch_wid=1, stretch_len=1)
kora.penup() 
kora.goto(0,0)
kora.dx = 0.2
kora.dy = -0.2

#functions
def madrab1_up():
    y= madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab1_down():
    y= madrab1.ycor()
    y -= 20
    madrab1.sety(y)


def madrab2_up():
    y= madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y= madrab2.ycor()
    y -= 20
    madrab2.sety(y)

#keyborad bindings
wind.listen()   #tell the window to expect keyboard input
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down, "Down")


#main game loop
while True:
    wind.update()
    #move the ball
    kora.setx(kora.xcor() + kora.dx)
    kora.sety(kora.ycor()+ kora.dy)

    #Border check
    if kora.ycor() > 290:
        kora.sety(290)
        kora.dy *= -1

    if kora.ycor() < -290:
        kora.sety(-290)
        kora.dy *= -1

    if kora.xcor() > 390:
        kora.goto(0,0)
        kora.dx *=-1

    if kora.xcor() < -390:
        kora.goto(0,0)
        kora.dx *=-1

      #check if the ball hit the racket
    if (kora.xcor() > 340 and kora.xcor() <350)  and (kora.ycor() < madrab2.ycor() + 40 and kora.ycor() > madrab2.ycor() - 40):
        kora.setx(340)
        kora.dx *= -1
    if (kora.xcor() < -340 and kora.xcor() > -350)  and (kora.ycor() < madrab1.ycor() + 40 and kora.ycor() > madrab1.ycor()- 40):
        kora.setx(-340)
        kora.dx *= -1
