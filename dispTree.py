from tkinter import *
from turtle import *
from types import *

#tree = ["Root",["B",["C",["D","E"],"F"],"G",["J", "K", "T"], "H"]]
s = 100;
startpos = (0,120)
hideturtle()
speed("fastest")

def cntstrs(list):
    return len([item for item in list if type(item) is str])

def drawtree(tree, pos, head=0):
    c = cntstrs(tree)
    while len(tree):
        goto(pos)
        item = tree.pop(0)
        if head:
            write(item,1)
            drawtree(tree.pop(0),pos)
        else:
            if type(item) is str:
                newpos = (pos[0] + s*c/4 - s*cntstrs(tree), pos[1] - s)
                down()
                goto((newpos[0], newpos[1] + 15))
                up()
                goto(newpos)
                write(item,1)
            elif type(item) is list:
                drawtree(item,newpos)

    ts = getscreen()
    ts.getcanvas().postscript(file="tree2.eps")

up()
#drawtree(tree, startpos,1)
#ts = getscreen()
#ts.getcanvas().postscript(file="tree.eps")
