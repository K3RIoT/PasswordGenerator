import random
from tkinter import *

uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "[]{}!@#$%^&*()_-+=:;/.,`~"

class PasswordGeneratorGUI:
    
    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x80+100+100")
        self.root.resizable(0,0)
        self.root.title("Random Password Generator")

        #Button
        self.btn=Button(self.root,text="Generate")
        self.btn.pack()
        self.btn.place(x=620,y=42)
        self.btn.config(command=self.generate)

        #Button
        self.btn=Button(self.root,text="Copy")
        self.btn.pack()
        self.btn.place(x=570,y=42)
        self.btn.config(command=self.copy)
        
        #Entry
        self.entry = Entry(self.root,state='readonly', font=("arial",15),width=200)        
        var = StringVar()
        var.set('Password')
        self.entry.config(textvariable=var, relief='flat')
        self.entry.pack()
        self.entry.place(x=10,y=20)

        #Spinbox
        self.spin=Spinbox(self.root,width=3,from_=10,to =50,font=("arial",17),state='readonly')
        self.spin.pack()
        self.spin.place(x=620,y=6)
      
    def mainLoop(self):
        self.root.mainloop()

    def generate(self):
        all = uppers+lowers+numbers+symbols
        length = int(self.spin.get())
        var = StringVar()
        password = "".join(random.sample(all,length))
        var.set(password)
        self.entry.config(textvariable=var,relief='flat')
    
    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.entry.get())
        self.root.update()    
        
def main():    
    myPasswordGeneratorGUI = PasswordGeneratorGUI()
    myPasswordGeneratorGUI.mainLoop()


if __name__ == "__main__":
    main()
