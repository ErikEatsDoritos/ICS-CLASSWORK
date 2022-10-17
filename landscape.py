# pygame template

import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 30)
RED = (255, 0, 0)
BLUE = (96, 198, 221)
YELLOW =(221, 232, 78)
GRAY = (161,149,149)
BROWN = (94,58,4)
DBLUE = (21,46,82)
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
pygame.display.set_caption("City Landscape")
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
rect_move = 0


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    rect_x = 0
    rect_y = 0
   
    # DRAWING
    screen.fill((25,77,250))  # always the first drawing command
    # sun

    pygame.draw.circle(screen,(YELLOW),(30,50),75)

    # building 1
    pygame.draw.rect(screen,GRAY,(20,150,150,500))
    pygame.draw.rect(screen,BLACK,(20,150,150,500),2)

    for i in range(5):
        rect_x += 27
        rect_y = 0
        for j in range(10):
            pygame.draw.rect(screen,BLUE,(rect_x + 7 , rect_y +160 ,20,20))
            rect_y += 27
    
    #building 2 
    pygame.draw.rect(screen,GRAY,(200,50,100,500))
    pygame.draw.rect(screen,BLACK,(200,50,100,500),2)

    rect_x = 188
    for i in range(3):
        rect_x += 27
        rect_y = 0
        for j in range(15):
            pygame.draw.rect(screen,BLUE,(rect_x , rect_y + 55 ,20,20))
            rect_y += 27
    # building 3 
    pygame.draw.rect(screen,GRAY,(350,200,250,500))
    pygame.draw.rect(screen,BLACK,(350,200,250,500),2)

    rect_x = 330
    for i in range(9):
        rect_x += 27
        rect_y = 0
        for j in range(7):
            pygame.draw.rect(screen,BLUE,(rect_x , rect_y + 210 ,20,20))
            rect_y += 27
    
    # bridge
    pygame.draw.line(screen,(BROWN),[0,300],[680,300],25)
    
    rect_x = 0
    rect_y = 0

    while rect_x < 600:
        pygame.draw.rect(screen,BROWN,(rect_x + 50,310,100,25))
        pygame.draw.rect(screen,BROWN,(rect_x + 75,335,50,100))
        rect_x += 150
    
    # monorail 
    
    pygame.draw.rect(screen,DBLUE,(50 + rect_move,240,150,48))
    pygame.draw.polygon(screen,DBLUE,[[50 + rect_move,240],[50 + rect_move,287],[30 + rect_move,287]])
    pygame.draw.polygon(screen,DBLUE,[[200 + rect_move,240],[200 + rect_move,287],[220 + rect_move,287]])
    pygame.draw.line(screen,(139,186,255),[50 + rect_move,255],[200 + rect_move,255],10)
    pygame.draw.line(screen,(WHITE),[45 + rect_move,270],[205 + rect_move,270],3)
    pygame.draw.line(screen,(WHITE),[45 + rect_move,275],[205 + rect_move,275],3)
    rect_move += 1 

    if rect_move == 800:
        rect_move = -220
    
    # ground
    pygame.draw.rect(screen,(161,160,180),(0,400,640,100))
    pygame.draw.line(screen,(BLACK),[0,400],[680,400],2)

    #cloud
    
    pygame.draw.circle(screen,(WHITE),(500,50),40)
    pygame.draw.circle(screen,(WHITE),(450,50),45)
    pygame.draw.circle(screen,(WHITE),(400,50),30)

    

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(165)
    #---------------------------


pygame.quit()
