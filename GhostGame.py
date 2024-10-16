import pygame
import random
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,800))
artifact = pygame.Rect((380,380,20,20))

run = True
lives = 3

def spawn_ghost_x(num1):
    if num1 == 1:
        ghost_x = random.randint(0,750)
        return pygame.Rect((ghost_x, 0, 50, 50))
    elif num1 == 2:
        ghost_x = random.randint(0,750)
        return pygame.Rect((ghost_x, 750, 50, 50))

def spawn_ghost_y(num1):
    if num1 == 1:
        ghost_y = random.randint(0,750)
        return pygame.Rect((0, ghost_y, 50, 50))
    elif num1 == 2:
        ghost_y = random.randint(0,750)
        return pygame.Rect((750, ghost_y, 50, 50))

ghost = spawn_ghost_x(1)
ghost2 = spawn_ghost_x(2)
ghost3 = spawn_ghost_y(1)
ghost4 = spawn_ghost_y(2)

def move_towards(target, ghost):
    if ghost.x <= target.x:
        ghost.x += 2
    elif ghost.x >= target.x + target.width:
        ghost.x -= 2

    if ghost.y <= target.y:
        ghost.y += 2
    elif ghost.y >= target.y + target.height:
        ghost.y -= 2

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    if run:
        move_towards(artifact, ghost)
        move_towards(artifact, ghost2)
        move_towards(artifact, ghost3)
        move_towards(artifact, ghost4)

    if ghost.colliderect(artifact) == True:
        lives -= 1
        print("Lives: " + str(lives))
        ghost = spawn_ghost_x(1)
    if ghost2.colliderect(artifact) == True:
        lives -= 1
        print("Lives: " + str(lives))
        ghost2 = spawn_ghost_x(2)
    if ghost3.colliderect(artifact) == True:
        lives -= 1
        print("Lives: " + str(lives))
        ghost3 = spawn_ghost_y(1)
    if ghost4.colliderect(artifact) == True:
        lives -= 1
        print("Lives: " + str(lives))
        ghost4 = spawn_ghost_y(1)
    if lives <= 0:
        run = False


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(255,0,0) ,artifact)
    pygame.draw.rect(screen, (255,255,255), ghost)
    pygame.draw.rect(screen, (255, 255, 255), ghost2)
    pygame.draw.rect(screen, (255, 255, 255), ghost3)
    pygame.draw.rect(screen, (255, 255, 255), ghost4)
    pygame.display.flip()
    clock.tick(60)
