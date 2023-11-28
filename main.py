import pygame
from data import *
import sys
from player import Player
from ray import Ray

pygame.init()
screen = pygame.display.set_mode((1400,600))
clock = pygame.time.Clock()
player = Player()
ray = Ray()


def drawMap():
    for y,row in enumerate(MAP):
        for x,item in enumerate(row):
            if item == '1':
                rect = pygame.Rect(x*50, y*50, 50,50)
                pygame.draw.rect(screen,BLACK,rect)

def drawOutline():
    for i in range(WIDTH//50):
        pygame.draw.line(screen,GREY, (i*50,0), (i*50, HEIGHT))
    for i in range(HEIGHT//50):
        pygame.draw.line(screen,GREY, (0,i*50), (WIDTH, i*50))

def drawFloor():
    floor_rect = pygame.Rect(WIDTH, HEIGHT/2, 600,300)
    pygame.draw.rect(screen,GREY,floor_rect)

    for y,row in enumerate(MAP_FLOOR):
        for x,item in enumerate(row):
            if item == '1':
                rect = pygame.Rect(x*50, y*50, 50,50)
                pygame.draw.rect(screen,GREY,rect)

def checkMouse():
    mKeys = pygame.mouse.get_pressed()
    if mKeys[0]:
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < 800:
            MAP[mouse_pos[1]//50][mouse_pos[0]//50] = '1'
    if mKeys[2]:
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < 800:
            MAP[mouse_pos[1]//50][mouse_pos[0]//50] = '0' 

while True:
    screen.fill((255,255,255))
    drawFloor()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    checkMouse()
    drawMap()
    player.movement()
    drawOutline()
    ray.rayCasting(screen, player.angle, player.pos)
    player.display(screen)
    

    pygame.display.update()
    clock.tick(FPS)
