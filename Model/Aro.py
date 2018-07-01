#!/usr/bin/env python
from Resources.CC3501Utils import *
import random

class Aro(Figura):
    def __init__(self, pos=Vector(50.0, 30.0), rgb=(255.0 / 255, 0, 0)):
        opciones = ['normal', 'tubo', 'toilet']
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
            self.sonido = pygame.mixer.Sound("Resources/hoop1.wav")
            self.sonido.set_volume(0.4)
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

        if self.tipo == 'toilet':
            self.sonido = pygame.mixer.Sound("Resources/splash.wav")
            self.sonido.set_volume(0.6)
            radio = self.radioM * 0.8
            self.radioM = self.radioM * 0.8

            # Rectangulo inferior
            glBegin(GL_QUADS)
            glColor3f(224 / 255, 224 / 255, 224 / 255)
            glVertex2f(-radio * 0.5, -radio * 0.7)
            glVertex2f(radio * 0.5, -radio * 0.7)
            glVertex2f(radio * 0.5, -radio * 1.5)
            glVertex2f(-radio * 0.5, -radio * 1.5)
            glEnd()

            glBegin(GL_LINE_LOOP)
            glColor3f(0, 0, 0)
            glVertex2f(-radio * 0.5, -radio * 0.7)
            glVertex2f(radio * 0.5, -radio * 0.7)
            glVertex2f(radio * 0.5, -radio * 1.5)
            glVertex2f(-radio * 0.5, -radio * 1.5)
            glEnd()

            # Rectangulo superior
            glBegin(GL_QUADS)
            glColor3f(224 / 255, 224 / 255, 224 / 255)
            glVertex2f(-radio * 0.7, 0)
            glVertex2f(-radio * 0.8, radio * 1.2)
            glVertex2f(radio * 0.8, radio * 1.2)
            glVertex2f(radio * 0.7, 0)
            glEnd()

            glBegin(GL_LINE_LOOP)
            glColor3f(0,0,0)
            glVertex2f(-radio * 0.7, 0)
            glVertex2f(-radio * 0.8, radio * 1.2)
            glVertex2f(radio * 0.8, radio * 1.2)
            glVertex2f(radio * 0.7, 0)
            glEnd()

            # Semicirculo
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(224/255, 224/255, 224/255)
            glVertex2f(0, 0)
            ang = 2 * pi / 20
            for i in range(10 , 21):
                ang_i = ang * i
                glVertex(cos(ang_i) * radio, sin(ang_i) * radio)
            glEnd()

            glBegin(GL_LINE_LOOP)
            glColor3f(0, 0, 0)
            ang = 2 * pi / 20
            for i in range(10, 21):
                ang_i = ang * i
                glVertex(cos(ang_i) * radio, sin(ang_i) * radio)

            glEnd()

            #Cadena
            glBegin(GL_TRIANGLES)
            glColor3f(96/255, 95/255, 95/255)
            glVertex2f(-radio * 0.5, radio * 0.9)
            glVertex2f(-radio * 0.7, radio)
            glVertex2f(-radio * 0.5, radio * 1.1)

            glEnd()


    def mover(self):
        self.pos += Vector(self.velocidad, 0)

    def enPantalla(self):
        return self.pos.cartesianas()[0] + self.radioM > 0

    def generarNuevo(self, anchoPantalla):
        return self.pos.cartesianas()[0] + self.radioM < self.reaparicionRatio * anchoPantalla


