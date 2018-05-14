#!/usr/bin/env python
import pygame
from CC3501Utils import *
import numpy


class Pelota(Figura):
    def __init__(self, pos=Vector(10.0, 30.0), rgb=(255.0 / 255, 128.0 / 255, 0)):
        self.acY = -0.045
        self.velY = -0.1
        self.t = 0
        self.dir = 0
        self.radio = 30
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(255.0 / 255, 128.0 / 255, 0)
        glVertex2f(0, 0)
        radio = self.radio
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(cos(ang_i) * radio, sin(ang_i) * radio)

        glEnd()

    def mover(self):
        if self.dir != 0:
            self.dir += 1
            if self.dir == 1000:
                self.dir = 0
                self.t = 0
                self.vel = -0.1

        self.pos += Vector(0, self.velY + self.acY * self.t ** 2)

        self.t += 1

    def saltar(self):
        self.t = 0
        self.dir = 1
        self.velY = 10

    def chocarArriba(self):
        self.t = 10
        self.dir = 0
        self.velY = -0.1




