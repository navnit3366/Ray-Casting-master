
FPS = 90

PLAYER_MOVMENT = 2
WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
GREY = (153,153,153)
GREEN = (0, 201, 47)
DARK_GREEN = (0, 153, 36)
PLAYER_COLOR = (50, 168, 82)
RED = (168, 50, 50)

#loadmap
MAP = []
with open("map.txt") as file:
    data = file.read().split('\n')
    for row in data:
        MAP.append([char for char in row])
MAP_FLOOR = []
with open("map_floor.txt") as file:
    data = file.read().split('\n')
    for row in data:
        MAP_FLOOR.append([char for char in row])

BRICK_TEXTURE = []
with open(f"textures/brick.txt") as file:
        data = file.read().split('\n')
        for row in data:
            BRICK_TEXTURE.append([char for char in row])
BRICK_COLORS = {}
with open (f"textures/brick_colors.txt") as file:
        data = file.read().split('\n')
        for i,row in enumerate(data):
            colors = row[row.find('-')+2:].split(',')
            colors = (int(colors[0]), int(colors[1]), int(colors[2]))
            BRICK_COLORS[str(i+1)] = colors
BRICK_COLORS_DARK = {}
for key in BRICK_COLORS.keys():
    BRICK_COLORS_DARK[key] = (BRICK_COLORS[key][0] * 0.6,  BRICK_COLORS[key][1] *0.6, BRICK_COLORS[key][2]*0.6)
BRICK_COLORS_GREY = {
    '1': (200,200,200),
    '2': (180,180,180),
    '3': (140,140,140),
    '4': (100,100,100),
    '5': (20,20,20)
}
    
