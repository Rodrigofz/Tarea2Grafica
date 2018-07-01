#!/usr/bin/env python
from Resources.CC3501Utils import *
from View.Window import Window
from Model.Escena import Escena
from Model.Pelota import Pelota
from Model.Aro import Aro
import random


def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "Flappy dunk")
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
    jumpSound.set_volume(0.1)

    run = True
    pause = True

    while run:
        while pause:
            vista.dibujar(items, escena, score, True)
            pygame.display.flip()
            pygame.time.wait(int(1000 / 30))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        pause = False
                if event.type == QUIT:
                    pause = False
                    run = False


        #Checkear input del teclado
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    jumpSound.play()
                    pelota.saltar()
                if event.key == K_p:
                    pause = True

        #Dibujar

        vista.dibujar(items, escena, score)

        #Chocar abajo
        if pelota.pos.cartesianas()[1] <= 0:
            print ('No puedes tocar el suelo :(')
            run = False

        #Chocar arriba
        if pelota.pos.cartesianas()[1] >= alto:
            print ('No puedes tocar el techo :(')
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

    print('JUEGO TERMINADO')
    pygame.quit()


main()

