import pygame
pygame.init()
w = 1200
h = 700
sc = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
                               # цвета
white = (200, 200, 200)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
graund=h-70                           # уровень земли
jump=1
jump_1=30
jump_2=0
                            # поверхности
hero=pygame.Surface((40,50))
hero.fill(blue)

rect=hero.get_rect()
rect.bottom=h
rect.centerx=w/2

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = -jump_1
                print("hallo")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect.centerx-=20
    if keys[pygame.K_RIGHT]:
        rect.centerx+=20
    if keys[pygame.K_UP]:
        rect.bottom-=10
    if keys[pygame.K_DOWN]:
        rect.bottom+=10
    # if keys[pygame.K_SPACE]:
    #     jump=-jump_1
    if jump<0:
        rect.bottom += jump
        jump+=1
    if jump==0 and jump_2<=jump_1:
        rect.bottom+=jump_2
        jump_2+=1

    if jump_2>jump_1:
        jump=1
        jump_2=0

    # if jump==0:
    #     jump=20
    sc.fill(white)
    sc.blit(hero, rect)
    pygame.display.update()
    clock.tick(30)
