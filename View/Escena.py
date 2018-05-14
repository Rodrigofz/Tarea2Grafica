from CC3501Utils import *
import random

class Escena(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.altoSuelo = alto/12
        super().__init__(pos = Vector(0,0))

    def figura(self):
        #Fondo
        glBegin(GL_QUADS)
        glColor3f(115/255, 184/255, 223/255)
        glVertex2f(0,0)
        glVertex2f(0, self.alto)
        glVertex2f(self.ancho, self.alto)
        glVertex2f(self.ancho, 0)
        glEnd()

        #Suelo
        glBegin(GL_QUADS)
        glColor3f(177/255, 76 / 255, 46/255)
        glVertex2f(0,0)
        glVertex2f(0, self.altoSuelo)
        glVertex2f(self.ancho, self.altoSuelo)
        glVertex2f(self.ancho, 0)
        glEnd()

        #Lineas
        i = 0
        while i <= int(self.altoSuelo):
            glBegin(GL_LINE_LOOP)
            glColor3f(0,0,0)
            glVertex2f(0, i)
            glVertex2f(self.ancho, i)
            glEnd()

            if i != int(self.altoSuelo):
                glBegin(GL_LINE_LOOP)
                glColor3f(0,0,0)
                aux = random.randint(0, self.ancho/2)
                glVertex2f(aux, i)
                glVertex2f(aux + 10, i + self.altoSuelo/5)
                glEnd()

                glBegin(GL_LINE_LOOP)
                glColor3f(0,0,0)
                aux2 = random.randint(self.ancho/2, self.ancho)
                glVertex2f(aux2, i)
                glVertex2f(aux2 + 10, i + self.altoSuelo / 5)
                glEnd()

            i += self.altoSuelo/5

        #Muralla parte baja
        glBegin(GL_QUADS)
        glColor3f(149/255, 76 / 255, 46/255)
        glVertex2f(0, self.altoSuelo+1)
        glVertex2f(0, self.altoSuelo * 2.5)
        glVertex2f(self.ancho, self.altoSuelo * 2.5)
        glVertex2f(self.ancho, self.altoSuelo+1)
        glEnd()
        #Lineas
        i = 0
        while i<self.ancho:
            glBegin(GL_LINE_LOOP)
            glColor3f(0,0,0)
            glVertex2f(i, self.altoSuelo+1)
            glVertex2f(i, self.altoSuelo * 2.5 - 20)
            glEnd()
            i += self.ancho/24

        glBegin(GL_LINE_LOOP)
        glVertex2f(0, self.altoSuelo * 2.5 - 20)
        glVertex2f(0, self.altoSuelo * 2.5)
        glVertex2f(self.ancho, self.altoSuelo * 2.5)
        glVertex2f(self.ancho, self.altoSuelo * 2.5 - 20)
        glEnd()

        #Marcador
        glBegin(GL_QUADS)
        glColor3f(32/255, 32/255, 32/255)
        glVertex2f(self.ancho * 0.1, self.alto * 0.6)
        glVertex2f(self.ancho * 0.1, self.alto * 0.85)
        glVertex2f(self.ancho * 0.5, self.alto * 0.85)
        glVertex2f(self.ancho * 0.5, self.alto * 0.6)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(40 / 255, 40 / 255, 40 / 255)
        glVertex2f(self.ancho * 0.12, self.alto * 0.62)
        glVertex2f(self.ancho * 0.12, self.alto * 0.83)
        glVertex2f(self.ancho * 0.48, self.alto * 0.83)
        glVertex2f(self.ancho * 0.48, self.alto * 0.62)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(218 / 255, 197 / 255, 90 / 255)
        glVertex2f(self.ancho * 0.12 + 40, self.alto * 0.62 + 40)
        glVertex2f(self.ancho * 0.12 + 40, self.alto * 0.62 + 80)
        glVertex2f(self.ancho * 0.12 + 70, self.alto * 0.62 + 80)
        glVertex2f(self.ancho * 0.12 + 70, self.alto * 0.62 + 40)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(218 / 255, 197 / 255, 90 / 255)
        glVertex2f(self.ancho * 0.48 - 40, self.alto * 0.62 + 40)
        glVertex2f(self.ancho * 0.48 - 40, self.alto * 0.62 + 80)
        glVertex2f(self.ancho * 0.48 - 70, self.alto * 0.62 + 80)
        glVertex2f(self.ancho * 0.48 - 70, self.alto * 0.62 + 40)
        glEnd()


        #Timbre:
        glBegin(GL_QUADS)
        glColor(204/255, 204/255, 0)
        glVertex2f(self.ancho * 0.8 - 18, self.alto * 0.7 - 18)
        glVertex2f(self.ancho * 0.8 - 18, self.alto * 0.7 - 25)
        glVertex2f(self.ancho * 0.8 + 18, self.alto * 0.7 - 25)
        glVertex2f(self.ancho * 0.8 + 18, self.alto * 0.7 - 18)
        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor(0, 0, 0)
        glVertex2f(self.ancho * 0.8 - 18, self.alto * 0.7 - 18)
        glVertex2f(self.ancho * 0.8 - 18, self.alto * 0.7 - 25)
        glVertex2f(self.ancho * 0.8 + 18, self.alto * 0.7 - 25)
        glVertex2f(self.ancho * 0.8 + 18, self.alto * 0.7 - 18)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(204/255, 204/255, 0)
        glVertex2f(self.ancho * 0.8, self.alto * 0.7)
        radio = 20
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(cos(ang_i) * radio + self.ancho * 0.8, sin(ang_i) * radio + self.alto * 0.7)

        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0,0,0)
        radio = 20
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(cos(ang_i) * radio + self.ancho * 0.8, sin(ang_i) * radio + self.alto * 0.7)

        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0,0,0)
        #glVertex2f(self.ancho * 0.8, self.alto * 0.7)
        radio = 3
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(cos(ang_i) * radio + self.ancho * 0.8, sin(ang_i) * radio + self.alto * 0.7)

        glEnd()