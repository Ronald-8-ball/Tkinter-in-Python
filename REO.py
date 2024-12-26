from tkinter import *
window = Tk()
window.title("My canvas")
window.geometry("300x300")

geo = Label(text = "Konichiwa", fg = "black", bg = "white")

geo2 = Button(text = "Click here", fg = "black", bg = "white")

geo3 = Entry(fg = "blue", bg = "red", width = 50)

geo.pack()
geo2.pack()
geo3.pack()

geo4 = Frame(master = window, relief = RAISED, borderwidth = 5)
geo4.pack()

geo5 = Label(master = geo4, text = "sample frame" )
geo5.pack()

geo6 = Text(fg = "blue", bg = "yellow")
geo6.pack()

window.mainloop()
