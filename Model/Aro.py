#!/usr/bin/env python
from CC3501Utils import *
import numpy as np
import random

class Aro(Figura):
    def __init__(self, pos=Vector(50.0, 30.0), rgb=(255.0 / 255, 0, 0)):
        opciones = ['normal', 'tubo', 'raro']
        self.tipo = opciones[random.randint(0,len(opciones) - 1)]
        self.radioM = random.randint(50, 100)
        self.radiom = self.radioM * 0.21
        self.reaparicionRatio = 0.70
        self.velocidad = -7
        self.atravesado = False
        self.score = 0
        super().__init__(pos, rgb)


    def figura(self):
        if self.tipo == 'normal':
            self.sonido = pygame.mixer.Sound("Resources/normalHoop.wav")
            self.sonido.set_volume(0.3)
            for j in range(0, 10):
                glBegin(GL_LINE_LOOP)

                radioM = self.radioM
                radiom = self.radiom
                ang = 2 * pi / 20
                for i in range(21):
                    ang_i = ang * i
                    if  sin(ang_i) * radiom > 0:
                        glColor3f(152/255, 26/255, 17/255)
                    else:
                        glColor3f(233/255, 26/255, 17/255)
                    glVertex(cos(ang_i) * radioM, sin(ang_i) * radiom + j)

                glEnd()


        if self.tipo == 'tubo':
            self.sonido = pygame.mixer.Sound("Resources/marioTube.wav")
            self.sonido.set_volume(0.1)
            for j in range(0,70):
                glBegin(GL_LINE_LOOP)
                radioM = self.radioM * 0.8
                if j >= 55: radioM = radioM * 1.2

                radiom = self.radiom * 0.8
                ang = 2 * pi / 20
                for i in range(50):
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

        if self.tipo == 'raro':
            self.sonido = pygame.mixer.Sound("Resources/normalHoop.wav")
            self.sonido.set_volume(0.3)
            for j in range(0, 5):
                glBegin(GL_LINE_LOOP)

                radioM = self.radioM
                radiom = self.radiom
                ang = 2 * pi / 20
                for i in range(21):
                    ang_i = ang * i
                    if  sin(ang_i) * radiom > 0:
                        glColor3f(17/255, 26/255, 152/255)
                    else:
                        glColor3f(17/255, 26/255, 233/255)
                    glVertex(cos(ang_i) * radioM + cos(ang_i*20)*3, sin(ang_i) * radiom + cos(ang_i*20)*3)

                glEnd()

    def mover(self):
        self.pos += Vector(self.velocidad, 0)

    def enPantalla(self):
        return self.pos.cartesianas()[0] + self.radioM > 0

    def generarNuevo(self, anchoPantalla):
        return self.pos.cartesianas()[0] + self.radioM < self.reaparicionRatio * anchoPantalla


