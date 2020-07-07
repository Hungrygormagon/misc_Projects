from random import randint
from tkinter import *
import tkinter as tk
import os
from os import system
import configparser
import ChaliceOfTorres_Main, Chalice_Gui, Chalice_Class


##Simulates various dice rolls
def d20_roller (self, d20Roll):
    d20Min = 1
    d20Max = 20

    d20Roll = randint(d20Min, d20Max)
    if d20Roll == 20:
        print('It\'s a critical hit! You rolled ' + str(d20Roll))
    elif d20Roll == 1:
        print('Oof, it\'s a critical miss. You rolled ' + str(d20Roll))
    else:
        print('You rolled ' + str(d20Roll))
    return d20Roll

def d12_roller (self):
    d12Min = 1
    d12Max = 12

    d12Roll = randint(d12Min, d12Max)
    print('You rolled ' + str(d12Roll))
       
def d10_roller (self):
    d10Min = 1
    d10Max = 10

    d10Roll = randint(d10Min, d10Max)
    print('You rolled ' + str(d10Roll))

def d8_roller (self):
    d8Min = 1
    d8Max = 8

    d8Roll = randint(d8Min, d8Max)
    print('You rolled ' + str(d8Roll))

def d6_roller (self):
    d6Min = 1
    d6Max = 6

    d6Roll = randint(d6Min, d6Max)
    print('You rolled ' + str(d6Roll))

def d4_roller (self):
    d4Min = 1
    d4Max = 4

    d4Roll = randint(d4Min, d4Max)
    print('You rolled ' + str(d4Roll))

def center_window(self, w, h): # pass in the tkinter frame (Master) reference and the w and h
    # get users screen width and heith
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user clicks on the 'X" to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Unsaved data will be lost. \nSave now?"):
        #This closes the app
        self.master.destroy()
        os._exit(0)


"""# Save current configuration
def saveConfig():
    global rows, cols, mines
    #configuration
    config = configparser.SafeConfigParser()
    config.add_section("game")
    config.set("game", "rows", str(rows))
    config.set("game", "cols", str(cols))
    config.set("game", "mines", str(mines))
    config.add_section("sizes")
    config.set("sizes", "amount", str(min(5,len(customsizes))))
    for x in range(0,min(5,len(customsizes))):
        config.set("sizes", "row"+str(x), str(customsizes[x][0]))
        config.set("sizes", "cols"+str(x), str(customsizes[x][1]))
        config.set("sizes", "mines"+str(x), str(customsizes[x][2]))

    with open("config.ini", "w") as file:
        config.write(file)
# Load current config
def loadConfig():
    global rows, cols, mines, customsizes
    config = configparser.SafeConfigParser()
    config.read("config.ini")
    rows = config.getint("game", "rows")
    cols = config.getint("game", "cols")
    mines = config.getint("game", "mines")
    amountofsizes = config.getint("sizes", "amount")
    for x in range(0, amountofsizes):
        customsizes.append((config.getint("sizes", "row"+str(x)), config.getint("sizes", "cols"+str(x)), config.getint("sizes", "mines"+str(x))))
"""
def onSelection(self, textBox):
    textBox.insert("Just a text Widget\nin two lines\n")
    print("Is this working")
    return textBox
    

def onAttack(self):
    d20Roll = 0
    rollValue = d20_roller(self, d20Roll)
    dmgTotal = rollValue + 
    print(dmgTotal)
    

def onRunaway(self):
    print()
def printText():
    text = "\nThis \nis \na \ntest \nof \nthe \nscroll \nbar \ndoes \nit \nwork? \nIt's so easy"
    print(text)


if __name__ == "__main__":
    pass      