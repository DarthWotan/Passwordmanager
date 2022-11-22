from tkinter import *

root = Tk()
root.geometry("500x500")

frame_1 = Frame(root)
Grid.rowconfigure(root, 0, weight=1)

# this changes the size/number of the grid
for r in range(9):
    Grid.rowconfigure(frame_1, r, weight=1)
    for c in range(9):
        Grid.columnconfigure(frame_1, c, weight=1)


frame_1.grid()
button_1 = Button(root, text="test1")
button_2 = Button(root, text = "test2")
button_3 = Button(root, text="test3")

# dropdown box:  Source >>> https://www.delftstack.com/de/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
option_list = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
]
variable = StringVar(frame_1)
variable.set(option_list[0])

opt = OptionMenu(frame_1, variable, *option_list)
opt.config(widt=20)
opt.grid()

labelTest = Label(text="", font=('Helvetica', 12), fg='red')
labelTest.grid()

# command if it changes
def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))

# checks it
variable.trace("w", callback)




root.mainloop()