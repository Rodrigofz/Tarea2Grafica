#!/usr/bin/env python
import pygame
from CC3501Utils import *
import numpy


class Pelota(Figura):
    def __init__(self, pos=Vector(10.0, 30.0), rgb=(255.0 / 255, 128.0 / 255, 0)):
        self.acY = -0.045
        self.velY = -0.1
        self.t = 0
        self.dir = True
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
        self.pos += Vector(0, self.velY + self.acY * self.t ** 2)
        self.t += 1
        self.dir = self.velY + self.acY * self.t ** 2 < 0

    def saltar(self):
        self.t = 0
        self.velY = 10

    def chocarArriba(self):
        self.t = 10
        self.velY = -0.1

    def atravesoAro(self, aro):
        pelotaX = self.pos.cartesianas()[0]
        aroX = aro.pos.cartesianas()[0]

        pelotaY = self.pos.cartesianas()[1]
        aroY = aro.pos.cartesianas()[1]

        checkX = (pelotaX - self.radio) >= (aroX - aro.radioM) and (pelotaX + self.radio) <= (aroX + aro.radioM)
        checkY = pelotaY >= aroY - 20 and pelotaY <= aroY + 20
        checkDir = self.dir
        checkAro = not aro.atravesado

        total = checkX and checkY and checkDir and checkAro
        if total: aro.atravesado = True

        return total



