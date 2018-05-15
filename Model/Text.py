from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame

def draw_text(x, y, text, color=(255, 255, 255), fondo=(0, 0, 0, 0), tamano=20):
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    font = pygame.font.Font("ARCADE.TTF", tamano)
    text_surface = font.render(text, 4, color, fondo)
    text_surface.set_alpha(0)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    position = (x-text_surface.get_width()/2, y-text_surface.get_height()/2)
    glRasterPos2d(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)