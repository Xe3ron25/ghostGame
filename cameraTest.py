import sys, pygame
from pygame.locals import *
pygame.init()


resolution = (800, 600)
screen = pygame.display.set_mode(resolution)

#making the square
camPos = pygame.Rect(pygame.Rect(0, 0, 20, 20))
color = (255, 0, 0)

clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        # track mouse movement
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            camPos.x = pos[0]
            camPos.y = pos[1]

        #click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Flash")
            color = (0, 255, 0)
            #cam flash
            flash = pygame.draw.circle(screen, (255,255,255), (camPos.x, camPos.y), 30)

        #unclick
        if event.type == pygame.MOUSEBUTTONUP:
            print("done")
            color = (255, 0, 0)
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    screen.fill(color=(0, 0, 0))



    cameraPosition = pygame.draw.rect(screen, color, (camPos))

    pygame.display.flip()

    clock.tick(60)