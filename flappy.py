import pygame, sys, random
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((500, 600))
wall = pygame.image.load('wall.png')
wall2 = pygame.image.load('wall.png')
wall3 = pygame.image.load('wall.png')
wall4 = pygame.image.load('wall.png')
wall5 = pygame.image.load('wall.png')
wall6 = pygame.image.load('wall.png')
wall7 = pygame.image.load('wall.png')
player = pygame.image.load('player1.png')
player1 = pygame.image.load('player1.png')

wall_x = 440
wall_y = 10
 
wall_x2 = 440
wall_y2 = 70

wall_x3 = 440
wall_y3 = 200

wall_x4 = 440
wall_y4 = 450

wall_x5 = 440
wall_y5 = 500

wall_x6 = 440
wall_y6 = 500

wall_x7 = 440
wall_y7 = 500

player_x = 20
player_y = 300

player1_x = 20
player1_y = 500

score = 0
myfont = pygame.font.SysFont("monospace", 16)
time = 0

while True:
    if wall_x < -50:
        wall_x = random.randint(300, 600)
        wall_y = random.randint(0, 540)
    if wall_x2 < -50:
        wall_x2 = random.randint(300, 600)
        wall_y2 = random.randint(0, 540)
    if wall_x3 < -50:
        wall_x3 = random.randint(300, 600)
        wall_y3 = random.randint(0, 540)
    if wall_x4 < -50:
        wall_x4 = random.randint(300, 600)
        wall_y4 = random.randint(0, 540)
    if wall_x5 < -50:
        wall_x5 = random.randint(300, 600)
        wall_y5 = random.randint(0, 540)
    if wall_x6 < -50:
        wall_x6 = random.randint(300, 600)
        wall_y6 = random.randint(0, 540)
    if wall_x7 < -50:
        wall_x7 = random.randint(300, 600)
        wall_y7 = random.randint(0, 540)
    else:
        wall_x -= .45
        wall_x2 -= .45
        wall_x3 -= .45
        wall_x4 -= .45
        wall_x5 -= .45
        wall_x6-= .45
        wall_x7 -= .45

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Lets player move smoothly
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player_y -= 0.5
        if player_y < 0:
            player_y += 0.5
    if keys[K_DOWN]:
        player_y += 0.5
        if player_y > 550:
            player_y -= 0.5
    if keys[K_RIGHT]:
        player_x += 0.5
        if player_x > 450:
            player_x -= 0.5
    if keys[K_LEFT]:
        player_x -= 0.5
        if player_x < 0:
            player_x += 0.5
    '''
    Adds a second player
    if keys[K_w]:
        player1_y -= 0.5
        if player1_x < 0:
            player1_x += 0.5
    if keys[K_s]:
        player1_y += 0.5
        if player1_x < 0:
            player1_x += 0.5
    '''

    # Checks if walls hit player and stops game
    
    if abs(player_x - wall_x)<= 40 and abs(player_y - wall_y) <= 40:
        break
    if abs(player_x - wall_x2)<= 40 and abs(player_y - wall_y2) <= 40:
        break
    if abs(player_x - wall_x3)<= 40 and abs(player_y - wall_y3) <= 40:
        break
    if abs(player_x - wall_x4)<= 40 and abs(player_y - wall_y4) <= 40:
        break
    if abs(player_x - wall_x5)<= 40 and abs(player_y - wall_y5) <= 40:
        break
    if abs(player_x - wall_x6)<= 40 and abs(player_y - wall_y6) <= 40:
        break
    if abs(player_x - wall_x7)<= 40 and abs(player_y - wall_y7) <= 40:
        break

    # Increases score when player passes wall
    if abs(player_x - wall_x)<= 40 and abs(pygame.time.get_ticks() - time) > 300:
        time = pygame.time.get_ticks()
        score += 100
        

    screen.fill((255,255,255))
    screen.blit(player, (player_x, player_y))
    #screen.blit(player1, (player1_x, player1_y))
    screen.blit(wall, (wall_x, wall_y))
    screen.blit(wall2, (wall_x2, wall_y2))
    screen.blit(wall3, (wall_x3, wall_y3))
    screen.blit(wall4, (wall_x4, wall_y4))
    screen.blit(wall5, (wall_x5, wall_y5))
    screen.blit(wall6, (wall_x6, wall_y6))
    screen.blit(wall7, (wall_x7, wall_y7))
    scoreText = myfont.render('Score: ' + str(score), 2, (0, 0, 0))
    screen.blit(scoreText, (200, 0))
    pygame.display.update()
