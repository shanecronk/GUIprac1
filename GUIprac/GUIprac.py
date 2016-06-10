
import sys
import tkinter
from tkinter import *
#Ensure the correct file is being imported. We want (C:\tkinter\__init__.py)
print()
print("""The imported file is: """)
print(tkinter.__file__)

#The simple class for Tkinter
class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        #The "constructor" in this class, Python does not have actual constructors
        tkinter.Tk.__init__(self,parent)
        #Every GUI is a hierchy of objects. Ex...A window might contain 2 buttons. The window is the parent of those buttons.
        
        #It is a good habit to keep a reference point for the parent of any object
        #This allows objects to be altered and still have a reference to the original form of the object
        self.parent = parent

        #Intialize the GUI
        self.initialize()
    ################################################################################################
    #       Method for INITIALIZATIONS    
    #       Initializations are going to take place here for every GUI created
    #       This is a Layout Manager
    #       Grid used for determining where to place containers (Objects like buttons)
    #################################################################################################
    
    
    
    def initialize(self):
        self.grid()         
        #############################################################################
        #           ADDING TEXT ENTRY
        #
        #############################################################################
        self.uNameVar = tkinter.StringVar()
        #Create the Widget
        self.uName = tkinter.Entry(self,textvariable = self.uNameVar)                
        self.uName.grid(column=0,row=1,sticky='EW')     #Assign the Widget to the Grid location based on column and row
        self.uName.bind("<Return>",self.OnPressEnter)   #On ENTER press
        self.uNameVar.set(u"Login: ")     #Set the entry variable to a string


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

        ############################################################################
        #       ADDING A BUTTON
        #       Note, we do not need to keep a reference to the button because 
        #       we will not be reading or altering its value
        #############################################################################

        button = tkinter.Button(self,text = u"Click me !",command=self.OnButtonClick)#On BUTTON click
        button.grid(column=1,row=1)

        #############################################################################
        #           ADDING THE LABEL
        #           Use the LABEL object in tkinter
        ##############################################################################
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable = self.labelVariable, anchor ="w", fg ="white", bg="blue") #Foreground color, background color
                                                                        #anchor=w means text is left aligned in label
                                                                        #textvariable = custom entered string
        label.grid(column=0,row=0, columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello!")
        
        #ENABLE RESIZING
        self.grid_columnconfigure(0,weight=1)               #Allows the window to be resized but maintain the format of the boxes and buttons
        #ADDING CONSTRAINT
        self.resizable(True,False)                          #Prevents the vertical resizing of the window

        self.update()
        self.geometry(self.geometry())                      #Prevents window from resizing constantly based on text entered

        self.uName.focus_set()                              #This will auto select the text box for new text entry
        self.uName.select_range(0,tkinter.END)
    
    #Method for a BUTTON CLICK
    def OnButtonClick(self):
        self.labelVariable.set(self.uNameVar.get()+" (You clicked the button!)")   #Change the label to display what happened 
        print ("You Clicked The Button! ")
        self.uName.focus_set()
        self.uName.select_range(0,tkinter.END)
    
    #Method for a ENTER PRESS    
    def OnPressEnter(self,event):
        self.labelVariable.set(self.uNameVar.get()+"(You pressed ENTER!)")        #Change the label to display what happened 
        print("You Pressed Enter!")
        self.uName.focus_set()
        self.uName.select_range(0,tkinter.END)




if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Login Application')
    app.geometry("270x100")
    app.mainloop()
