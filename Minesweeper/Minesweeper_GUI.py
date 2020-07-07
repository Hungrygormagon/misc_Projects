#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Version: 3.7.5
#
# Author: Steven J. Carney
#
# File: Mineswepper_TKinter.py
#
# Tested OS: This code is known to work on WIndows 10
#


from tkinter import *
from tkinter import messagebox as tkMessagebox
from collections import deque
import random
import platform
import time
from datetime import time, date, datetime
import os
#import Minesweeper_Main


size_X = 10
size_Y = 10

stateDefault = 0
stateClicked = 1
stateFlagged = 2

btnClick = "<Button-1>"
btnFlag = "<Button-2>" if platform.system() == 'Darwin' else "<Button-3>"

window = None

class Minesweeper:
    def __init__(self, tk):
        #import images
        self.images = {
            'plain': PhotoImage(file = "img\\tile_plain.png"),
            'clicked': PhotoImage(file = "img\\tile_clicked.png"),
            'mine': PhotoImage(file = "img\\tile_mine.png"),
            'flag': PhotoImage(file = "img\\tile_wrong.png"),
            "numbers": []
        }
        #impores numbered tiles using conditional
        for i in range(1, 9):
            self.images["numbers"].append(PhotoImage(file = 'img\\tile_'+str(i)+".gif"))

        #sets up frame
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        #set up labels/UI
        self.labels = {
            "time": Label(self.frame, text = "00:00:00"),
            "mines": Label(self.frame, text = "Mines: 0"),
            "flags": Label(self.frame, text = "Flags: 0")
        }

        self.labels["time"].grid(row = 0, column = 0, columnspan = size_Y) #Top full width
        self.labels["mines"].gird(row = size_X+1, column = 0, columnspan = size_Y/2)
        self.labels["flags"].grid(row = size_X+1, column = size_Y/2-1, columnspan=size_Y/2)

        self.restart() #Starts game
        self.updateTimer() #initializes timer

def Main():
    # create Tk instance
    window = Tk()
    # set program title
    window.title("Minesweeper")
    # create game instance
    minesweeper = Minesweeper(window)
    # run event loop
    window.mainloop()

if __name__ == "__main__":
    Main()
