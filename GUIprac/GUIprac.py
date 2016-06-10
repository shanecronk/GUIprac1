
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

    #Method for INITIALIZATIONS    
    def initialize(self):   #Initializations are going to take place here for every GUI created
                            #This is a Layout Manager
        self.grid()         #Grid used for determining where to place containers (Objects like buttons)

        #ADDING TEXT ENTRY
        self.entryVariable = tkinter.StringVar()
        #Create the Widget
        self.entry = tkinter.Entry(self,textvariable = self.entryVariable)                
        self.entry.grid(column=0,row=1,sticky='EW')     #Assign the Widget to the Grid location based on column and row
        self.entry.bind("<Return>",self.OnPressEnter)   #On ENTER press
        self.entryVariable.set(u"Enter Text Here:")     #Set the entry variable to a string

        #ADDING A BUTTON
        #Note, we do not need to keep a reference to the button because we will not be reading or altering its value
        button = tkinter.Button(self,text = u"Click me !",command=self.OnButtonClick)#On BUTTON click

        button.grid(column=1,row=1)

        self.labelVariable = tkinter.StringVar()

        
        #ADDING THE LABEL
        #Use the LABEL object in tkinter
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

        self.entry.focus_set()                              #This will auto select the text box for new text entry
        self.entry.select_range(0,tkinter.END)
    
    #Method for a BUTTON CLICK
    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get()+" (You clicked the button!)")   #Change the label to display what happened 
        print ("You Clicked The Button! ")
        self.entry.focus_set()
        self.entry.select_range(0,tkinter.END)
    
    #Method for a ENTER PRESS    
    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get()+"(You pressed ENTER!)")        #Change the label to display what happened 
        print("You Pressed Enter!")
        self.entry.focus_set()
        self.entry.select_range(0,tkinter.END)




if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('My Created Application')
    app.geometry("270x100")
    app.mainloop()
