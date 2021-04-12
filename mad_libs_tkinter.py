from tkinter import *
import tkinter.simpledialog, tkinter.messagebox

window = Tk()
def clicked():
    with open("story_file.txt") as file:
        for line in file:
            myList=line.split(",")
    myString = ""
    for item in myList:
        if item[0] == '&':
            try:
                neededString="Provide an example of a "+item[1:]+"\n"
                myString+=" "+ tkinter.simpledialog.askstring("Libs",neededString)
            
            except:
                print("Is something wrong?")
                return
            #input("Please provide a "+item[1:]+"\n")
        else:
            myString+= " "+item
    tkinter.messagebox.showinfo("Your Lib:",myString)
    file.close()
    
#myList = reader.rsplit(',')
#    res = "Welcome to "+txt.get()
#    lbl.configure(text=res)

    
window.geometry("500x300")
window.title("Welcome to Brian's app")

lbl = Label(window, text="Welcome to Brian's Libs")
lbl.pack()

myButton = Button(window, text = "Get a lib", command=clicked).pack()
window.mainloop()
