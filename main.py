import tkinter as tk

from pendulum import Pendulum
from point import Point

size = 1960, 1080
master = tk.Tk()
canvas = tk.Canvas(master, width=size[0], height=size[1])
master.attributes('-fullscreen', True)
canvas.pack()
pend1 = Pendulum(Point(size[0] / 2, size[1] / 2), length=100)
pend2 = Pendulum(Point(0, 0), length=200)
points = []


def draw_point():
    global canvas, pend1, points
    canvas.delete('all')
    for point in points:
        width = point[0] / 10
        x, y = point[1].x, point[1].y
        canvas.create_oval(x - width, y - width, x + width, y + width, fill='#000000')
        point[0] -= 1
    try:
        point = points[-1]
        x, y = point[1].x, point[1].y
        canvas.create_line(x, y, pend1.get_end().x, pend1.get_end().y)
    except:
        pass
    canvas.create_line(size[0] / 2, size[1] / 2, pend1.get_end().x, pend1.get_end().y)
    points = [p for p in points if p[0] > 0]

def update():
    global canvas, master, pend1
    draw_point()
    pend1.update(pend=pend2)
    pend2.update(center=pend1.get_end())
    points.append([1, pend1.get_end()])
    points.append([200, pend2.get_end()])
    master.after(20, update)


def main():
    update()
    tk.mainloop()


if __name__ == '__main__':
    main()
