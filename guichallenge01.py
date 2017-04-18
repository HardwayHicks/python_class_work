import tkinter

mainwindow = tkinter.Tk()

mainwindow.title("Calculatoor")
mainwindow.geometry('280x480-8-200')
mainwindow['padx'] = 8

mainwindow.columnconfigure(0, weight=1)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1)
mainwindow.columnconfigure(3, weight=10)
mainwindow.rowconfigure(0, weight=0)
mainwindow.rowconfigure(1, weight=0)
mainwindow.rowconfigure(2, weight=0)
mainwindow.rowconfigure(3, weight=0)
mainwindow.rowconfigure(4, weight=0)
mainwindow.rowconfigure(5, weight=0)

result = tkinter.Entry(mainwindow)
result.grid(row=0, column=0, columnspan=4, sticky='nesw')
result.config()

c_button = tkinter.Button(mainwindow, width=3, text="C")
ce_button = tkinter.Button(mainwindow, width=3, text="CE")
c_button.grid(row=2, column=0, sticky='e')
ce_button.grid(row=2, column=1, sticky='ew')
button1 = tkinter.Button(mainwindow, width=3, text="1")
button2 = tkinter.Button(mainwindow, width=3, text="2")
button3 = tkinter.Button(mainwindow, width=3, text="3")
button4 = tkinter.Button(mainwindow, width=3, text="4")
button5 = tkinter.Button(mainwindow, width=3, text="5")
button6 = tkinter.Button(mainwindow, width=3, text="6")
button7 = tkinter.Button(mainwindow, width=3, text="7")
button8 = tkinter.Button(mainwindow, width=3, text="8")
button9 = tkinter.Button(mainwindow, width=3, text="9")
button0 = tkinter.Button(mainwindow, width=3, text="0")
button_add = tkinter.Button(mainwindow, width=3, text="+")
button_minus = tkinter.Button(mainwindow, width=3, text="-")
button_multiply = tkinter.Button(mainwindow, width=3, text="*")
button_divide = tkinter.Button(mainwindow, width=3, text="/")
button_equals = tkinter.Button(mainwindow, width=3, text="=")
button7.grid(row=3, column=0, sticky='e')
button8.grid(row=3, column=1, sticky='we')
button9.grid(row=3, column=2, sticky='we')
button_add.grid(row=3, column=3, sticky='w')


mainwindow.mainloop()