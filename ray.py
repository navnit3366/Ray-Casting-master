import pygame
import math
from data import *


class Ray():
    def __init__(self):
        self.color = RED


    def rayCasting(self, screen, angle, player_pos):
        for i in range(120):
            self.rayCast(screen, angle+math.radians(i/2)-math.radians(30), player_pos, i, angle)

    def correctAngle(self, angle):
        if angle < 0:
            angle = angle + 2*math.pi
        elif angle > 2*math.pi:
            angle = angle - 2*math.pi
        return angle

    def rayCast(self, screen, angle, player_pos, offset, player_angle):

        angle = self.correctAngle(angle)
        angle_diff =  self.correctAngle(player_angle - angle)

        px = player_pos[0]
        py = player_pos[1]
        check_hor = True
        check_vert = True

        # Check horizontal lines
        if angle > math.pi and angle < math.pi*2:
            ry = py - py%50
            rx = px - (py-ry)/math.tan(angle) 
            oy = -50
            ox = oy/math.tan(angle) 
        elif angle < math.pi and angle > 0:
            ry = py - py%50 + 50
            rx = px - (py-ry)/math.tan(angle) 
            oy = 50
            ox = oy/math.tan(angle) 
        else:
            ry=py + 1000
            rx=px + 1000
            check_hor = False
        if check_hor:
            for i in range(16):
                mx = int(rx//50)
                my = int(ry//50)
                if ry < py:
                    my -= 1
                if mx>= 0 and mx < len(MAP[0]) and my>=0 and my<len(MAP):
                    if MAP[my][mx] == '1':
                        break
                ry += oy 
                rx += ox

        hor_ry = ry
        hor_rx = rx
        hypo_hor = math.sqrt(math.pow(py-ry,2) + math.pow(px-rx,2))
        # Check vertical lines
        
        if angle > math.pi/2 and angle < 3*math.pi/2:
            rx = px - px%50
            ry = py - (px-rx)*math.tan(angle) 
            ox = -50
            oy = ox*math.tan(angle) 
        elif angle < 3*math.pi/2 or angle > math.pi/2:
            rx = px - px%50 + 50
            ry = py - (px-rx)*math.tan(angle) 
            ox = 50
            oy = ox*math.tan(angle) 
        else:
            ry=px
            rx=py
            check_vert = False
        
        if check_vert:
            for i in range(16):
                mx = int(rx//50)
                my = int(ry//50)
                if rx < px:
                    mx -= 1
                if mx>= 0 and mx < len(MAP[0]) and my>=0 and my<len(MAP):
                    if MAP[my][mx] == '1':
                        break
                ry += oy 
                rx += ox
        
        ver_ry = ry
        ver_rx = rx
        hypo_ver = math.sqrt(math.pow(py-ry,2) + math.pow(px-rx,2))
        if hypo_ver < hypo_hor:
            dist = hypo_ver
            color = DARK_GREEN
            rx = ver_rx
            ry = ver_ry
            pygame.draw.line(screen,RED,(px,py),(ver_rx,ver_ry))
        else:
            dist = hypo_hor
            color = GREEN
            rx = hor_rx
            ry = hor_ry
            pygame.draw.line(screen,GREEN,(px,py),(hor_rx,hor_ry))
        
        #display 3d
        regular_dist = dist
        dist = dist*math.cos(angle_diff)
        rect_height = 600 / dist if dist > 0 else 600
        rect_height = rect_height*40
        pixel = rect_height/50
        for i in range(50):
            color = BRICK_COLORS[BRICK_TEXTURE[i][int(ry%50)]] if hypo_ver < hypo_hor else BRICK_COLORS_DARK[BRICK_TEXTURE[i][int(rx%50)]]
            rect = pygame.Rect(offset*5 + WIDTH, HEIGHT/2 - rect_height/2 + i*pixel, 5, pixel*2 )
            pygame.draw.rect(screen,color, rect)

        # Floor Needs work

        # if rect_height < 600:
        #     dy = 600
        #     for i in range(int(600 - rect_height/2 - HEIGHT/2)):
        #         tx = px + math.cos(angle)*i
        #         ty = py + math.sin(angle)*i
        #         if MAP_FLOOR[int(ty//50)][int(tx//50)] == '1':
        #             color = BRICK_COLORS_GREY[BRICK_TEXTURE[int(ty%50)][int(tx%50)]]
        #         else:
        #             color = BRICK_COLORS_DARK[BRICK_TEXTURE[int(ty%50)][int(tx%50)]]
        #         rect = pygame.Rect(offset*5 + WIDTH, 600 - i, 5, i*2)
        #         pygame.draw.rect(screen, color, rect)
                
