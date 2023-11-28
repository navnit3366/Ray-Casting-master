import pygame
from data import *
import math


class Player():

    def __init__(self):
        self.pos = (WIDTH//2, HEIGHT//2)
        self.color = PLAYER_COLOR
        self.radius = 5
        self.angle = 0

    def display(self, screen):
        pygame.draw.circle(screen, PLAYER_COLOR, self.pos, self.radius)
    

            


        

    def movement(self):
        keys = pygame.key.get_pressed()
        x_movement = math.cos(self.angle)*PLAYER_MOVMENT
        y_movement = math.sin(self.angle)*PLAYER_MOVMENT

        if keys[pygame.K_w]:
            if MAP[int((self.pos[1] + y_movement*4)//50)][int(self.pos[0]//50)] != '1':
                self.pos = (self.pos[0], self.pos[1] + y_movement)
            if MAP[int(self.pos[1]//50)][int((self.pos[0]+ x_movement*4)//50)] != '1':
                self.pos = (self.pos[0] + x_movement, self.pos[1])

        if keys[pygame.K_s]:
            if MAP[int((self.pos[1] - y_movement*4)//50)][int(self.pos[0]//50)] != '1':
                self.pos = (self.pos[0], self.pos[1] - y_movement)
            if MAP[int(self.pos[1]//50)][int((self.pos[0]-x_movement*4)//50)] != '1':
                self.pos = (self.pos[0] - x_movement, self.pos[1])

        x_movement = math.cos(self.angle+math.radians(90))*PLAYER_MOVMENT
        y_movement = math.sin(self.angle+math.radians(90))*PLAYER_MOVMENT

        if keys[pygame.K_d]:
            if MAP[int((self.pos[1] + y_movement*4)//50)][int(self.pos[0]//50)] != '1':
                self.pos = (self.pos[0], self.pos[1] + y_movement)
            if MAP[int(self.pos[1]//50)][int((self.pos[0]+ x_movement*4)//50)] != '1':
                self.pos = (self.pos[0] + x_movement, self.pos[1])

        if keys[pygame.K_a]:
            if MAP[int((self.pos[1] - y_movement*4)//50)][int(self.pos[0]//50)] != '1':
                self.pos = (self.pos[0], self.pos[1] - y_movement)
            if MAP[int(self.pos[1]//50)][int((self.pos[0]-x_movement*4)//50)] != '1':
                self.pos = (self.pos[0] - x_movement, self.pos[1])

        if keys[pygame.K_LEFT]:
            self.angle -= math.radians(2)
        if keys[pygame.K_RIGHT]:
            self.angle += math.radians(2)
        self.correctAngle()

    def correctAngle(self):
        if self.angle > 2*math.pi:
            self.angle = self.angle - 2*math.pi
        elif self.angle < 0:
            self.angle = self.angle + 2*math.pi
        
        