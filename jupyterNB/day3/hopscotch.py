# hopscotch.py
#
# Draw the Hopscotch Court
# Usage:
#      % python hopscotch.py
#
# Jeff Parker, June 24, 2018

import turtle

edge  = 50      # edge length of each square
width = 5       # Pen width

def square(t, edgeLen):
    "Draw a square of a given size"
    for i in range(4):
        t.fd(edgeLen)
        t.lt(90)

def climbup(t, edgeLen):
    "Move up one space, keep orientation"
    t.penup()           # Don't scribble!
    t.lt(90)
    t.fd(edgeLen)
    t.rt(90)
    t.pendown()

def stack_square(t, edgeLen):
    "Draw a square, and move turtle to upper left corner"
    square(t, edgeLen)
    climbup(t, edgeLen)

def move_half_back(t, edgeLen):
    "Take a half step to the left, keep orientation"
    t.penup()           # Don't scribble!
    t.bk(edgeLen/2)
    t.pendown()

def crossbar(t, edgeLen):
    "Draw two squares balanced over current point, and move up"

    # backup a half square
    move_half_back(t, edgeLen)

    # draw the two squares
    square(t, edgeLen)
    t.fd(edgeLen)
    square(t, edgeLen)

    # backup to our starting spot
    move_half_back(t, edgeLen)

    # Prepare for next piece
    climbup(t, edgeLen)

def hopscotch_court(t, edgeLen, penWidth):
    "Assemble a hopscotch court from our components"

    # Start turtle 200 units south to center the figure
    t.penup() 	# Don't scribble!
    t.setpos(0, -200)
    t.pendown()

    t.pensize(penWidth)

    # Draw a stack of three squares
    stack_square(t, edgeLen)
    stack_square(t, edgeLen)
    stack_square(t, edgeLen)

    # Draw the crossbars
    crossbar(t, edgeLen)
    stack_square(t, edgeLen)

    crossbar(t, edgeLen)
    stack_square(t, edgeLen)

    # Hide Turtle
    t.ht()

turt = turtle.Turtle()

hopscotch_court(turt, edge, width)

turtle.mainloop()
