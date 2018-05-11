#!/usr/bin/env python
import pygame
from CC3501Utils import *
from Controller.Control import Control
from View.Window import Window
from Model.Pelota import Pelota
from Model.Aro import Aro
import random


def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "Mi juego")
    vista = Window()

    items = []
    pelota = Pelota(pos=Vector(100, 0.7 * alto))
    items.append(pelota)

    aro = Aro(pos=Vector(ancho - 400, 0.3 * alto))
    items.append(aro)

    aro = Aro(pos=Vector(ancho - 100, 0.5 * alto))
    items.append(aro)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    items[0].saltar()

        vista.dibujar(items)
        pygame.display.flip()
        pygame.time.wait(int(1000 / 30))

        if items[len(items)-1].generarNuevo(ancho):
            nuevoAro = Aro(pos=Vector(ancho + 100, random.randint(100, alto - 100)))
            items.append(nuevoAro)


        for i in items:
            i.mover()


    pygame.quit()


main()

# while True:
#   program.update()
#  pygame.time.wait(int(1000/30))
