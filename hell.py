import pygame , sys , random , time 
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
password = str(random.randrange(1000,10000))

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 30)
RED = (255, 0, 0)
BLUE = (96, 198, 221)
YELLOW =(221, 232, 78)
GRAY = (161,149,149)
Global_score = 0
task1complete = 0 
font = pygame.font.SysFont(None, 30)
click = False
progress = 0
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
# ---------------------------
def main_menu():
    global Global_score
    click = False
    while True:
        click = False
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
                    click = True
    
        screen.fill((GRAY))
        draw_text('Space Station Chores', pygame.font.SysFont(None, 80), (BLACK), screen, 45, 100)
        draw_text('Your goal is to complete each task below to win!', font, (BLACK), screen, 50, 200)
        mx , my = pygame.mouse.get_pos()
        
        Button_1 = pygame.draw.rect(screen, BLACK,(10,300,200,100)) 
        Button_2 = pygame.draw.rect(screen, BLACK,(220,300,200,100))
        Button_3 = pygame.draw.rect(screen, BLACK,(430,300,200,100))
        draw_text("Task 1", pygame.font.SysFont(None, 50) ,GREEN,screen,50,330)
        draw_text("Task 2", pygame.font.SysFont(None, 50) ,GREEN,screen,270,330)
        draw_text("Task 3", pygame.font.SysFont(None, 50) ,GREEN,screen,480,330)
        if Global_score == 3:
            win()
        if Button_1.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(10,300,200,100),3)
            if click:
                task1()      
        if Button_2.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(220,300,200,100),3)
            if click:
                Global_score += 1
        if Button_3.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(430,300,200,100),3)
            if click:
                Global_score += 1
        
        progress = Global_score * 100
        percent = round((Global_score / 3) * 100)
        pygame.draw.rect(screen,GREEN,(150,30,progress,40))
        pygame.draw.rect(screen,BLACK,(150,30,300,40),2)
        draw_text(f"{percent} %", pygame.font.SysFont(None, 50) ,RED,screen,260,35)

        pygame.display.flip()
        clock.tick(60)
    
def task1():
    running = True
    passinput = ""
    click = False
    
    
    global Global_score
    while running: 
        click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
    
            
        screen.fill((GRAY))
        draw_text('Uploading Log files', font, (BLACK), screen, 20, 20)
        mx , my = pygame.mouse.get_pos()
        
        pygame.draw.rect(screen,(98,98,98),(50,50,500,400))
        stickynote = pygame.draw.rect(screen, YELLOW,(380,300,100,100))
        draw_text('click me!', font, (BLACK), screen, 390, 320)
        button_1 = pygame.draw.rect(screen,GRAY,(100,100,50,50))
        draw_text('1', font, (BLACK), screen, 100, 100)
        button_2 = pygame.draw.rect(screen,GRAY,(160,100,50,50))
        draw_text('2', font, (BLACK), screen, 160, 100)
        button_3 = pygame.draw.rect(screen,GRAY,(220,100,50,50))
        draw_text('3', font, (BLACK), screen, 220, 100)
        button_4 = pygame.draw.rect(screen,GRAY,(100,160,50,50))
        draw_text('4', font, (BLACK), screen, 100, 160)
        button_5 = pygame.draw.rect(screen,GRAY,(160,160,50,50))
        draw_text('5', font, (BLACK), screen, 160, 160)
        button_6 = pygame.draw.rect(screen,GRAY,(220,160,50,50))
        draw_text('6', font, (BLACK), screen, 220, 160)
        button_7 = pygame.draw.rect(screen,GRAY,(100,220,50,50))
        draw_text('7', font, (BLACK), screen, 100, 220)
        button_8 = pygame.draw.rect(screen,GRAY,(160,220,50,50))
        draw_text('8', font, (BLACK), screen, 160, 220)
        button_9 = pygame.draw.rect(screen,GRAY,(220,220,50,50))
        draw_text('9', font, (BLACK), screen, 220, 220)
        button_0 = pygame.draw.rect(screen,GRAY,(160,280,50,50))
        draw_text('0', font, (BLACK), screen, 160, 280)
        enter_button = pygame.draw.rect(screen,GREEN,(220,280,50,50))
        pygame.draw.rect(screen,BLACK,(290,100,150,60))
        

        if stickynote.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(380,300,100,100),3)
            if click:
                sticky_note()
        if button_0.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(160,280,50,50),2)
            if click:
                passinput += "0"
        if button_1.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(100,100,50,50),2)
            if click:
                passinput += "1"
        if button_2.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(160,100,50,50),2)
            if click:
                passinput += "2"
        if button_3.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(220,100,50,50),2)
            if click:
                passinput += "3"
        if button_4.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(100,160,50,50),2)
            if click:
                passinput += "4"
        if button_5.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(160,160,50,50),2)
            if click:
                passinput += "5"
        if button_6.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(220,160,50,50),2)
            if click:
                passinput += "6"
        if button_7.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(100,220,50,50),2)
            if click:
                passinput += "7"
        if button_8.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(160,220,50,50),2)
            if click:
                passinput += "8"
        if button_9.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(220,220,50,50),2)
            if click:
                passinput += "9"
        if enter_button.collidepoint((mx,my)):
            if click:
               if passinput != password:
                    passinput = ""
 
        if enter_button.collidepoint((mx,my)):
            if click:
               if passinput == password:
                    passinput = ""
                    loading()
                    return
                
    
        draw_text(f'{passinput}',pygame.font.SysFont(None, 60), (RED), screen, 300, 110)
    
        pygame.display.flip()
        clock.tick(60)

def sticky_note():

    running = True
    
    while running:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        
        
        screen.fill((YELLOW))
    
        draw_text(f'Todays password is {password}',pygame.font.SysFont(None, 60), (BLACK), screen, 100, 100) 
        
        pygame.display.flip()
        clock.tick(60)

def loading():
   running = True
   rect_x = 0
   loading = False 
   while running:
        screen.fill((GRAY))
        mx , my = pygame.mouse.get_pos()
        pygame.draw.rect(screen,(98,98,98),(50,50,500,400))
        unload = pygame.draw.rect(screen,GREEN,(200,210,210,60))
        
        

        draw_text("Unload files",pygame.font.SysFont(None, 50), (BLACK), screen, 210, 220) 
        
        if unload.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(200,210,210,60),2)
            if click:
                loading = True
                
                   

        
        if loading == True:    
                pygame.draw.rect(screen,RED,(100,300,0 + rect_x,50))  
                time.sleep(0.3)
                rect_x += 20
                if rect_x >= 421:
                    time.sleep(1)
                    loading = False
                    
                    task_complete()
                    return
                    
        pygame.draw.rect(screen,BLACK,(100 ,300,400 ,50),1)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
            
        pygame.display.flip()
        clock.tick(60)

def task_complete():
    global Global_score
    global task1complete
    running = True
    while running:
        
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.fill((GRAY))
       
        mx , my = pygame.mouse.get_pos()
        pygame.draw.rect(screen,(98,98,98),(50,50,500,400))
        draw_text("Task Complete!",font, (BLACK), screen, 190, 130)
        draw_text("Click below to continue:",font, (BLACK), screen, 130, 170)
        
        unload = pygame.draw.rect(screen,BLUE,(160,220,200,100))
        draw_text("Return",pygame.font.SysFont(None, 70), (BLACK), screen, 180, 240)
        if unload.collidepoint((mx,my)):
            pygame.draw.rect(screen,RED,(160,220,200,100),2)
            if click:
                if task1complete == 0:
                    Global_score += 1
                    task1complete = 1
                return 
            
        pygame.display.flip()
        clock.tick(60)

def win():
    click = False
    global Global_score
    global progress
    global percent 
    global task1complete
    running = True

    while running:
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        screen.fill((GRAY))
        mx , my = pygame.mouse.get_pos()
        progress = Global_score * 100
        percent = round((Global_score / 3) * 100)
        pygame.draw.rect(screen,GREEN,(150,30,progress,40))
        pygame.draw.rect(screen,BLACK,(150,30,300,40),2)
        draw_text('Congrats you beat all tasks!',pygame.font.SysFont(None, 60), (BLACK), screen, 50, 100)
        draw_text('Start Again?',pygame.font.SysFont(None, 60), (BLACK), screen, 200, 150)
        
        draw_text(f"{percent} %", pygame.font.SysFont(None, 50) ,RED,screen,260,35)

        Quit = pygame.draw.rect(screen, BLACK,(350,300,200,100))
        Restart = pygame.draw.rect(screen, BLACK,(100,300,200,100))
        draw_text('Yes',pygame.font.SysFont(None, 60), (WHITE), screen, 160, 330)
        draw_text('No',pygame.font.SysFont(None, 60), (WHITE), screen, 420, 330)
        if Quit.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(350,300,200,100),2)
            if click:
                pygame.quit()
                sys.exit()
        if Restart.collidepoint((mx,my)):
            pygame.draw.rect(screen, RED,(100,300,200,100),2)
            if click:
                Global_score = 0
                task1complete = 0
                return
                
        

        
        
            
        pygame.display.flip()
        clock.tick(60)

main_menu()
