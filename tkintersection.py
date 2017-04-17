import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainwindow = tkinter.Tk()

mainwindow.title("Hello world")
mainwindow.geometry('640x480-8-200')

label = tkinter.Label(mainwindow, text="Hello Worrd")
label.grid(row=0, column=0)
# packing to a specific side restricts the button anchors
leftFrame = tkinter.Frame(mainwindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)
# gotta sue fill and BOTH to fill the window with the canvas
rightFrame = tkinter.Frame(mainwindow)
rightFrame.grid(row=1, column=2, sticky='n')
# using grid is way better than using pack, you can set up things to be much more adaptive to different layouts
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns, because without this part the columns are only displayed as the minimum needed
mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=10)
rightFrame.config(relief='sunken', borderwidth=10)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainwindow.mainloop()

