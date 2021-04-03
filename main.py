import pygame
import random, sys

pygame.init()
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    K_ESCAPE,
    K_SPACE,
    QUIT
)

screen_width = 500
screen_height= 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake")

def end():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def menu(score):
    screen.fill((255, 255, 255))
    font = pygame.font.Font('freesansbold.ttf', 19)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                end()
                break
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game()
                    break
                if event.key == K_ESCAPE:
                    end()
                    break
        if score > 0:
            scoretext = font.render('Score: '+str(score), True, (0,0,0))
            scorepos = scoretext.get_rect()
            scorepos.center = (screen_width // 2, screen_height // 3)
            screen.blit(scoretext,scorepos)
        text = font.render("If you want to play press SPACE",True,(0,0,0))
        textpos = text.get_rect()
        textpos.center = (screen_width // 2, screen_height // 2)
        screen.blit(text,textpos)
        pygame.display.update()

def game():
    white = (255, 255, 255)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)

    score = 0
    fruit = True
    apple = pygame.image.load('img/apple.png')
    fruit_pos = []
    snake_pos = [200, 100]
    snake_body = [[200, 100], [200 - 10, 100], [200 - (2 * 10), 100]]
    time = pygame.time.Clock()
    move = 'left'
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    end()
                elif event.key == K_DOWN:
                    move = 'down'
                elif event.key == K_LEFT:
                    move = 'left'
                elif event.key == K_UP:
                    move = 'up'
                elif event.key == K_RIGHT:
                    move = 'right'
            if event.type == QUIT:
                end()
        scoretext = font.render('Score: '+str(score), True, blue)
        scorepos = scoretext.get_rect()
        scorepos.center = (250 // 2, 35 // 2)
        screen.fill((0,0,0))
        screen.blit(scoretext, scorepos)
        for i in snake_body:
            pygame.draw.rect(screen,white,(i[0],i[1],10,10))
        if fruit:
            fruit_pos = [random.randrange(20,screen_width-20),random.randrange(20,screen_height-20)]
            fruit = False
        screen.blit(apple, fruit_pos)
        snake_body.append(list(snake_pos))
        if pygame.Rect(snake_pos[0], snake_pos[1], 10, 10).colliderect(pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10)):
            fruit = True
            score +=1
        else:
            snake_body.pop(0)
        for i in snake_body[:-1]:
            if pygame.Rect(i[0],i[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
                game_on = False
        print(snake_pos)

        if snake_pos[0] == 0 or snake_pos[1]==0:
            game_on=False
        elif snake_pos[0] == screen_width+10 or snake_pos[1]== screen_height+10:
            game_on=False
        if move == 'right':
            snake_pos[0] += 10
        elif move == 'left':
            snake_pos[0] -= 10
        elif move == 'up':
            snake_pos[1] -= 10
        elif move == 'down':
            snake_pos[1] += 10
        pygame.display.update()
        time.tick(24)
    menu(score)

menu(0)