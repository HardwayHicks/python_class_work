import tkinter

mainwindow = tkinter.Tk()

mainwindow.title("Calculatoor")
mainwindow.geometry('280x480-8-200')
mainwindow['padx'] = 8

mainwindow.columnconfigure(0, weight=100)
mainwindow.columnconfigure(1, weight=100)
mainwindow.columnconfigure(2, weight=100)
mainwindow.columnconfigure(3, weight=100)
mainwindow.rowconfigure(0, weight=100)
mainwindow.rowconfigure(1, weight=100)
mainwindow.rowconfigure(2, weight=100)
mainwindow.rowconfigure(3, weight=100)
mainwindow.rowconfigure(4, weight=100)
mainwindow.rowconfigure(5, weight=100)

result = tkinter.Entry(mainwindow)
result.grid(row=0, column=0, columnspan=4, sticky='nw')

mainwindow.mainloop()