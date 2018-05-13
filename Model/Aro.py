#!/usr/bin/env python
from CC3501Utils import *
import numpy as np
import random

class Aro(Figura):
    def __init__(self, pos=Vector(50.0, 30.0), rgb=(255.0 / 255, 0, 0)):
        opciones = ['normal', 'tubo']
        self.tipo = opciones[random.randint(0,len(opciones) - 1)]
        self.radioM = 70
        self.radiom = 15
        self.reaparicionRatio = (6/8)
        self.velocidad = -2
        super().__init__(pos, rgb)


    def figura(self):
        if self.tipo == 'normal':
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


        if self.tipo == 'tubo':
            for j in range(0,70):

                glLineWidth(20)
                glBegin(GL_LINE_LOOP)

                radioM = self.radioM * 0.8
                if j >= 55: radioM = radioM * 1.2

                radiom = self.radiom * 0.8
                ang = 2 * pi / 20
                for i in np.arange(0, 50, 0.1) :
                    ang_i = ang * i
                    if sin(ang_i) * radiom < 0:
                        xCrit = -20
                        dist = abs(cos(ang_i) * radioM - xCrit)
                        gi = 247
                        gf = 140
                        greenA = ((gf-gi)*dist/radioM + gi)/255
                        glColor3f(83 / 255, greenA, 54 / 255)
                    else:
                        glColor3f(26/255, 140/255, 19/255)

                    glVertex(cos(ang_i) * radioM, sin(ang_i) * radiom + j)

                glEnd()




    def mover(self):
        self.pos += Vector(self.velocidad, 0)

    def enPantalla(self):
        return self.pos.cartesianas()[0] + self.radioM > 0

    def generarNuevo(self, anchoPantalla):
        return self.pos.cartesianas()[0] + self.radioM in range(int(self.reaparicionRatio * anchoPantalla - 2),int(self.reaparicionRatio * anchoPantalla + 2))


