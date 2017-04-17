import tkinter
import os
mainwindow = tkinter.Tk()

mainwindow.title("Grid Demo")
mainwindow.geometry('640x480-8-200')
mainwindow['padx'] = 8

label = tkinter.Label(mainwindow, text="Tkinter grid demo")
label.grid(row=0, column=0, columnspan=3)

mainwindow.columnconfigure(0, weight=100)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1000)
mainwindow.columnconfigure(3, weight=600)
mainwindow.columnconfigure(4, weight=1000)
mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainwindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# frame for radio buttons
optionFrame = tkinter.LabelFrame(mainwindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(1)
# radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Path", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# this the widget that displays the result
resultLabel = tkinter.Label(mainwindow, text="result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainwindow)
result.grid(row=2, column=2, sticky='sw')

# frame for time spinners
timeFrame = tkinter.LabelFrame(mainwindow, text="time")
timeFrame.grid(row=3, column=0, sticky='new')
# time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

# frame for date spinners
dateFrame = tkinter.Frame(mainwindow)
dateFrame.grid(row=4, column=0, sticky='new')
# date labels
dayLabel = tkinter.Label(dateFrame, text="day")
monthLabel = tkinter.Label(dateFrame, text="month")
yearLabel = tkinter.Label(dateFrame, text="year")
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# actual date spinners
daySpinner = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpinner = tkinter.Spinbox(dateFrame, width=5, values=("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug",
                                                           "sep", "oct", "nov", "dec"))
yearSpinner = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpinner.grid(row=1, column=0)
monthSpinner.grid(row=1, column=1)
yearSpinner.grid(row=1, column=2)

# buttons
okButton = tkinter.Button(mainwindow, text="OK")
cancelButton =tkinter.Button(mainwindow, text="Cancel", command=mainwindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')


mainwindow.mainloop()

print(rbValue.get())

