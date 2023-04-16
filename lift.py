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
#     действия
jump=1
jump_1=30
jump_2=0
vhod_y=0
vhod_x=0
caunt=[]
work=""
#     этажи
vy = 20
ny = 620
lx = 200
px = 370
mis_x = 500
mis_y = 20
speed = 10
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
                jump =- jump_1
            if event.key ==pygame.K_v:
                vhod_y=1
            if event.key ==pygame.K_1:
                caunt+=["at_1"]
            if event.key ==pygame.K_2:
                caunt+=["at_2"]
            if event.key ==pygame.K_3:
                caunt+=["at_3"]
    keys = pygame.key.get_pressed()
    #         перемещение клавишами
    if keys[pygame.K_LEFT]:
        rect.centerx-=20
    if keys[pygame.K_RIGHT]:
        rect.centerx+=20
    if keys[pygame.K_UP]:
        rect.bottom-=10
    if keys[pygame.K_DOWN]:
        rect.bottom+=10
    #     вход в здание

    if len(caunt)>0:
        work=caunt[0]

    if vhod_y==1 and rect.centery>vy+500:
        rect.bottom-=4
        if rect.centery<=vy+500:
            vhod_y=0
            vhod_x=1
    if vhod_x==1:
        rect.centerx-=4
        if rect.centerx<=285:
            vhod_x=0
    if "at_2"==work:
        if rect.centery<=vy+300:
            rect.centery+=4
            if rect.centery>=vy+300:
                caunt = caunt[1:]
                work = ""
        if rect.centery>=vy+300:
            rect.centery-=4
            if rect.centery<=vy+300:
                caunt = caunt[1:]
                work = ""
    if "at_1"==work:
        if vy+495<=rect.centery<=vy+500:
            caunt=caunt[1:]
            work=""
        if rect.centery<=vy+500:
            rect.centery+=4
        if rect.centery >= vy + 500:
            rect.centery -= 4

    if "at_3"==work:
        if rect.centery<=vy+100:
            caunt = caunt[1:]
            work = ""
        rect.centery-=4



    if jump<0:
        rect.bottom += jump
        jump+=1
    if jump==0 and jump_2<=jump_1:
        rect.bottom+=jump_2
        jump_2+=1

    if jump_2>jump_1:
        jump=1
        jump_2=0

    sc.fill(white)
    sc.blit(hero, rect)
    pygame.draw.rect(sc, green, (lx, vy, 170, 200), 3)
    pygame.draw.rect(sc, green, (lx, vy + 200, 170, 200), 3)
    pygame.draw.rect(sc, green, (lx, vy + 400, 170, 200), 3)
    # pygame.draw.rect(sc, green, (mis_x, mis_y, 170, 200), 3)
    pygame.draw.line(sc, blue, (lx, vy), (lx, ny))
    pygame.draw.line(sc, blue, (px, vy), (px, ny))
    pygame.display.update()
    clock.tick(30)
