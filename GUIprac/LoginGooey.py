###############################################################################################
#LoginGooey.py The Purpose Of This Class is to Create a new GUI environment                   #
#for User LOGIN and REGISTRATION                                                              #
#This will be done by using (tkinter)                                                         #
#Author : Shane Cronk                                                                         #
#Date : 6/9/2016                                                                              #
###############################################################################################

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
           
        self._initialize() #Initialize the GUI
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
        #           TEXT BOX CREATION                              #
        #                                                          #
        ############################################################

        #ADDING USERNAME TEXT ENTRY
        self.uNameVar = tkinter.StringVar()
        #Create the 'Entry' widget for USERNAME
        self.uName = tkinter.Entry(self, textvariable = self.uNameVar)
        #Assign the weidget to the Grid Location
        self.uName.grid(column = 0, row = 1,sticky = 'EW')
        #Bind the widget to a EVENT
        self.uName.bind("<Return>",self.OnPressEnter)   #The event occurs when ENTER is pressed
        #Set the string variable for the uName widget
        self.uNameVar.set("USER NAME: ")

        #ADDING PASS TEXT ENTRY
        self.uPassVar = tkinter.StringVar()
        #Create the 'Entry' widget for PASS
        self.uPass = tkinter.Entry(self,textvariable = self.uPassVar)
        #GRID
        self.uPass.grid(column = 0,row = 2, sticky = 'EW')
        #BIND EVENT
        self.uPass.bind("<Return>",self.OnPressEnter)
        #Set String Variable for uPASS
        self.uPassVar.set("PASSWORD: ")

        ##############################################################
        #           ADDING THE BUTTONS                               #
        #                                                            #
        ##############################################################
        
        #Note I used a reference to the original button with 'self.submitButton'
        #This is not required becase we will not be using the button value for anything
        #The button simply preforms an EVENT when it is clicked. 

        self.submitButton = tkinter.Button(self,text = u"SUBMIT",command=self.OnButtonClick)
        self.submitButton.grid(column=1,row=1)

        self.resetButton = tkinter.Button(self,text = u"RESET",command=self.OnButtonClick)
        self.resetButton.grid(column = 1,row = 2)

        #############################################################
        #                   ADDING LABEL                            #
        #                                                           #
        #############################################################

        #Foreground color, background color
        #anchor=w means text is left aligned in label
        #textvariable = custom entered string
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable = self.labelVariable, anchor ="w", fg ="white", bg="blue") 
        label.grid(column=0,row=0, columnspan=2,sticky='EW')
        self.labelVariable.set(u"Welcome To The Login Environment!")



        

#########################################################################################
#       EVENT HANDLING GOES BELOW THIS LINE                                             #
#                                                                                       #
#########################################################################################

    def onButtonClickSub(self):
        print ("You clicked the button!")

    def onButtonClickRes(self):
        print("You reset the fields")

    def onEnterPress(self,event):
        print ("You pressed enter!")


    def OnPressEnter(self,event):
        self.labelVariable.set(self.uNameVar.get()+"(You pressed ENTER!)")        #Change the label to display what happened 
        print("You Pressed Enter!")
        self._writeFile()
        self._readFile()
        
        self.uName.focus_set()
        self.uName.select_range(0,tkinter.END)


    def OnButtonClick(self):
        self.labelVariable.set(self.uNameVar.get()+" (You clicked the button!)")   #Change the label to display what happened 
        print ("You Clicked The Button! ")
        self.uName.focus_set()
        self.uName.select_range(0,tkinter.END)
 
#########################################################################################
#       WRITING AND READING TO/FROM A FILE                                              #
#                                                                                       #
#########################################################################################   

    def toString(self):
        self.toString = str(self)
        return self.toString

    def unString(self):
        self.unString = self
        return self.unString

    def _writeFile(self):
        #self.toString()
        filename = input("Please input a filename: ")
        with open("filename","a") as out_file:
            out_file.write(self.uNameVar.get()) #Prints actual username that is in the file
        #self.unString()
        

    def _readFile(self):
        #self.toString()
        filename = input("Reading file...Please input a filename: ")
        with open("filename","rt") as in_file:
            in_file.read(int(self.uNameVar.get()))
        #self.unString()
        print(self.uNameVar.get())


#########################################################################################
#       Main Program/Execution                                                          #
#                                                                                       #
#########################################################################################


if __name__ == "__main__":
    Goo = CreateGooey(None)
    Goo.title('User Page')
    Goo.geometry("470x200")
    
    Goo.mainloop()








