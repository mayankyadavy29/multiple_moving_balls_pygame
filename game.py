from config import pygame, screen, clock, height
from ball import Ball
from user import User
import sys

bg = pygame.image.load("background.jpg")
screen.blit(bg, (0, 0))

balls = list()
for i in range(4):
    balls.append(Ball(pygame.image.load("intro_ball.gif"), i*120, i+1))

user = User(pygame.image.load("hero.png"), height//2, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # To reset background
    for ball in balls:
        screen.blit(bg, ball.pos, ball.pos)
    screen.blit(bg, user.pos, user.pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        user.move(up=True)
    if keys[pygame.K_DOWN]:
        user.move(down=True)
    if keys[pygame.K_LEFT]:
        user.move(left=True)
    if keys[pygame.K_RIGHT]:
        user.move(right=True)
    screen.blit(user.img, user.pos)

    for ball in balls:
        ball.move()
        screen.blit(ball.img, ball.pos)
    pygame.display.update()
    clock.tick(60)