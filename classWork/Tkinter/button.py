import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r,text='Stop',width=12,
                   command = r.destroy)
button.pack()
r.mainloop()