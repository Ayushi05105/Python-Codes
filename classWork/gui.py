from tkinter import *
root =Tk()
def on_button_click():
    label2.config(text="Hello" + e.get())
Label1 =Label(root,text="Enter Name:")
e = Entry(root,width=50,borderwidth=5)

myButton = Button(root,text="Click Me!")
label2 = Label(root,text="")

Label1.grid(row =0,column=1,padx=10,pady=10)
e.grid(row =0,column=1,columnspan=2,padx=10,pady=10)

myButton.grid(row =1,column=0,columnspan=3,padx=10,pady=10)
label2.grid(row =2,column=0,columnspan=3,padx=10,pady=10)

root.mainloop()