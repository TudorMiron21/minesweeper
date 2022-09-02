from pygame.locals import *
from io import DEFAULT_BUFFER_SIZE
import pygame
import sys
import os
import sizes1
import sizes2
import sizes3


pygame.font.init()
WIDTH,HEIGHT=700,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MENU")
font = pygame.font.SysFont("comicsansms", 32)
FPS = 60
BACKROUND= pygame.image.load(os.path.join('images', 'bomb_backround.png'))
BACKROUND = pygame.transform.scale(BACKROUND,(WIDTH,HEIGHT))

def show_text():
    welcome_message=font.render("Welcome to MINESWEEPER!",True,(255,0,0))
    WIN.blit(welcome_message,(150,10))

    easy=font.render("For easy mode press the E key",True,(255,0,0))
    WIN.blit(easy,(10,100))
    medium=font.render("For medium mode press the M key",True,(255,0,0))
    WIN.blit(medium,(10,200))
    hard=font.render("For hard mode press the H key",True,(255,0,0))
    WIN.blit(hard,(10,300))


def draw_window():
    WIN.blit(BACKROUND,(0,0))
    show_text()
    pygame.display.update()


def main():
    run=True
    ok=0
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    s1=sizes1.size1
                    s2=sizes1.size2
                    fl1=sizes1.nr_flags
                    t1=(s1,s2,fl1)
                    return t1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_m:
                    s3=sizes2.size1
                    s4=sizes2.size2
                    fl2=sizes2.nr_flags
                    t2=(s3,s4,fl2)
                    return t2
                 
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_h:
                    s5=sizes3.size1
                    s6=sizes3.size2
                    fl3=sizes3.nr_flags
                    t3=(s5,s6,fl3)
                    return t3
                    
        draw_window()
    pygame.quit()



