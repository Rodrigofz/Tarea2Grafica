#!/usr/bin/env python
from CC3501Utils import *


class Aro(Figura):
    def __init__(self, pos=Vector(50.0, 30.0), rgb=(255.0 / 255, 0, 0)):
        self.radioM = 70
        self.radiom = 15
        self.reaparicionRatio = (6/8)
        super().__init__(pos, rgb)


    def figura(self):
        glLineWidth(20)
        glBegin(GL_LINE_LOOP)
        glColor3f(1, 0, 0)
        radioM = self.radioM
        radiom = self.radiom
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(cos(ang_i) * radioM, sin(ang_i) * radiom)

        glEnd()

    def mover(self):
        self.pos += Vector(-2, 0)

    def enPantalla(self):
        return self.pos.cartesianas()[0] + self.radioM > 0

    def generarNuevo(self, anchoPantalla):
        return self.pos.cartesianas()[0] + self.radioM in range(int(self.reaparicionRatio * anchoPantalla - 2),int(self.reaparicionRatio * anchoPantalla + 2))


