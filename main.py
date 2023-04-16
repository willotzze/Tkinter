import pygame
pygame.init()
w = 1200
h = 700
sc = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
white = (200, 200, 200)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
vy = 20
ny = 620
lx = 200
px = 370
mis_x = 500
mis_y = 20
speed = 10


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            # if event.pos[0] >= px or event.pos[0] <= lx-170 or event.pos[1] >= ny or event.pos[1] <= vy:
            mis_x=event.pos[0]
            mis_y=event.pos[1]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        lx -= speed
        px -= speed
    if keys[pygame.K_RIGHT]:
        lx += speed
        px += speed
    if keys[pygame.K_UP]:
        vy -= speed
        ny -= speed
    if keys[pygame.K_DOWN]:
        vy += speed
        ny += speed

    sc.fill(white)
    pygame.draw.rect(sc, green, (lx, vy, 170, 200), 3)
    pygame.draw.rect(sc, green, (lx, vy + 200, 170, 200), 3)
    pygame.draw.rect(sc, green, (lx, vy + 400, 170, 200), 3)
    pygame.draw.rect(sc, green, (mis_x, mis_y, 170, 200), 3)
    pygame.draw.line(sc, blue, (lx, vy), (lx, ny))
    pygame.draw.line(sc, blue, (px, vy), (px, ny))
    if mis_x-10<=px<=mis_x+10:
        mis_x=px


    pygame.display.update()
    clock.tick(30)
