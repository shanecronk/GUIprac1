"""The Purpose Of This Class is to Create a new GUI environment for User LOGIN and REGISTRATION.
This will be done by using (tkinter)
Author : Shane Cronk
Date : 6/9/2016
"""

import sys
import tkinter
from tkinter import *

###################################################################################
#           This class will create a default GUI with basic initializations       #
#           tkinter.Tk is the module used within tkinter                          #
###################################################################################
class CreateGooey(tkinter.Tk):
    #The __init__ method to begin the object creation with initial values
    def __init__(self,parent):
        #The 'constructor' in python. Used to set class initializations for 'CreateGooey'
        tkinter.Tk.__init__(self,parent)

        self.parent = parent    #Keep a reference point for parent of any object
        self._initialize()       #Initialize the GUI
    #_initialize is used to set initial characteristics of the GUI
    def _initialize(self):
        ############################################################
        #    WINDOW SIZE AND POSITIONING AND LAYOUT                #
        #                                                          #
        ############################################################

        self.grid()             #Grid is the Layout Manager. Location is based on Column and Row values

        #ENABLE RESIZING OF WINDOW
        self.grid_columnconfigure(0,weight=1)       #Allows windows to resize but maintains button size
        #ADDING CONSTRAINT...No Vertical Resizing!
        self.resizable(True,False)

        self.update()
        self.geometry(self.geometry())      #Prevents window from resizing constantly based on text entered.
        
        ############################################################
        #                   ADDING LABEL                           #
        #                                                          #
        ############################################################

        #Foreground color, background color
        #anchor=w means text is left aligned in label
        #textvariable = custom entered string
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable = self.labelVariable, anchor ="w", fg ="white", bg="blue") 
        label.grid(column=0,row=0, columnspan=2,sticky='EW')
        self.labelVariable.set(u"Welcome To The Login Environment!")



        ############################################################
        #           TEXT BOX CREATION                              #
        #                                                          #
        ############################################################

        #ADDING USERNAME TEXT ENTRY
        self.uNameVar = tkinter.StringVar()
        #Create the 'Entry' widget for USERNAME
        self.uName = tkinter.Entry(self, textvariable = self.uNameVar)
        #Assign the weidget to the Grid Location
        self.uName.grid(column = 0, row = 0,sticky = 'EW')
        #Bind the widget to a EVENT
        self.uName.bind("<Return>",self.OnEnterPress)   #The event occurs when ENTER is pressed
        #Set the string variable for the uName widget
        self.uName.set("USER NAME: ")

        #ADDING PASS TEXT ENTRY
        self.uPassVar = tkinter.StringVar()
        #Create the 'Entry' widget for PASS
        self.uPass = tkinter.Entry(self,textvariable = self.uPassVar)
        #GRID
        self.uPass.grid(column = 0,row = 1, sticky = 'EW')
        #BIND EVENT
        self.uPass.bind("<Return>",self.OnButtonClick)
        #Set String Variable for uPASS
        self.uPass.set("PASSWORD: ")


       

#########################################################################################
#       EVENT HANDLING GOES BELOW THIS LINE                                             #
#                                                                                       #
#########################################################################################

def onButtonClick(self):
    print ("You clicked the button!")

def onEnterPress(self):
    print ("You pressed enter!")




#########################################################################################
#       Main Program/Execution                                                          #
#                                                                                       #
#########################################################################################

Goo = CreateGooey(None)
Goo.title('User Page')
Goo.geometry("270x200")
Goo.mainloop()



