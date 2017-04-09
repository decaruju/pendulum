from math import cos, sin, pi

from point import Point

class Pendulum:
    def __init__(self, center, length, angle=0, speed=0):
        self.center = center
        self.angle = angle
        self.speed = speed
        self.length = length

    def get_end(self):
        return Point(self.center.x + self.length * cos(self.angle), self.center.y + self.length * sin(self.angle))

    def update(self, center=None, pend=None):
        speed = 0.005
        if center is not None:
            self.center = center
        if pend is not None:
            self.speed += speed*cos(self.angle - pend.angle)
        while self.angle < 0:
            self.angle += 2*pi
        while self.angle > 2*pi:
            self.angle -= 2*pi
        self.angle += self.speed
        self.speed += speed*cos(self.angle)

