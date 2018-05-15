#!/usr/bin/env python
import pygame
from CC3501Utils import *
from Controller.Control import Control
from View.Window import Window
from View.Escena import Escena
from Model.Pelota import Pelota
from Model.Aro import Aro
import random
from Model.Text import draw_text


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
    score = 0
    multiplicador = 2

    #Sonido
    jumpSound = pygame.mixer.Sound("Resources/jump1.wav")
    jumpSound.set_volume(0.2)


    run = True

    while run:
        #Checkear input del teclado
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    jumpSound.play()
                    pelota.saltar()

        #Dibujar

        vista.dibujar(items, escena, score)

        #Rebotar abajo
        if pelota.pos.cartesianas()[1] <= 0:
            run = False

        #Rebotar arriba
        if pelota.pos.cartesianas()[1] >= alto:
            run = False

        #Generar aro nuevo
        if items[len(items)-1].generarNuevo(ancho):
            nuevoAro = Aro(pos=Vector(ancho + 100, random.randint(100, alto - 130)))
            items.append(nuevoAro)

        #Sacar aros que ya no esten en pantalla
        if items[1].pos.cartesianas()[0] <= -100:
            items.pop(1)

        #Pelota atraviesa aro limpiamente
        if pelota.atravesoAroClean(items[1]):
            items[1].sonido.play()
            score += multiplicador
            items[1].score += multiplicador
            multiplicador += 1

        #Pelota atraviesa aro tocando bordes
        elif pelota.atravesoAroTocandoBordes(items[1]):
            items[1].sonido.play()
            score += 1
            multiplicador = 2
            items[1].score += 1

        #Aro por debajo
        if pelota.aroPorDebajo(items[1]):
            pelota.chocarArriba()

        #mover
        for i in items:
            i.mover()

        pygame.display.flip()
        pygame.time.wait(int(1000 / 30))


    pygame.quit()


main()

