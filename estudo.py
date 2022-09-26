from turtle import width
import pygame
from pygame.locals import *

size = width, height = (900, 700)
road_w = int(width/1.6)
roadMark_w = int(width/80)


pygame.init()
janela_aberta = True
#   TAMANHO DA JANELA
janela = pygame.display.set_mode((size))

#   NOME NA JANELA
pygame.display.set_caption('Joguin')

#   COR DE FUNDO DA JANELA
janela.fill((60, 220, 0))

#   CRIANDO DESENHO NA TELA
pygame.draw.rect( # Marca cinza
            janela,
            (50,50,50),
            (width/2-road_w/2, 0, road_w, height))

pygame.draw.rect( # Marca amarela
                janela,
                (255, 240, 60),
                (width/2 - roadMark_w/2, 0, roadMark_w, height))

pygame.draw.rect( # Marca branca esquerda
                janela,
                (255, 255, 255),
                (width/2 - road_w/2 + roadMark_w*2, 0, roadMark_w, height))

pygame.draw.rect( # Marca branca direita
                janela,
                (255, 255, 255),
                (width/2 + road_w/2 - roadMark_w*3, 0, roadMark_w, height))

#   ATUALIZANDO A JANELA
pygame.display.update()

while janela_aberta:
    for event in pygame.event.get():
        if event.type == QUIT:
            janela_aberta = False

pygame.quit()