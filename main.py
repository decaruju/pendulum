import tkinter as tk

from pendulum import Pendulum
from point import Point

size = 1960/2, 1080/2
master = tk.Tk()
canvas = tk.Canvas(master, width=size[0], height=size[1])
master.attributes('-fullscreen', True)
canvas.pack()
points = []
pends = [[Pendulum(Point(size[0] / 2, size[1] / 2), length=200), Pendulum(Point(0, 0), length=250)]]
for i in range(10):
    pends.append([Pendulum(Point(size[0] / 2, size[1] / 2), length=200, speed=0.0001*i), Pendulum(Point(0, 0), length=250)])

def draw_point():
    global canvas, points
    canvas.delete('all')
    for point in points:
        width = point[0] / 10
        x, y = point[1].x, point[1].y
        canvas.create_oval(x - width, y - width, x + width, y + width, fill='#000000')
        point[0] -= 1

    points = [p for p in points if p[0] > 10]

def update():
    global canvas, master
    draw_point()
    for pend in pends:
        pend[0].update(pend=pend[1])
        pend[1].update(center=pend[0].get_end())
        points.append([1, pend[0].get_end()])
        points.append([100, pend[1].get_end()])
    master.after(20, update)


def main():
    update()
    tk.mainloop()


if __name__ == '__main__':
    main()
