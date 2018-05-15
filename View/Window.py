#!/usr/bin/env python
import pygame
from CC3501Utils import *
from Model.Text import draw_text
from Model.Aro import Aro

class Window:
    def dibujar(self, items, escena, score):
        # limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        escena.dibujar()
        #Text
        draw_text(240, 600*0.78, "SCORE", fondo=(40,40,40), tamano = 40)
        draw_text(96 + 55 + 90, 600*0.62 + 40, str(score), fondo = (40,40,40), tamano = 40)
        draw_text(96 + 55, 600 * 0.62 + 10, "HOME", fondo=(40,40,40))
        draw_text(96 + 55 + 180, 600 * 0.62 + 10, "VISITOR", fondo=(40, 40, 40))
        for i in items:
            i.dibujar()
            if type(i) == Aro and i.score != 0:
                draw_text(i.pos.cartesianas()[0], i.pos.cartesianas()[1] - 40, "+ " + str(i.score),color=(0,0,0), fondo= (255, 255, 0), tamano = 30)



