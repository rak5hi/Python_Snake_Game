import pygame
import random
import time

pygame.init()

width, height = 1000, 800             #Full Screen - 1536 864
game_screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)   
pygame.display.set_caption("The Snake Game")

x, y = 200, 200    # intial coordinate 
delta_x, delta_y = 10, 0

food_x, food_y = random.randrange(0, 800)//10*10, random.randrange(0, 800)//10*10

body_list = [(x, y)]

game_over = False

font = pygame.font.SysFont("bahnschrift", 25)

clock = pygame.time.Clock()  #creating objeect

########################## sanke func #########################################
def snake():
    global x, y, food_x, food_y, game_over
    x = (x + delta_x)%width
    y = (y + delta_y)%height
    
    if((x, y) in body_list):
        game_over = True
        return
    
    body_list.append((x, y))
    
    if(food_x == x and food_y == y):
        while((food_x, food_y) in body_list):
            food_x, food_y = random.randrange(0, 800)//10*10, random.randrange(0, 800)//10*10
    else:
        del body_list[0]
    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (255, 0, 0), pygame.Rect(0, 0, 1010, 810), 1)     #drawing border
    
    score = font.render("Score: " + str(len(body_list)), True, (0, 255, 0))         #score   
    game_screen.blit(score, [800, 0])
    
    pygame.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 10, 10])
    for (i,j) in body_list:
        pygame.draw.rect(game_screen, (0, 255, 0), [i, j, 10, 10])
        pygame.draw.rect(game_screen, (0, 0, 0), [i, j, 10, 10 ], 1)
    pygame.display.update()

##################  MAIN LOOP  ###################
while True:
    if(game_over):
        game_screen.fill((0, 0, 0))
        score = font.render("Your Score: " + str(len(body_list)), True, (0, 255, 0))
        game_screen.blit(score, [420, 400])
        
        msg = font.render('GAME OVER!', True, (0, 255, 0))
        game_screen.blit(msg, [420,370])
        
        creator = font.render("game by rakshi", True, (0, 255, 0))
        pygame.display.update()
        time.sleep(3)
        
        game_screen.fill((0, 0, 0))
        game_screen.blit(creator, [410, 370])
        pygame.display.update()
        time.sleep(1.5)
        pygame.quit()
        quit()
        
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                pygame.quit()
                quit()
            if(event.key == pygame.K_LEFT):
                if(delta_x != 10):
                    delta_x = -10
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                if(delta_x != -10):
                    delta_x = 10
                delta_y = 0
            elif(event.key == pygame.K_UP):
                delta_x = 0
                if(delta_y != 10):
                    delta_y = -10
            elif(event.key == pygame.K_DOWN):
                delta_x = 0
                if(delta_y != -10):
                    delta_y = 10
            else:
                continue
            snake()
    if(not events):
        snake()
    clock.tick(15)    #frame rate as arg