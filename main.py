#!/usr/bin/env python3

import math as m
import random


helpText = '''

'''

noEval = False

while True:

    noEval = False

    x = ""

    # Take the Input as a list
    temp = input("Calculator $ ").split()
    ui = []
    for item in temp:
        if item.isdigit():
            ui.append(int(item))
        else:
            ui.append(item)

    # If Statements

    if ui[0] == "exit" or ui[0] == "stop":
        break

    if ui[0] == "help":
        noEval = True
        print(helpText)

    if ui[0] == "random":
        noEval = True
        try:
            if ui[1] < ui[2]:
                x1 = ui[1]
                x2 = ui[2]
            else:
                x1 = ui[2]
                x2 = ui[1]
            print(random.randint(x1, x2))
        except:
            print("Try again with valid numbers!                random [n1] [n2]")

    if ui[0] == "midpoint":
        noEval = True
        if len(ui) == 1:
            x1 = input("X1 $ ")
            y1 = input("Y1 $ ")
            x2 = input("X2 $ ")
            y2 = input("Y2 $ ")

            try:
                x1 = int(x1); x2 = int(x2); y1 = int(y1); y2 = int(y2)
                print("({x}, {y})".format(x = (x1 + x2)/2, y = (y1 + y2)/2))

            except:
                print("Try again with valid numbers!")

        else:
            try:
                x1 = ui[1]
                x2 = ui[3]
                y1 = ui[2]
                y2 = ui[4]
                print("({x}, {y})".format(x = (x1 + x2)/2, y = (y1 + y2)/2))
            except:
                print("Try again with valid numbers!                midpoint [x1] [y1] [x2] [y2]")

    if ui[0] == "distance":
        noEval = True
        if len(ui) == 1:
            x1 = input("X1 $ ")
            y1 = input("Y1 $ ")
            x2 = input("X2 $ ")
            y2 = input("Y2 $ ")

            try:
                x1 = int(x1); x2 = int(x2); y1 = int(y1); y2 = int(y2)
                print( abs( m.sqrt( ( (x2 - x1) ** 2) + ( (y2 - y1) ** 2) ) ))

            except:
                print("Try again with valid numbers!")

        else:
            try:
                x1 = ui[1]
                x2 = ui[3]
                y1 = ui[2]
                y2 = ui[4]
                print( abs( m.sqrt( ( (x2 - x1) ** 2) + ( (y2 - y1) ** 2) ) ) )

            except:
                print("Try again with valid numbers!                distance [x1] [y1] [x2] [y2]")

    if not noEval:
        try:
            for item in ui:
                x = x + str(item)
            print(eval(x))

        except:
            print("Please try something else")
