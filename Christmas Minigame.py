import pygame, sys, time
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
font = pygame.font.SysFont(None, 30)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
collected = [0,0,0,0,0,0,0,0]
# [0,0,0,0,0,0,0,0]   [1,1,1,1,1,1,1,1]
move_x = 0
move_y = 0 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 30)
RED = (255, 0, 0)
BLUE = (96, 198, 221)
YELLOW =(221, 232, 78)
GRAY = (161,149,149)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def main_menu():
    
    Click = False
    while True:
        screen.fill((BLUE))
        mx, my = pygame.mouse.get_pos()

        draw_text('Christmas Mania', pygame.font.SysFont(None, 80), (BLACK), screen, 45, 100)

        draw_text('Made by Erik', font, (BLACK), screen, 50, 200)
        button_1 = pygame.draw.rect(screen, BLACK, (100,300,150,60))  
        button_2 = pygame.draw.rect(screen, BLACK, (350,300,150,60))
        draw_text('Play', pygame.font.SysFont(None, 80), (WHITE), screen, 100, 300)
        draw_text('Help', pygame.font.SysFont(None, 80), (WHITE), screen, 350, 300)
        if button_1.collidepoint((mx,my)):
            pygame.draw.rect(screen,(RED),(100,300,150,60),2)
            if Click:
                exit_location(0)
                level_1()
        if button_2.collidepoint((mx,my)):
            pygame.draw.rect(screen,(RED),(350,300,150,60),2)
            if Click:
               help()
                
        if button_2.collidepoint((mx,my)):
            pass

        Click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
        pygame.display.update()
        clock.tick(165)
def help():
    Click = False
    running = True
    while running:
        screen.fill((BLUE))
        
        draw_text('Santa had his christmas tree robbed', pygame.font.SysFont(None, 20), (BLACK), screen, 45, 100)

        draw_text('he needs your help to bring back the presents and ornaments ', pygame.font.SysFont(None, 20), (BLACK), screen, 50, 200)
        draw_text('As Santas little helper you accept his offer and set out into the world to find them', pygame.font.SysFont(None, 20), (BLACK), screen, 50, 300)
        
        Click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
        pygame.display.update()
        clock.tick(165)




def level_1():
    Click = False
    running = True
    global move_x
    global move_y
    up = False
    down = False
    left = False
    right = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_d:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = False  
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_d:
                    right = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
                    print(pygame.mouse.get_pos())
                    print(collected)
                    
            if up: 
                move_y -= 3
                if move_y <= 0:
                    move_y += 20
            if down:
                move_y += 3
                if move_y >= HEIGHT:
                    move_y += 20
            if left:
                move_x -= 3
                if move_x <= 0:
                    move_x += 20
                
            if right: 
                move_x += 3
                if move_x >= WIDTH:
                  move_x -= 20  
        screen.fill((GRAY))        
        snow = pygame.draw.rect(screen,(WHITE),(0,420,640,480))
        snow2 = pygame.draw.rect(screen,(WHITE),(0,300,580,50))
        snow3 = pygame.draw.rect(screen,(WHITE),(0,100,50,200))
        snow4 = pygame.draw.rect(screen,(WHITE),(100,120,200,100))
        snow5 = pygame.draw.rect(screen,(WHITE),(370,0,80,200))
        snow6 = pygame.draw.rect(screen,(WHITE),(445,120,120,80))
        objects = [snow, snow2, snow3, snow4, snow5, snow6]
        for i in range(len(objects)):
            if objects[i].collidepoint(move_x,move_y):
                if right:
                    move_x -= 20  
                if left:
                    move_x += 20
                if down:
                    move_y -= 20
                if up: 
                    move_y += 20
            
         
        

     
        elf(move_x,move_y)
        if collected[0] != 1:
            present(10,10)
        if move_x >= 10 and move_x <= 50 and move_y >= 10 and move_y <=50:
            collected[0] = 1
        
        if collected[1] != 1:
            orniment = pygame.draw.circle(screen,(BLACK),(550,40),20)
            if orniment.collidepoint(move_x,move_y):
                collected[1] = 1

        
        if move_y <= 100 and move_x <= 10:
            exit_location(3)
            level_2()
            
        
        
        
        pygame.display.update()
        clock.tick(165)

def level_2():
    Click = False
    running = True
    global move_x
    global move_y
    
    up = False
    down = False
    left = False
    right = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_d:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = False  
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_d:
                    right = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
                    print(pygame.mouse.get_pos())
                    print(collected)
            if up: 
                move_y -= 3
                if move_y <= 0:
                    move_y += 20
            if down:
                move_y += 3
                if move_y >= HEIGHT:
                    move_y += 20
            if left:
                move_x -= 3
                if move_x <= 0:
                    move_x += 20
                
            if right: 
                move_x += 3
                if move_x >= WIDTH:
                  move_x -= 20  
        screen.fill((GRAY))        
        snow = pygame.draw.rect(screen,(WHITE),(200,300,500,50))
        snow2 = pygame.draw.rect(screen,(WHITE),(0,150,50,200))
        snow3 = pygame.draw.rect(screen,(WHITE),(0,150,500,50))
        snow4 = pygame.draw.rect(screen,(WHITE),(0,420,680,480))
        snow5 = pygame.draw.rect(screen,(WHITE),(0,0,500,75))
        snow6 = pygame.draw.rect(screen,(WHITE),(600,0,500,300))

        objects = [snow, snow2, snow3, snow4, snow5,snow6]
        for i in range(len(objects)):
            if objects[i].collidepoint(move_x,move_y):
                if right:
                    move_x -= 20  
                if left:
                    move_x += 20
                if down:
                    move_y -= 20
                if up: 
                    move_y += 20
            
         
        

     
        elf(move_x,move_y)
        if collected[2] != 1:
            present(20,90)
        if move_x >= 20 and move_x <= 60 and move_y >= 90 and move_y <=140:
            collected[2] = 1
        
        if collected[3] != 1:
            orniment = pygame.draw.circle(screen,(YELLOW),(15,380),20)
            if orniment.collidepoint(move_x,move_y):
                collected[3] = 1
        if move_y <= 420 and move_x >= 630:
            exit_location(1)
            level_1()
        if move_y <= 150 and move_x <= 10:
            exit_location(5)
            level_4()
        if move_x <= 600 and move_x >= 500 and move_y <= 10:
            exit_location(6)
            level_3()
        
        pygame.display.update()
        clock.tick(165)

def level_3():
    Click = False
    running = True
    
    up = False
    down = False
    left = False
    right = False
    global move_x
    global move_y
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_d:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = False  
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_d:
                    right = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
                    print(pygame.mouse.get_pos())
                    print(collected)
            if up: 
                move_y -= 3
                if move_y <= 0:
                    move_y += 20
            if down:
                move_y += 3
                if move_y >= HEIGHT:
                    move_y += 20
            if left:
                move_x -= 3
                if move_x <= 0:
                    move_x += 20
                
            if right: 
                move_x += 3
                if move_x >= WIDTH:
                  move_x -= 20  
        screen.fill((GRAY))        
        snow = pygame.draw.rect(screen,(WHITE),(600,0,100,600))
        snow1= pygame.draw.rect(screen,(WHITE),(0,0,680,50))
        snow2 = pygame.draw.rect(screen,(WHITE),(0,0,50,600))
        snow3 = pygame.draw.rect(screen,(WHITE),(0,430,500,100))
        snow4 = pygame.draw.rect(screen,(WHITE),(430,150,75,600))
        snow5 = pygame.draw.rect(screen,(WHITE),(130,150,300,50))
        snow6 = pygame.draw.rect(screen,(WHITE),(130,200,50,150))
        snow7 = pygame.draw.rect(screen,(WHITE),(175,300,150,50))
        objects = [snow, snow1,snow2,snow3,snow4,snow5,snow6,snow7]
        for i in range(len(objects)):
            if objects[i].collidepoint(move_x,move_y):
                if right:
                    move_x -= 20  
                if left:
                    move_x += 20
                if down:
                    move_y -= 20
                if up: 
                    move_y += 20
            
         
        

     
        elf(move_x,move_y)
        if collected[4] != 1:
            present(195,215)
        if move_x >= 195 and move_x <= 245 and move_y >= 215 and move_y <=255:
            collected[4] = 1
        
        if collected[5] != 1:
            orniment = pygame.draw.circle(screen,(BLUE),(70,70),20)
        if orniment.collidepoint(move_x,move_y):
            collected[5] = 1

        if move_x <= 600 and move_x >= 500 and move_y >= 470:
            exit_location(4)
            level_2()
        
        
        
        
        pygame.display.update()
        clock.tick(165)

def level_4():
    Click = False
    running = True
    global move_x
    global move_y
    up = False
    down = False
    left = False
    right = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_d:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = False  
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_d:
                    right = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
                    print(pygame.mouse.get_pos())
                    print(collected)
            if up: 
                move_y -= 3
                if move_y <= 0:
                    move_y += 20
            if down:
                move_y += 3
                if move_y >= HEIGHT:
                    move_y += 20
            if left:
                move_x -= 3
                if move_x <= 0:
                    move_x += 20
                
            if right: 
                move_x += 3
                if move_x >= WIDTH:
                  move_x -= 20  
        screen.fill((GRAY))        
        snow = pygame.draw.rect(screen,(WHITE),(0,0,680,70))
        snow1 = pygame.draw.rect(screen,(WHITE),(0,70,75,500))
        snow2 = pygame.draw.rect(screen,(WHITE),(0,150,300,75))
        snow3 = pygame.draw.rect(screen,(WHITE),(225,220,75,100))
        snow4 = pygame.draw.rect(screen,(WHITE),(75,400,225,100))
        snow5 = pygame.draw.rect(screen,(WHITE),(400,150,300,75))
        snow6 = pygame.draw.rect(screen,(WHITE),(400,150,75,170))
        snow7 = pygame.draw.rect(screen,(WHITE),(585,150,75,400))
        snow8 = pygame.draw.rect(screen,(WHITE),(400,400,600,170))

        objects = [snow, snow1,snow2,snow3,snow4,snow5,snow6,snow7,snow8]
        for i in range(len(objects)):
            if objects[i].collidepoint(move_x,move_y):
                if right:
                    move_x -= 20  
                if left:
                    move_x += 20
                if down:
                    move_y -= 20
                if up: 
                    move_y += 20
            
         
        

     
        elf(move_x,move_y)
        if collected[6] != 1:
            present(115,260)
        if move_x >= 115 and move_x <= 165 and move_y >= 260 and move_y <=310:
            collected[6] = 1
        
        if collected[7] != 1:
            orniment = pygame.draw.circle(screen,(RED),(540,260),20)
            if orniment.collidepoint(move_x,move_y):
                collected[7] = 1

        if move_x >= 600 and move_y >= 75 and move_y <= 160:
            exit_location(2)
            level_2()
        if move_x >= 300 and move_x <= 400 and move_y >= 470:
            exit_location(7)
            level_5()
        
        
        
        
        pygame.display.update()
        clock.tick(165)
def level_5():
    Click = False
    running = True
    global move_x
    global move_y
    up = False
    down = False
    left = False
    right = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_d:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == pygame.K_w:
                    up = False  
                if event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_s:
                    down = False
                if event.key == pygame.K_d:
                    right = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
                    print(pygame.mouse.get_pos())
                    print(collected)
            if up: 
                move_y -= 3
                if move_y <= 0:
                    move_y += 20
            if down:
                move_y += 3
                if move_y >= HEIGHT:
                    move_y += 20
            if left:
                move_x -= 3
                if move_x <= 0:
                    move_x += 20
                
            if right: 
                move_x += 3
                if move_x >= WIDTH:
                  move_x -= 20  
        screen.fill((GRAY))        
        border = pygame.draw.rect(screen,(GRAY),(180,160,200,300))
        pygame.draw.polygon(screen,(GREEN),[[275,180],[200,350],[350,350]])
        pygame.draw.rect(screen,(BLACK),(250,350,50,50))
        snow1 = pygame.draw.rect(screen,(WHITE),(0,0,270,70))
        snow = pygame.draw.rect(screen,(WHITE),(380,0,300,70))
        snow3 =  pygame.draw.rect(screen,(WHITE),(0,0,100,600))
        snow2 =  pygame.draw.rect(screen,(WHITE),(550,0,100,700))
        objects = [border, snow, snow1, snow2, snow3]
        for i in range(len(objects)):
            if objects[i].collidepoint(move_x,move_y):
                if right:
                    move_x -= 20  
                if left:
                    move_x += 20
                if down:
                    move_y -= 20
                if up: 
                    move_y += 20
            
        if collected[0] == 1:
            pygame.draw.rect(screen,(RED),(210,360,25,25)) 
            pygame.draw.rect(screen,(YELLOW),(210,360+ 10 ,25,5))  
            pygame.draw.rect(screen,(YELLOW),(210 + 10,360 ,5,25))     

        if collected[1] == 1:
            pygame.draw.circle(screen,(BLACK),(250,240),10)
        if collected[2] == 1:
            pygame.draw.rect(screen,(RED),(315,360,25,25)) 
            pygame.draw.rect(screen,(YELLOW),(315,360+ 10 ,25,5))  
            pygame.draw.rect(screen,(YELLOW),(315 + 10,360 ,5,25))     

        if collected[3] == 1:
            pygame.draw.circle(screen,(YELLOW),(330,320),10)
        if collected[4] == 1:
            pygame.draw.rect(screen,(RED),(210,420,25,25)) 
            pygame.draw.rect(screen,(YELLOW),(210,420+ 10 ,25,5))  
            pygame.draw.rect(screen,(YELLOW),(210 + 10, 420 ,5,25))     

        if collected[5] == 1:
            pygame.draw.circle(screen,(BLUE),(220,310),10)
        if collected[6] == 1:
            pygame.draw.rect(screen,(RED),(310,420,25,25)) 
            pygame.draw.rect(screen,(YELLOW),(310,420+ 10 ,25,5))  
            pygame.draw.rect(screen,(YELLOW),(310 + 10,420 ,5,25))     

        if collected[7] == 1:
            pygame.draw.circle(screen,(RED),(310,250),10)
        

        

     
        elf(move_x,move_y)
        

        if move_x >= 300 and move_x <= 400 and move_y <= 10:
            exit_location(8)
            level_4()
        if move_x >= 100 and move_x <= 550 and move_y >= 470:
            
            level_6()
        
        
        
        
        pygame.display.update()
        clock.tick(165)

def level_6():
    Click = False
    running = True
    global move_x
    global move_y
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
                   
        mx,my = pygame.mouse.get_pos()  
        screen.fill((BLACK))  
        draw_text('You tell santa that you finished and he checks the tree...', pygame.font.SysFont(None, 20), (WHITE), screen, 45, 100)
        button = pygame.draw.rect(screen,(WHITE),(150,150,50,30))
        if button.collidepoint((mx,my)):
            pygame.draw.rect(screen,(RED),(150,150,50,30),1)
            if Click:      
                if sum(collected) == 8:
                        win()
                    

                elif sum(collected) <= 7:

                    draw_text('Santa says theres still some left.. click again to go back',pygame.font.SysFont(None, 40), (WHITE), screen, 45, 300)
                    
                    if Click:
                        exit_location(7)
                        level_5()

        

     

        

        
        
        
        
        
        pygame.display.update()
        clock.tick(165)
def win():
    Click = False
    running = True
    global move_x
    global move_y
    global collected
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    Click = True
                   
        mx,my = pygame.mouse.get_pos()  
        screen.fill((BLACK))  
        
        draw_text('you win would you like to start again?', pygame.font.SysFont(None, 20), (WHITE), screen, 45, 100)
        button = pygame.draw.rect(screen,(WHITE),(150,150,100,50))
        button2 = pygame.draw.rect(screen,(WHITE),(300,150,100,50))
        draw_text('Yes', pygame.font.SysFont(None, 40), (BLACK), screen, 150, 150)
        draw_text('No', pygame.font.SysFont(None, 40), (BLACK), screen, 300, 150)   
        if button.collidepoint((mx,my)):
            pygame.draw.rect(screen,(RED),(150,150,100,50),1)
            if Click:      
               
               exit_location(0)
               collected = [0,0,0,0,0,0,0,0]
               main_menu()
        if button2.collidepoint((mx,my)):
            pygame.draw.rect(screen,(RED),(300,150,100,50),1)
            if Click:  
                 
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(165)

def present(x,y):
    pygame.draw.rect(screen,(RED),(x,y,50,50)) 
    pygame.draw.rect(screen,(YELLOW),(x,y+ 20 ,50,10))  
    pygame.draw.rect(screen,(YELLOW),(x + 20,y ,10,50))     

def elf(x,y):
    pygame.draw.rect(screen,(RED),(x,y,20,30)) 
    pygame.draw.rect(screen,(215,183,135),(x,y - 20 ,20,20))
    pygame.draw.rect(screen,(GREEN),(x + 20 ,y ,5,10))
    pygame.draw.rect(screen,(GREEN),(x - 5 ,y ,5,10))
    pygame.draw.rect(screen,(BLACK),(x + 13 ,y - 10 ,2,2))
    pygame.draw.rect(screen,(BLACK),(x + 3 ,y - 10 ,2,2))
    
def exit_location(exit):
    global move_x
    global move_y
    if exit == 0:
        move_x = 15
        move_y = 375 
        #level 1 start   
    if exit == 1:
        move_x = 30
        move_y = 20
        #level 1 end
    elif exit == 2:
        move_x = 15
        move_y = 110
        #level 2 end to level 4 start
    elif exit == 3:
        move_x = 610
        move_y = 385
        #level 2 start
    elif exit == 4:
        move_x = 540 
        move_y = 30 
        #level 2 end to level 3 start
    elif exit == 5: 
        move_x = 585
        move_y = 100
        #level 4 start
    elif exit == 6:
        move_x = 530
        move_y = 420
        #level 3 start
    elif exit == 7:
        move_x = 330
        move_y = 20
    elif exit == 8:
        move_x = 330
        move_y = 420
        #level 4 ending
    
main_menu()
