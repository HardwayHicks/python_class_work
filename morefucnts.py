import math
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)

# functions in a class are referred to as methods
# modify the circle function so that it allows the color of the circle to be specified
# and defaults to red if no color is chosen.


def circle(page, radius, g, h, color="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h -y)
    #     plot(page, 2 *g -x, y)
    #     plot(page, 2 *g -x, 2 * h -y)


def draw_axis(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y+1, fill="red")


mainwindow = tkinter.Tk()

mainwindow.title("parabola")
mainwindow.geometry("640x480")

canvas = tkinter.Canvas(mainwindow, width=640, height=480)
canvas.grid(row=0, column=0)


draw_axis(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, "green")
circle(canvas, 100, 100, -100, "yellow")
circle(canvas, 100, -100, 100, "black")
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainwindow.mainloop()


# well since i'm here, might as well type out my daily schedule for now
# 600 wake up, at the pool before 7, swim for a minimum of 45 minutes, home by 8, spend time with girls
# having breakfast, leave to go to coffee shop or get in the pod by 10.
# the work schedule needs to be 25 on, 5 off, on the 4th break take 25
