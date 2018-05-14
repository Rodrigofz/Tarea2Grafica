#!/usr/bin/env python
import pygame
from CC3501Utils import *

class Window:
    #def __init__(self):

    def dibujar(self, items, escena):
        # limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        escena.dibujar()

        for i in items:
            i.dibujar()


