# Koch.py
#
# Use the turtle to draw a Koch snowflake
#     https://en.wikipedia.org/wiki/Koch_snowflake
#
# Usage:
#     python snowflake [levels]
#
# Chapter 4 of Think Python!

import turtle
import sys


def edge(t: turtle, edgeLen: int, complexity: int):
    "Draw the edge of a Koch curve of a given complexity"
    if (complexity == 1):
        t.fd(edgeLen)
    else:
        "Draw four simpler edges"
        edgeLen = edgeLen // 3
        edge(t, edgeLen, complexity-1)
        t.lt(60)
        edge(t, edgeLen, complexity-1)
        t.rt(120)
        edge(t, edgeLen, complexity-1)
        t.lt(60)
        edge(t, edgeLen, complexity-1)


def snowflake(t: turtle, edgeLen: int, max: int):
    "Draw a Koch Snowflake"
    for i in range(3):
        edge(t, edgeLen, max)
        t.rt(120)


# Look for command line argument
max = 5
if (len(sys.argv) > 1):
    try:
        # Try to convert command line argument to integer
        max = int(sys.argv[1])
    except ValueError:
        max = 5

my_turtle = turtle.Turtle()

# Backup to center the image
my_turtle.penup()
my_turtle.setpos(-100, 100)
my_turtle.pendown()

# This is complicated: draw quickly
my_turtle.speed(0)

# Draw the snowflake: 243 is 3**5 - powers of 3 are best
snowflake(my_turtle, 243, max)

# Wait for user to close the window
turtle.mainloop()
