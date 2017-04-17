import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainwindow = tkinter.Tk()

mainwindow.title("Hello world")
mainwindow.geometry('640x480+500+400')

label = tkinter.Label(mainwindow, text="Herro Worrd")
label.pack(side='top')
# packing to a specific side restricts the button anchors
leftFrame = tkinter.Frame(mainwindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(mainwindow, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')
# gotta sue fill and BOTH to fill the window with the canvas
rightFrame = tkinter.Frame(mainwindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainwindow.mainloop()