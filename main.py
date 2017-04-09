import tkinter as tk
from random import uniform
from pendulum import Pendulum
from point import Point
from math import pi

size = 1960, 1080
master = tk.Tk()
canvas = tk.Canvas(master, width=size[0], height=size[1])
master.attributes('-fullscreen', True)
canvas.pack()
points = []
pends = []
for i in range(10):
    pends.append([Pendulum(Point(size[0] / 2, size[1] / 2),
        length=200,angle=3*pi/2), Pendulum(Point(0, 0),
            length=250,angle=3*3/2+uniform(0,0.00001))])

def draw_point():
    global canvas, points
    canvas.delete('all')
    canvas.create_oval(size[0]/2-5, size[1]/2-5, size[0]/2+5, size[1]/2+5,
                fill='#000000')
    for point in points:
        width = point[0] / 5
        x, y = point[1].x, point[1].y
        canvas.create_oval(x - width, y - width, x + width, y + width, fill='#000000')
        point[0] -= 5

    points = [p for p in points if p[0] > 10]

def update():
    global canvas, master
    #draw_point()
    for pend in pends:
        pend[0].update(pend=pend[1])
        pend[1].update(center=pend[0].get_end())
        point = pend[1].get_end()
        canvas.create_oval(point.x - 1, point.y - 1, point.x + 1, point.y + 1, fill='#000000')
        #points.append([1, pend[0].get_end()])
        #points.append([50, pend[1].get_end()])
    master.after(20, update)


def main():
    update()
    tk.mainloop()


if __name__ == '__main__':
    main()
