from tkinter import *

root=Tk()
e=Entry(root,width=50)
e.grid(row=4,column=0)

e1=Entry(root,width=50)
e1.grid(row=5,column=0)

root.title("last exam for Ali chegini")

def click():
    mylabel=Label(root,text="hello "+e.get())
    mylabel.grid(row=1,column=2)



def click1():
    mylabel = Label(root, text="hello " + e1.get())
    mylabel.grid(row=2, column=2)

my_button1=Button(root,text="click to see your name",padx=20,pady=20,fg="black",bg="green",command=click)
my_button1.grid(row=0,column=0)
my_button2=Button(root,text="click to see your last name",padx=20,pady=20,fg="black",bg="white",command=click1)
my_button2.grid(row=2,column=0)
my_button3=Button(root,text="Exit",padx=20,pady=20,bg="red",command=quit)
my_button3.grid(row=3,column=0)


root.mainloop()