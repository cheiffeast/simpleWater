from pygame.locals import *
from random import randint
import pygame
width, height = 500, 500
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
Playing = True
fill = False
Offset = 400
ClickPower = 30
PConstant = 0.03
BaselineConstant = 0.01
Damping = 0.935
mass = 0.6
pointsNumber = 250
points = [[0, 0, mass] for i in range(pointsNumber)]
def updatePoints():
    global points
    for i in range(len(points)):
        try:
            dy = points[i + 1][0] - points[i][0]
            rF = PConstant * dy
        except:
            dy = 0 - points[i][0]
            rF = PConstant * dy
        try:
            dy = points[i - 1][0] - points[i][0]
            lF = PConstant * dy
        except:
            dy = 0 - points[i][0]
            lF = PConstant * dy
        
        dy = 0 - points[i][0]
        baselineForce = BaselineConstant * dy
        force = lF + rF + baselineForce
        force = Damping * points[i][1] + (force / points[i][2])
        points[i][1] = force
        points[i][0] += points[i][1]

def draw():
    global points
    
    screen.fill([255, 255, 255])
    
    updatePoints()
    for i in range(len(points)):
        if fill:
            pygame.draw.line(screen, [64, 164, 223], [i * (width / pointsNumber), width], [i * (width / pointsNumber), Offset + points[i][0]], int(width/pointsNumber))
    pygame.draw.aalines(screen, [64, 164, 223], False, [[i * (width / pointsNumber), Offset + points[i][0]] for i in range(len(points))], 50)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    m = pygame.mouse.get_pressed()
    if m[0] == 1:
        mp = pygame.mouse.get_pos()
        point = int(mp[0]/(width/pointsNumber))
        for i in range(-int(pointsNumber/50), int(pointsNumber/50), 1):
            points[point + i][0] = - ClickPower + abs(i)
        
    

    
    clock.tick(60)
    pygame.display.update()

while Playing:
    draw()
