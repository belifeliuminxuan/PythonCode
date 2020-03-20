# -*- coding: utf-8 -*-
# Time    : 2020/3/14 12:13
# Author  : Liu MinXuan
# Email   : liuminxuan1024@gmail.com
# File    : write1.py

#
# fd = open("test.txt", "a+")
# te = str(list(range(10000000)))
# fd.write(te)
import turtle
#太阳
turtle.color('red')
turtle.penup()
turtle.goto(250,200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.color('black','blue')
turtle.begin_fill()
#飞机
turtle.penup()
turtle.home()
turtle.pendown()
turtle.pensize(5)
turtle.goto(-300,150)
turtle.goto(100,50)
turtle.goto(0,0)
turtle.end_fill()
turtle.goto(-30,-125)
turtle.goto(-50,-50)
turtle.begin_fill()
turtle.goto(-300,150)
turtle.goto(-125,-125)
turtle.goto(-50,-50)
turtle.goto(-30,-125)
turtle.goto(-85,-85)
turtle.end_fill()
#线条
turtle.pensize(3)
turtle.penup()
turtle.goto(75,25)
turtle.pendown()
turtle.goto(200,0)
turtle.penup()
turtle.goto(50,-5)
turtle.pendown()
turtle.goto(250,-30)
turtle.penup()
turtle.goto(10,-80)
turtle.pendown()
turtle.goto(100,-150)
turtle.penup()
turtle.goto(-80,-125)
turtle.pendown()
turtle.goto(120,-200)
turtle.ht()

