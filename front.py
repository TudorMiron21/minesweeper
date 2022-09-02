from pygame.locals import *
from io import DEFAULT_BUFFER_SIZE
import pygame
import sys
import os
import backend

import menu

pygame.init()

pygame.font.init()
WIDTH, HEIGHT = 40*backend.size2, 120+40*backend.size1
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MINESWEEPER")
font = pygame.font.SysFont("Arial", 32)
GREY = (192, 192, 192)
FPS = 60
DEFAULT_IMAGE = (40, 40)
BLANCK = pygame.image.load(os.path.join('images', 'empty-block.png'))
BLANCK = pygame.transform.scale(BLANCK, DEFAULT_IMAGE)
ZERO = pygame.image.load(os.path.join('images', '0.png'))
ZERO = pygame.transform.scale(ZERO, DEFAULT_IMAGE)
ONE = pygame.image.load(os.path.join('images', '1.png'))
ONE = pygame.transform.scale(ONE, DEFAULT_IMAGE)
TWO = pygame.image.load(os.path.join('images', '2.png'))
TWO = pygame.transform.scale(TWO, DEFAULT_IMAGE)
THREE = pygame.image.load(os.path.join('images', '3.png'))
THREE = pygame.transform.scale(THREE, DEFAULT_IMAGE)
FOUR = pygame.image.load(os.path.join('images', '4.png'))
FOUR = pygame.transform.scale(FOUR, DEFAULT_IMAGE)
FIVE = pygame.image.load(os.path.join('images', '5.png'))
FIVE = pygame.transform.scale(FIVE, DEFAULT_IMAGE)
SIX = pygame.image.load(os.path.join('images', '6.png'))
SIX = pygame.transform.scale(SIX, DEFAULT_IMAGE)
SEVEN = pygame.image.load(os.path.join('images', '7.png'))
SEVEN = pygame.transform.scale(SEVEN, DEFAULT_IMAGE)
EIGHT = pygame.image.load(os.path.join('images', '8.png'))
EIGHT = pygame.transform.scale(EIGHT, DEFAULT_IMAGE)
CLICKED_BOMB = pygame.image.load(os.path.join('images', 'unclicked-bomb.png'))
CLICKED_BOMB = pygame.transform.scale(CLICKED_BOMB, DEFAULT_IMAGE)
UNCLICKED_BOMB = pygame.image.load(
    os.path.join('images', 'bomb-at-clicked-block.png'))
UNCLICKED_BOMB = pygame.transform.scale(UNCLICKED_BOMB, DEFAULT_IMAGE)
FLAG = pygame.image.load(os.path.join('images', 'flag.png'))
FLAG = pygame.transform.scale(FLAG, DEFAULT_IMAGE)
WRONG_FLAG = pygame.image.load(os.path.join('images', 'wrong-flag.png'))
WRONG_FLAG = pygame.transform.scale(WRONG_FLAG, DEFAULT_IMAGE)
WON = pygame.image.load(os.path.join('images', 'you_won.png'))
WON = pygame.transform.scale(WON, (200, 60))
LOSS = pygame.image.load(os.path.join('images', 'you_lose.png'))
LOSS = pygame.transform.scale(LOSS, (200, 60))

initial_coord = [120, 0]
textX,textY=(0,0)

def show_score(x,y,score):
    scor=font.render("SCORE: "+str(score),True,(0,0,0))
    WIN.blit(scor,(x,y))

def get_coord_for_matrix(x, y):
    if y < 120:
        return [x, 0]
    if x >= initial_coord[1] and y >= initial_coord[0]:
        return [(x-initial_coord[1])//40, (y-initial_coord[0])//40]

def load_pictures():
    for i in range(3, backend.size1+3):
        for j in range(backend.size2):
            if backend.unknown[i-3][j] == -1:
                WIN.blit(BLANCK, (j*40, i*40))
            if backend.unknown[i-3][j] == backend.bomb:
                WIN.blit(CLICKED_BOMB, (j*40, i*40))
            if backend.unknown[i-3][j] == backend.clicked_bomb:
                WIN.blit(UNCLICKED_BOMB, (j*40, i*40))
            if backend.unknown[i-3][j] == 0:
                WIN.blit(ZERO, (j*40, i*40))
            if backend.unknown[i-3][j] == 1:
                WIN.blit(ONE, (j*40, i*40))
            if backend.unknown[i-3][j] == 2:
                WIN.blit(TWO, (j*40, i*40))
            if backend.unknown[i-3][j] == 3:
                WIN.blit(THREE, (j*40, i*40))
            if backend.unknown[i-3][j] == 4:
                WIN.blit(FOUR, (j*40, i*40))
            if backend.unknown[i-3][j] == 5:
                WIN.blit(FIVE, (j*40, i*40))
            if backend.unknown[i-3][j] == 6:
                WIN.blit(SIX, (j*40, i*40))
            if backend.unknown[i-3][j] == 7:
                WIN.blit(SEVEN, (j*40, i*40))
            if backend.unknown[i-3][j] == backend.flag:
                WIN.blit(FLAG, (j*40, i*40))

def load_win():
    WIN.blit(WON,(40*(backend.size2/2-2),40))
    pygame.display.update()

def load_loss():
    WIN.blit(LOSS,(40*(backend.size2/2-2),40))
    pygame.display.update()

def draw_window(scor):
    WIN.fill(GREY)
    load_pictures()
    show_score(textX,textY,scor)
    pygame.display.update()

def main():

    backend.generate_bombs(backend.grid)
    backend.afisare_grid(backend.grid)
    ok=0
    ok1=0
    first_click=0
    ok2=0
    nr_flags=backend.nr_flags
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_window(nr_flags)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    mx, my = pygame.mouse.get_pos()
                    loc = [mx, my]
                    #ok2=backend.click(get_coord_for_matrix(mx, my)[1], get_coord_for_matrix(mx, my)[0])
                    if first_click==0:
                        while not backend.click(get_coord_for_matrix(mx, my)[1], get_coord_for_matrix(mx, my)[0]):
                            backend.generate_bombs(backend.grid)
                            backend.afisare_grid(backend.grid)
                        first_click=1

                    elif backend.click(get_coord_for_matrix(mx, my)[1], get_coord_for_matrix(mx, my)[0]) == 0:

                        backend.unknown[get_coord_for_matrix(mx, my)[1]][get_coord_for_matrix(mx, my)[0]]=backend.clicked_bomb
                        backend.add_bomb_neighbours()
                        draw_window(nr_flags)
                        ok=1
                        backend.afisare_grid(backend.grid)
                        run = False
                        first_click=1
                    elif backend.win() == 1:
                        run = False
                        ok1=1
                        draw_window(nr_flags)
                        first_click=1
                if event.button == 3:
                    mx, my = pygame.mouse.get_pos()
                    loc = [mx, my]
                    okay=backend.flag(get_coord_for_matrix(mx, my)[
                                 1], get_coord_for_matrix(mx, my)[0])
                    row=get_coord_for_matrix(mx, my)[1]
                    col=get_coord_for_matrix(mx, my)[0]
                    if okay:
                        if backend.unknown[row][col]==backend.flag:
                            nr_flags-=1
                    elif backend.unknown[row][col]==-1:
                        nr_flags+=1
        if run == False:

            draw_window(nr_flags)
            if ok==1:
                pygame.mixer.Sound("boom.mp3").play()
                load_loss()
            elif ok1:
                load_win()
                pygame.mixer.Sound("win.mp3").play()
            run2 = True
            while run2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run2 = False
                       
    pygame.quit()


if __name__ == "__main__":
    main()
