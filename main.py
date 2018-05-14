#!/usr/bin/env python
import pygame
from CC3501Utils import *
from Controller.Control import Control
from View.Window import Window
from View.Escena import Escena
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

    escena = Escena(ancho, alto)

    run = True
    while run:
        #Checkear input del teclado
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pelota.saltar()

        #Dibujar

        vista.dibujar(items, escena)
        pygame.display.flip()
        pygame.time.wait(int(1000 / 30))

        #Rebotar abajo
        if pelota.pos.cartesianas()[1] <= 35:
            pelota.saltar()

        #Rebotar arriba
        if pelota.pos.cartesianas()[1] >= alto - 15:
            pelota.chocarArriba()

        #Generar aro nuevo
        if items[len(items)-1].generarNuevo(ancho):
            nuevoAro = Aro(pos=Vector(ancho + 100, random.randint(100, alto - 100)))
            items.append(nuevoAro)

        #Sacar aros que ya no esten en pantalla
        if items[1].pos.cartesianas()[0] <= -100:
            items.pop(1)

        #mover
        for i in items:
            i.mover()


    pygame.quit()


main()

