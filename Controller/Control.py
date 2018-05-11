#!/usr/bin/env python
import pygame

from CC3501Utils import *
from Model.Pelota import Pelota
from View.Window import Window

class Control:
    def __init__(self):
        self.heigth = 600
        self.width = 400
        init(self.heigth, self.width, "Mi juego")

        self.items = []
        self.pelota = Pelota()
        self.items.append(self.pelota)

        self.window = Window()
        run = True
        while run:
            self.window.dibujar(self.items)

    def update(self):
        self.window.dibujar()