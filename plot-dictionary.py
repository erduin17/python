# plot-dictionary.py
import tkinter as tk
import turtle

def main():
    #table is a dictionary
    table = {-100:0,-90:0,-80:0,-70:0,-60:0,-50:0,
                -40:0,-30:0,-20:0,-10:0,0:0,
                    10:0,20:0,30:0,40:0,50:0,
                    60:0,70:0,80:0,90:0,100:0
            }
    print(" KEYS ")
    print(table.keys())
    print(" VALUES ")
    print(table.values())
    #turtle graphics
    twin = turtle.Screen()
    twin.clear
    t = turtle.Turtle()
    #tWin = Turtle.Screen()
    for h,k in table.items(): #get the items in the dictionary
        print(h, k) #trace code
        #x,y = table[n]
        t.penup()
        t.goto(h,k)
        t.pendown()
        t.circle(5)
    twin.exitonclick()

main()
