import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Application")

label = tk.Label(text="Welcome to my Tkinter Application")
label.pack()

button = tk.Button(text="Click Me", command= lambda : print("Button Clicked!"))
button.pack()

window.mainloop()
