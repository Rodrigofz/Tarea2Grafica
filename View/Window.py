#!/usr/bin/env python
from Resources.CC3501Utils import *
from Resources.Text import draw_text
from Model.Aro import Aro

class Window:
    def dibujar(self, items, escena, score, pausa = False):
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

        #de ser necesario, muestra que el juego esta pausado
        if pausa:
            draw_text(400, 300, "PAUSE", tamano = 40)

        #mostrar controles
        draw_text(710, 570, "SPACE = Jump", tamano = 25, color = (255,255,255), fondo = (120, 183, 255))
        draw_text(710, 550, "p = Pause", tamano = 25, color = (255,255,255), fondo = (120, 183, 255))

