import pygame
import sys

pygame.init()
display = pygame.display.set_mode((500,500))


def displayTexures(texture):
    texture_arr = []
    colors_dict = {}
    with open(f"textures/{texture}.txt") as file:
        data = file.read().split('\n')
        for row in data:
            texture_arr.append([char for char in row])
    
    with open (f"textures/{texture}_colors.txt") as file:
        data = file.read().split('\n')
        for i,row in enumerate(data):
            colors = row[row.find('-')+2:].split(',')
            colors = (int(colors[0]), int(colors[1]), int(colors[2]))
            colors_dict[str(i+1)] = colors
    
    for y,row in enumerate(texture_arr):
        for x,pixel in enumerate(row):
            pygame.draw.rect(display,colors_dict[pixel], (x*5, y*5,5,5))
            pygame.draw.rect(display,colors_dict[pixel], (250+x*5, y*5,5,5))
            pygame.draw.rect(display,colors_dict[pixel], (x*5, 250+y*5,5,5))
            pygame.draw.rect(display,colors_dict[pixel], (250+x*5, 250+y*5,5,5))


    
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
            sys.exit()

    displayTexures("brick")
    pygame.display.update()

pygame.quit()