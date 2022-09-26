import pygame
from pygame.locals import *
import random

size = width, height = (900, 700)
road_w = int(width/1.6)
roadMark_w = int(width/80)

#   DIREÇÕES
faixa_direita = width/2 + road_w/4
faixa_esquerda = width/2 - road_w/4
speed = 1


pygame.init()
janela_aberta = True
#   TAMANHO DA JANELA
janela = pygame.display.set_mode((size))

#   NOME NA JANELA
pygame.display.set_caption('Joguin')

#   COR DE FUNDO DA JANELA
janela.fill((60, 220, 0))

#   ATUALIZANDO A JANELA
pygame.display.update()

#   CARREGANDO IMAGENS JOGADOR
jogador = pygame.image.load("jogador.png")
jogador_loc = jogador.get_rect()
jogador_loc.center = faixa_direita, height*0.8

#   CARREGANDO IMAGENS INIMIGO
inimigo = pygame.image.load("inimigo.png")
inimigo_loc = inimigo.get_rect()
inimigo_loc.center = faixa_esquerda, height*0.8

counter = 0

while janela_aberta:
    counter += 1
    if counter == 5000:
        speed+=0.25
        counter = 0
        print("level-up", speed)
    #   ANIMAÇÃO INIMIGO
    inimigo_loc[1] += speed
    if inimigo_loc[1] > height:
        if random.randint(0,1) == 0:
            inimigo_loc.center = faixa_direita, -200
        else:
            inimigo_loc.center = faixa_esquerda, -200
    #   FIM DE JOGO
    if jogador_loc[0] == inimigo_loc[0] and inimigo_loc[1] > jogador_loc[1] - 250:
        print("Game Over! Você perdeu!")
        break

    #   EVENTOS // ANIMAÇÃO
    for event in pygame.event.get():
        if event.type == QUIT:
            janela_aberta = False
            #   ANIMAÇÃO PERSONAGEM
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                jogador_loc = jogador_loc.move([-int(road_w/2),0])
            if event.key in [K_d, K_RIGHT]:
                jogador_loc = jogador_loc.move([int(road_w/2),0])

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

    janela.blit(jogador, jogador_loc)
    janela.blit(inimigo, inimigo_loc)
    pygame.display.update()


pygame.quit()