from tkinter import *
import tkinter as tk
#from PIL import imageTK, Image
import Chalice_Fun
import ChaliceOfTorres_Main, Chalice_Class


def load_GUI(self):
    playerType = "Testing this"
    npcType = "Also testing this"
    textOutput = "\nThis \nis \na \ntest \nof \nthe \nscroll \nbar \ndoes \nit \nwork? \nIt's so easy"
    #Labels for Player icons
    self.lbl_npc = tk.Label(self.master, text= "NPC: "+ npcType) #Labels the image for current npx
    self.lbl_npc.grid(row=2, column=1, columnspan = 2, padx=(10, 10), pady=(10,10), sticky=N+W)
    self.lbl_npcStats = tk.Label(self.master, text= "npcStats") #Labels stats for the current NPC
    self.lbl_npcStats.grid(row=5, column=1, columnspan = 2, padx=(10, 10), pady=(10,10), sticky=N+W)

    self.lbl_pcStats = tk.Label(self.master, text= "pcStats") #labels stats for the layer
    self.lbl_pcStats.grid(row=9, column=1, columnspan = 2, padx=(10, 10), pady=(10,10), sticky=N+W)

    self.lbl_input = tk.Label(self.master, text="Enter selection here:") #Labels the input box to make a selection
    self.lbl_input.grid(row=11, column=1, padx=(10, 10), pady=(10, 10), sticky=W)

    # input box for player to make selections
    self.text_input = tk.Entry(self.master, text= "")
    self.text_input.grid(row=11, column=2, columnspan=5, padx=(10, 10), pady=(10, 10), sticky=W)

   # Textbox to display text
    self.scrollbar1 = Scrollbar(self.master, orient= VERTICAL)
    self.textBox = Text(self.master, exportselection= 0, yscrollcommand= self.scrollbar1.set)
    #self.textBox.bind('<<ListboxSelect>>', lambda event: Chalice_Fun.onSelection(self, event))
    self.scrollbar1.config(command= self.textBox.yview)
    self.scrollbar1.grid(row=12, column=9, rowspan=4, columnspan=1, padx=(0,10), pady=(10,10), sticky=N+E+S)
    self.textBox.grid(row=12, column=1, rowspan=4, columnspan=8, padx=(10,0), pady=(10,10), sticky= N+E+S+W)
    self.textBox.configure(state='disabled') # Makes textbox uneditable by the user

    # Adds buttons for the Player to perform actions
    self.btn_Select = tk.Button(self.master, width=5, height=1, text="Enter", command=lambda: Chalice_Fun.onSelection(self, self.textBox))
    self.btn_Select.grid(row=11, column=6, padx=(10,10), pady=(10, 10), sticky=W)

    self.btn_Attack = tk.Button(self.master, width=5, height=1, text="Attack", command=lambda: Chalice_Fun.onAttack(self))
    self.btn_Attack.grid(row=9, column=7, padx=(15,0), pady=(45, 10), sticky=W)    

    self.btn_Run = tk.Button(self.master, width=5, height=1, text="Run", command=lambda: Chalice_Fun.onRunaway(self))
    self.btn_Run.grid(row=9, column=8, padx=(15,0), pady=(45, 10), sticky=W)

    self.btn_Roll = tk.Button(self.master, width=5, height=1, text="Roll", command=lambda: Chalice_Fun.d20_roller(self))
    self.btn_Roll.grid(row=9, column=9, padx=(15,0), pady=(45, 10), sticky=W)

#    self.btn_Save = tk.Button(self.master, width=5, height=1, text="Save", command=lambda: ChaliceOfTorres_Main.save_file(self, whatever=None))
#    self.btn_Save.grid(row=10, column=9, padx=(15,0), pady=(45, 10), sticky=W)

#    self.btn_Open = tk.Button(self.master, width=5, height=1, text="Open", command=lambda: ChaliceOfTorres_Main.open_file(self, whatever=None))
#    self.btn_Open.grid(row=11, column=9, padx=(15,0), pady=(45, 10), sticky=W)
   
"""def load_gui(self):
    self.lbl_fname = tk.Label(self.master, text= "First Name: ")
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)



    self.txt_fname = tk.Entry(self.master, text= "")
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)


    # Defining the listbox with a scrollbar 
    self.scrollbar1 = Scrollbar(self.master, orient= VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection= 0, yscrollcommand= self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: Phonebook_Func.onSelect(self, event))
    self.scrollbar1.config(command= self.lstList1.yview)
    self.scrollbar1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky= N+E+S+W)

    self.btn_add = tk.Button(self.master, width=12, height=2, text="Add", command=lambda: Phonebook_Func.addToList(self))
    self.btn_add.grid(row=8, column=0, padx=(25,0), pady=(45, 10), sticky=W)
    self.btn_update = tk.Button(self.master, width=12, height=2, text="Update", command=lambda: Phonebook_Func.onUpdate(self))
    self.btn_update.grid(row=8, column=1, padx=(15,0), pady=(45, 10), sticky=W)    
    self.btn_delete = tk.Button(self.master, width=12, height=2, text="Delete", command=lambda: Phonebook_Func.onDelete(self))
    self.btn_delete.grid(row=8, column=2, padx=(15,0), pady=(45, 10), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text="Close", command=lambda: Phonebook_Func.ask_quit(self))
    self.btn_close.grid(row=8, column=4, columnspan= 1, padx=(15,0), pady=(45, 10), sticky=E)

    Phonebook_Func.create_db(self)
    Phonebook_Func.onRefresh(self)"""



if __name__ == "__main__":
    pass