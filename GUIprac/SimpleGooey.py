from tkinter import *

def stopProg(e):        #Destroy the root window
    root.destroy()
    root = Tk()    #Create the Root Window
button1 = Button(root,text = "Hello World Click to Close")    #Create a widget, parent = root, add text
button1.pack()    #Layout Manager. Pack places widgets within the window one after another to fill space
button1.bind('<Button-1>',stopProg)     #Bind the button to an event. 
root.mainloop()                         #Loop the program and wait for events to occur 



