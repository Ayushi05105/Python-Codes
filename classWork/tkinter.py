import tkinter as tk
root =tk.Tk()
# root.title("My first tkinter app")
# root.geometry("300x200")

# label = tk.Label(root,text="Hello,Tkinter!",font =("Arial",16))
# label.pack(pady=20)
# button = tk.Button(root,text="Click Me")
# button.pack()

label = tk.Label(root,text="Welcome to Tkinter")
tk.Button(root,text="Click Me",command = hello).pack()
root.mainloop()