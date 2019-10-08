#!/usr/bin/python3
# Tron Prog0 at TU Graz SS 2019
# Name: Boris Malinic
# ===

from turtle import *
from time import *
from random import*
import math

#some global variables
livesp1 = 3
livesp2 = 3
highscore = 0
score = 0

# setup the screen with appropriate resolution and coordinate system
pg = Screen()
pg.setup(600,600,10,10)
pg.setworldcoordinates(-305,-310,320,350)
pg.bgcolor("black")
pg.title("Tron Programmieren 0 SS19")

# Game Intro code
border = Turtle() 
border.color("Lawn Green")
border.fillcolor("Light Slate Blue")
border.penup()
border.setposition(-260,-260)
border.pendown()
border.pensize(2)
border.begin_fill()
border.hideturtle()
for side in range(4):
    border.forward(520)
    border.left(90) 
border.end_fill()
pen = Turtle()	
pen.penup()
pen.color("white")
pen.hideturtle()
pen.setpos(-95,100)
pen.write("Welcome to Tron.",font=("Calibri",14))
pen.setpos(-255,60)
pen.write("Player one is green and moves with Left and Right",font=("Calibri",14))
pen.setpos(-240,30)
pen.write("Player two is yellow and moves with s and d",font=("Calibri",14))
pen.setpos(-250,0)
pen.write("You can quit the game at any time by pressing 'q'",font=("Calibri",14))
pen.setpos(-240,-70)
pen.write("Press '1' for singleplayer or '2' for multiplayer.",font=("Calibri",14))

# setting up the game for multiplayer on 2 keypress
def gamesetup():
    global pg
    global t1
    global t2
    global border
    pen.reset()
    border.reset()
    print("game started... setting up the game now")  
    pg.onkey(None, "2")	# unbind the "space"-key not trigger this function again 
    pg.onkey(None, "1")

# setting the border   
    border = Turtle() 
    border.color("cyan")
    border.penup()
    border.fillcolor("Medium Purple")
    border.setposition(-300,-300)
    border.pendown()
    border.pensize(2)
    border.hideturtle()
    border.begin_fill()
    for side in range(4):
        border.forward(600)
        border.left(90)
    border.end_fill()

# writing the additional info
    info = Turtle() 
    info.speed(0)
    info.color("Aquamarine")
    info.penup()
    info.hideturtle()
    info.goto(-80, 310)
    info.write("Lives player 2: " +str(livesp2),font=("Courier", 12, "normal"))
    info.goto(-80, 330)
    info.write("Lives player 1: " +str(livesp1),font=("Courier", 12, "normal"))

# obstacles
    obstacles = [(-280,-280),(-200,-200),(-100,-100),(100,100), (200,200),(280,280)]
    obst = Turtle()
    obst.shape("square")
    obst.shapesize(0.25,0.25)
    obst.speed(0)
    obst.pensize(1)
    obst.color("black")

    curr_x = obst.xcor()
    curr_y = obst.ycor()
        

                # pen up not to leave a trace on the board - only want the black
                # squares representing obstacles.
    obst.pu()

                # draw the obstacles by stamping the tron-bike's shape
    for i in obstacles:
        obst.setposition(i)
        obst.stamp()

                 # reset the position
    obst.setposition(curr_x,curr_y)	
    obst.color("black")   

# adding functions to be executed
    settingplayers()
    getCoordst1(t1)
    getCoordst2(t2)
    move()
    t2left() 
    t2right()
    t2down()
    left() 
    right()
    down()
    pg.update()
    pg.onkey(quit_game, "q")

# Singleplayer mode when pressed 1 on start
#########################################################
def gamesetupsp():
    global pg
    global t1
    global border
    pg.reset
    pen.reset()
    border.reset()
    print("game started... setting up the game now")  
    pg.onkey(None, "1")
    pg.onkey(None, "space")	# unbind the "space"-key not trigger this function again 

# setting the border   
    border = Turtle() 
    border.color("cyan")
    border.penup()
    border.fillcolor("Medium Purple")
    border.setposition(-300,-300)
    border.pendown()
    border.pensize(2)
    border.hideturtle()
    border.begin_fill()
    for side in range(4):
        border.forward(600)
        border.left(90)
    border.end_fill()

# writing the additional info
    info = Turtle() 
    info.speed(0)
    info.color("Aquamarine")
    info.penup()
    info.hideturtle()
    info.goto(-30, 325)
    info.write("Lives: " +str(livesp1),font=("Courier", 12, "normal"))

# obstacles
    obstacles = [(-280,-280),(-200,-200),(-100,-100),(100,100), (200,200),(280,280)]
    obst = Turtle()
    obst.shape("square")
    obst.shapesize(0.25,0.25)
    obst.speed(0)
    obst.pensize(1)
    obst.color("black")

    curr_x = obst.xcor()
    curr_y = obst.ycor()
        

                # pen up not to leave a trace on the board - only want the black
                # squares representing obstacles.
    obst.pu()

                # draw the obstacles by stamping the tron-bike's shape
    for i in obstacles:
        obst.setposition(i)
        obst.stamp()

                 # reset the position
    obst.setposition(curr_x,curr_y)	
    obst.color("black")   
    spmode()
    getCoordst1(t1)
    movesp()
    left() 
    right()
    down()
    pg.update()
    pg.onkey(quit_game, "q")

def sp():
    pg.reset()
    gamesetupsp()

def movesp():
    global t1
    global moving

    moving = True
    
    while moving:
        
        t1.forward(1)
    
        x,y = getCoordst1(t1)
        collisioncheckp1sp(x, y, t1)
        

    if livesp1 >= 1:
        pg.reset()
        end_sequencesp()

def spmode():
    global t1
    global xList
    global yList
    
    xList = []
    yList = []
   
# creates player
    t1 = Turtle()
    t1.speed(2)
    t1.penup()
    t1.backward(200) 
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.pendown()
    t1.pencolor("Lawn Green")
    t1.fillcolor("Lawn Green")

    movesp()

def collisioncheckp1sp(x,y,t1):
    global moving
    global xList
    global yList
    global livesp1
    
    # borderchecking    #used some ideas from the internet for this(upgraded them and adapted)
    if abs(x) > 299 or abs(y) > 299:
        moving = False
        livesp1 -= 1
        t1.pencolor("red")
        t1.hideturtle()
        for t in range(12):  
            t1.right(30)
            t1.forward(30)
            t1.setposition(x,y)
    # trail checking
    for i in range(len((xList))):
        if x == xList[i] and y == yList[i]: 
            moving = False
            livesp1 -= 1
            t1.pencolor("red")
            q,p = getCoordst1(t1)
            t1.hideturtle()
            # blow up animation
            for t in range(12):
                t1.right(30)
                t1.forward(30)
                t1.setposition(q,p)

    # sequences when lives = 0
    if livesp1 == 0:
        playerloss()
        scorereset()
    xList.append(x)
    yList.append(y)

def end_sequencesp():
    pg.reset()
    go = Turtle()
    go.hideturtle()
    go.penup()
    go.backward(50)
    go.pencolor("white")
    go.setpos(0,100)
    go.write("GAME OVER!",align="center",font=(14))
    go.setpos(-120,50)
    go.write("Do you want to try again? y/n",font=(14))
    pg.onkey(sp, "y")
    pg.onkey(quit_game, "n")
    pg.listen()

# Two-player functions
#########################################################
def restartgame():
    pg.reset()
    gamesetup()

def playerloss():
    pg.reset()
    resetlives()
    go = Turtle()
    go.hideturtle()
    go.penup()
    go.pencolor("red")
    go.setpos(-120,50)
    go.write("You have lost all lives!",font=(14))
    sleep(2)
def scorereset():
    info = Turtle()
    info.reset()

# when player losses lifes but wants to restart, the lives are set to default again
def resetlives():
    global livesp1
    global livesp2
    livesp1 = 3
    livesp2 = 3

# sequence when player 1 losses lives
def player1loss():
    pg.reset()
    resetlives()
    go = Turtle()
    go.hideturtle()
    go.penup()
    go.pencolor("red")
    go.setpos(0,100)
    go.write("PLAYER 1 LOST ALL LIVES!",align="center",font=(14))
    sleep(2)

# sequence when player 2 losses lives   
def player2loss():
    pg.reset()
    resetlives()
    go = Turtle()
    go.color("red")
    go.penup()
    go.pencolor("red")
    go.setpos(0,100)
    go.write("PLAYER 2 LOST ALL LIVES!",align="center",font=(14))
    sleep(2)

def quit_game(): 
    pg.bye() 

# sequence when a player dies
def end_sequence():
    go = Turtle()
    go.hideturtle()
    go.penup()
    go.backward(50)
    go.pencolor("white")
    go.setpos(0,100)
    go.write("GAME OVER!",align="center",font=(14))
    go.setpos(-120,50)
    go.write("Do you want to try again? y/n",font=(14))
    pg.onkey(restartgame, "y")
    pg.onkey(quit_game, "n")
    pg.listen()
    

# defining functions for the game(player spawns, movement, collision etc.)
def settingplayers():
    global t1
    global t2
    global xList
    global yList
    global aList
    global bList
    xList = []
    yList = []
    aList = []
    bList = []

# creates player1
    t1 = Turtle()
    t1.speed(2)
    t1.penup()
    t1.backward(200) 
    t1.left(90)
    t1.forward(50)
    t1.right(90)
    t1.pendown()
    t1.pencolor("Lawn Green")
    t1.fillcolor("Lawn Green")

# creates player2
    t2 = Turtle()
    t2.speed(2)
    t2.penup()
    t2.forward(200)
    t2.right(90)
    t2.forward(50)
    t2.right(90)
    t2.pendown()
    t2.pencolor("Yellow")
    t2.fillcolor("Yellow")
    

    move() # calling the move so that players move
	
def getCoordst1(t1):
    x = t1.xcor()   
    y = t1.ycor()   
    return x, y
def getCoordst2(t2):
    a = t2.xcor()   
    b = t2.ycor()   
    return a, b

def move():
    global t1
    global t2
    global moving

    moving = True
    
    while moving:
        
        t1.forward(1)
        t2.forward(1)

        x,y = getCoordst1(t1)
        collisioncheckp1(x, y, t1)
        a,b = getCoordst2(t2)
        collisioncheckp2(a, b, t2)

    if livesp1 >= 1 and livesp2 >= 1:
        pg.reset()
        end_sequence()
  
def collisioncheckp1(x,y,t1):
    global moving
    global xList
    global yList
    global aList
    global bList
    global livesp1
   
    
    # borderchecking    #used some ideas from the internet for this(upgraded them and adapted)
    if abs(x) > 299 or abs(y) > 299:
        moving = False
        livesp1 -= 1
        t1.pencolor("red")
        t1.hideturtle()
        for t in range(12):  
            t1.right(30)
            t1.forward(30)
            t1.setposition(x,y)
    # trail checking
    for i in range(len((xList))):
        if x == xList[i] and y == yList[i]: 
            moving = False
            livesp1 -= 1
            t1.pencolor("red")
            q,p = getCoordst1(t1)
            t1.hideturtle()
            # blow up animation
            for t in range(12):
                t1.right(30)
                t1.forward(30)
                t1.setposition(q,p)

    for i in range(len((aList))):
        if x == aList[i] and y == bList[i]: 
            moving = False
            livesp1 -= 1
            t1.pencolor("red")
            q,p = getCoordst1(t1)
            t1.hideturtle()
            #blow up animation in color of the bike that blows up 
            for t in range(12):
                t1.right(30)
                t1.forward(30)
                t1.setposition(q,p)

    # sequences when lives = 0
    if livesp1 == 0:
        player1loss()
        scorereset()
    xList.append(x)
    yList.append(y)

def collisioncheckp2(a,b,t2):
    global moving
    global aList
    global bList
    global xList
    global yList
    global livesp2

    # borderchecking
    if abs(a) > 299 or abs(b) > 299:
        moving = False
        livesp2 -= 1
        t2.pencolor("red")
        t2.hideturtle() 
        for t in range(12):
                t2.right(30)
                t2.forward(30)
                t2.setposition(a,b)
    # trail checking
    for i in range(len(aList)):   
        if a == aList[i] and b == bList[i]: 
            moving = False
            livesp2 -= 1
            q,p = getCoordst2(t2)
            t2.pencolor("red")
            t2.hideturtle()
            for t in range(12):
                t2.right(30)
                t2.forward(30)
                t2.setposition(q,p)

    for i in range(len(xList)):  
        if a == xList[i] and b == yList[i]: 
            moving = False
            q,p = getCoordst2(t2)
            t2.pencolor("red")
            t2.hideturtle()
            for t in range(12):
                t2.right(30)
                t2.forward(30)
                t2.setposition(q,p)  
    # sequences when lives = 0
    if livesp2 == 0:
        player2loss()
        scorereset()
    aList.append(a)
    bList.append(b)

# player movements
def t2right():
    global t2
    
    t2.right(90)
    t2.forward(1)

def t2left():
    global t2

    t2.left(90)
    t2.forward(1)
    
def right():
    global t1 

    t1.right(90)
    t1.forward(1)
    
def left():
    global t1

    t1.left(90)
    t1.forward(1)

def down():
    global t1
    
    t1.speed(1)
    t1.forward(0)
	

def t2down():
    global t2

    t2.speed(1)
    t2.forward(0)

# Key bindings
pg.onkey(gamesetup,"2") #bind the routine for the two-player setup to 2-key
pg.onkey(sp, "1") #bind the routine for the two-player setup to 1-key
pg.onkey(t2left, "a")
pg.onkey(t2right, "d")
pg.onkey(t2down, "s")
pg.onkey(right, "Right")
pg.onkey(left, "Left")
pg.onkey(down, "Down")
pg.onkey(quit_game, "q")
pg.listen()	# enable listening 
pg.mainloop()	# mainloop which listens to events and dispatches them

print("Until the next time!") 
