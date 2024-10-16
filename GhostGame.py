import pygame
import sys
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
#default speed
ghostSpeed1 = 2
ghostSpeed2 = 2
ghostSpeed3 = 2
ghostSpeed4 = 2
#speedName = ['slow1', 'med2', 'fast3']
#speedProb = [0.1,0.1,0.8] #[0.2,0.7,0.1]

def move_towards(target, ghost, ghostSpeed):

    if ghost.x <= target.x:
        ghost.x += ghostSpeed
    elif ghost.x >= target.x + target.width:
        ghost.x -= ghostSpeed

    if ghost.y <= target.y:
        ghost.y += ghostSpeed
    elif ghost.y >= target.y + target.height:
        ghost.y -= ghostSpeed

        #speedChoice = random.choices(speedName, speedProb)
        #if speedChoice == 'slow1':
        #    ghostSpeed = 1
        #elif speedChoice == 'med2':
        #    ghostSpeed = 2
        #elif speedChoice == 'fast3':
        #    ghostSpeed = 10


while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    #if run:
    move_towards(artifact, ghost, ghostSpeed1)
    move_towards(artifact, ghost2, ghostSpeed2)
    move_towards(artifact, ghost3, ghostSpeed3)
    move_towards(artifact, ghost4, ghostSpeed4)

    if ghost.colliderect(artifact) == True:
        #lives -= 1
        print("Lives: " + str(lives))
        ghost = spawn_ghost_x(1)

        speedChoice = random.randint(1, 10)
        print(speedChoice)
        if speedChoice <= 3:
            print("1 slow")
            ghostSpeed1 = 1
        elif 4 <= speedChoice <= 9:
            print("1 med")
            ghostSpeed1 = 3
        elif speedChoice == 10:
            print("1 fast")
            ghostSpeed1 = 5

        move_towards(artifact, ghost, ghostSpeed1)
    if ghost2.colliderect(artifact) == True:
        #lives -= 1
        print("Lives: " + str(lives))
        ghost2 = spawn_ghost_x(2)

        speedChoice = random.randint(1, 10)
        print(speedChoice)
        if speedChoice <= 3:
            print("2 slow")
            ghostSpeed2 = 1
        elif 4 <= speedChoice <= 9:
            print("2 med")
            ghostSpeed = 3
        elif speedChoice == 10:
            print("2 fast")
            ghostSpeed2 = 5

        move_towards(artifact, ghost2, ghostSpeed2)
    if ghost3.colliderect(artifact) == True:
        #lives -= 1
        print("Lives: " + str(lives))
        ghost3 = spawn_ghost_y(1)

        speedChoice = random.randint(1, 10)
        print(speedChoice)
        if speedChoice <= 3:
            print("3 slow")
            ghostSpeed3 = 1
        elif 4 <= speedChoice <= 9:
            print("3 med")
            ghostSpeed3 = 3
        elif speedChoice == 10:
            print("3 fast")
            ghostSpeed3 = 5

        move_towards(artifact, ghost3, ghostSpeed3)
    if ghost4.colliderect(artifact) == True:
        #lives -= 1
        print("Lives: " + str(lives))
        ghost4 = spawn_ghost_y(1)

        speedChoice = random.randint(1, 10)
        print(speedChoice)
        if speedChoice <= 3:
            print("4 slow")
            ghostSpeed4 = 1
        elif 4 <= speedChoice <= 9:
            print("4 med")
            ghostSpeed4 = 3
        elif speedChoice == 10:
            print("4 fast")
            ghostSpeed4 = 5

        move_towards(artifact, ghost4, ghostSpeed4)
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
