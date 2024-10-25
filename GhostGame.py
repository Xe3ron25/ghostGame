import pygame
import random
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,800))
artifact = pygame.Rect((380,380,20,20))

camPos = pygame.Rect(pygame.Rect(0, 0, 20, 20))
color = (255, 0, 0)

font = pygame.font.Font(None, 32)
font2 = pygame.font.Font(None, 64)
start_time = pygame.time.get_ticks()
speed_interval = 5000
last_speed = pygame.time.get_ticks()

ghostSpeed1 = 2
ghostSpeed2 = 2
ghostSpeed3 = 2
ghostSpeed4 = 2

ghost_speed = 0

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

def move_towards(target, ghost, ghost_speed):
    if ghost.x <= target.x:
        ghost.x += ghost_speed
    elif ghost.x >= target.x + target.width:
        ghost.x -= ghost_speed

    if ghost.y <= target.y:
        ghost.y += ghost_speed
    elif ghost.y >= target.y + target.height:
        ghost.y -= ghost_speed

while run:
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    timer_text = font.render(f'Time: {int(elapsed_time)}s', True, (255, 255, 255))
    lives_text = font.render(f"Lives:  {int(lives)}", True, (255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            camPos.x = pos[0]
            camPos.y = pos[1]


        if event.type == pygame.MOUSEBUTTONDOWN:
            color = (0, 255, 0)
            flash = pygame.draw.circle(screen, (255, 255, 255), (camPos.x, camPos.y), 30)

        # unclick
        if event.type == pygame.MOUSEBUTTONUP:
            color = (255, 0, 0)

    current_time = pygame.time.get_ticks()
    if current_time - last_speed >= speed_interval:
        ghost_speed = ghost_speed + .2
        last_speed = current_time

    if run:
        move_towards(artifact, ghost, ghostSpeed1)
        move_towards(artifact, ghost2, ghostSpeed2)
        move_towards(artifact, ghost3, ghostSpeed3)
        move_towards(artifact, ghost4, ghostSpeed4)

    if ghost.colliderect(artifact) == True:
        lives -= 1
        print("Lives: " + str(lives))
        ghost = spawn_ghost_x(1)

        speedChoice = random.randint(1, 10)
        print(speedChoice)
        if speedChoice <= 3:
            print("1 slow")
            ghostSpeed1 = 1 + ghost_speed
        elif 4 <= speedChoice <= 9:
            print("1 med")
            ghostSpeed1 = 2 + ghost_speed
        elif speedChoice == 10:
            print("1 fast")
            ghostSpeed1 = 3 + ghost_speed

        move_towards(artifact, ghost, ghostSpeed1)
    if ghost2.colliderect(artifact) == True:
        lives -= 1
        print("Lives: " + str(lives))
        ghost2 = spawn_ghost_x(2)

        speedChoice = random.randint(1, 10)
        print(speedChoice)
        if speedChoice <= 3:
            print("2 slow")
            ghostSpeed2 = 1 + ghost_speed
        elif 4 <= speedChoice <= 9:
            print("2 med")
            ghostSpeed = 2 + ghost_speed
        elif speedChoice == 10:
            print("2 fast")
            ghostSpeed2 = 3 + ghost_speed

        move_towards(artifact, ghost2, ghostSpeed2)
    if ghost3.colliderect(artifact) == True:
        lives -= 1
        print("Lives: " + str(lives))
        ghost3 = spawn_ghost_y(1)

        speedChoice = random.randint(1, 10)
        print(speedChoice)
        if speedChoice <= 3:
            print("3 slow")
            ghostSpeed3 = 1 + ghost_speed
        elif 4 <= speedChoice <= 9:
            print("3 med")
            ghostSpeed3 = 2 + ghost_speed
        elif speedChoice == 10:
            print("3 fast")
            ghostSpeed3 = 3 + ghost_speed

        move_towards(artifact, ghost3, ghostSpeed3)
    if ghost4.colliderect(artifact) == True:
        lives -= 1
        print("Lives: " + str(lives))
        ghost4 = spawn_ghost_y(1)

        speedChoice = random.randint(1, 10)
        print(speedChoice)
        if speedChoice <= 3:
            print("4 slow")
            ghostSpeed4 = 1 + ghost_speed
        elif 4 <= speedChoice <= 9:
            print("4 med")
            ghostSpeed4 = 2 + ghost_speed
        elif speedChoice == 10:
            print("4 fast")
            ghostSpeed4 = 3 + ghost_speed

        move_towards(artifact, ghost4, ghostSpeed4)
    if lives <= 0:
        pass
#camera reaction
    if camPos.colliderect(ghost) == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            ghost = spawn_ghost_x(1)

            speedChoice = random.randint(1, 10)
            print(speedChoice)
            if speedChoice <= 3:
                print("1 slow")
                ghostSpeed1 = 1 + ghost_speed
            elif 4 <= speedChoice <= 9:
                print("1 med")
                ghostSpeed1 = 2 + ghost_speed
            elif speedChoice == 10:
                print("1 fast")
                ghostSpeed1 = 3 + ghost_speed

            move_towards(artifact, ghost, ghostSpeed1)

    if camPos.colliderect(ghost2) == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            ghost2 = spawn_ghost_x(2)

            speedChoice = random.randint(1, 10)
            print(speedChoice)
            if speedChoice <= 3:
                print("2 slow")
                ghostSpeed2 = 1 + ghost_speed
            elif 4 <= speedChoice <= 9:
                print("2 med")
                ghostSpeed = 2 + ghost_speed
            elif speedChoice == 10:
                print("2 fast")
                ghostSpeed2 = 3 + ghost_speed

            move_towards(artifact, ghost2, ghostSpeed2)

    if camPos.colliderect(ghost3) == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            ghost3 = spawn_ghost_y(1)

            speedChoice = random.randint(1, 10)
            print(speedChoice)
            if speedChoice <= 3:
                print("3 slow")
                ghostSpeed3 = 1 + ghost_speed
            elif 4 <= speedChoice <= 9:
                print("3 med")
                ghostSpeed3 = 2 + ghost_speed
            elif speedChoice == 10:
                print("3 fast")
                ghostSpeed3 = 3 + ghost_speed

            move_towards(artifact, ghost3, ghostSpeed3)

    if camPos.colliderect(ghost4) == True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            ghost4 = spawn_ghost_y(2)

            speedChoice = random.randint(1, 10)
            print(speedChoice)
            if speedChoice <= 3:
                print("4 slow")
                ghostSpeed4 = 1 + ghost_speed
            elif 4 <= speedChoice <= 9:
                print("4 med")
                ghostSpeed4 = 2 + ghost_speed
            elif speedChoice == 10:
                print("4 fast")
                ghostSpeed4 = 3 + ghost_speed

            move_towards(artifact, ghost4, ghostSpeed4)

    screen.fill((0, 0, 0))
    screen.blit(timer_text, (0, 0))
    screen.blit(lives_text, (700,0))
    pygame.draw.rect(screen,(255,0,0) ,artifact)
    pygame.draw.rect(screen, (255,255,255), ghost)
    pygame.draw.rect(screen, (255, 255, 255), ghost2)
    pygame.draw.rect(screen, (255, 255, 255), ghost3)
    pygame.draw.rect(screen, (255, 255, 255), ghost4)
    cameraPosition = pygame.draw.rect(screen, color, (camPos))
    pygame.display.flip()
    clock.tick(60)

screen.fill((0, 0, 0))
final_time_text = font2.render(f'You lasted: {int(elapsed_time)}s', True, (255, 255, 255))
screen.blit(final_time_text, (290, 400))
pygame.display.flip()
pygame.time.delay(2000)
