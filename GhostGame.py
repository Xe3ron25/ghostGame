import pygame
import random
import time
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800,800))
artifact = pygame.Rect((380,380,20,20))

cameraFlash = pygame.mixer.Sound("camera-flash-204151.mp3")
ghostSigh = pygame.mixer.Sound("ghost-sigh (1).mp3")
deathLaugh = pygame.mixer.Sound("death-laugh.mp3")
laugh = 1
victoryTheme = pygame.mixer.Sound("victory.mp3")

pygame.mixer.music.load("menu.mp3")
pygame.mixer.music.play(-1)

ghost_image = pygame.image.load("ghost.png").convert_alpha()
ghost_image = pygame.transform.scale(ghost_image, (50, 50))
ghostboss_image = pygame.image.load("ghostboss.png").convert_alpha()
ghostboss_image = pygame.transform.scale(ghostboss_image, (75, 75))
camera_image = pygame.image.load("camera.png").convert_alpha()
camera_image = pygame.transform.scale(camera_image, (25, 20))
camPos = pygame.Rect(pygame.Rect(0, 0, 25, 20))
center_image = pygame.image.load("centerpiece.png").convert_alpha()
center_image = pygame.transform.scale(center_image, (40, 40))

clock = pygame.time.Clock()
start_time = time.time()

speedDuringBoss = False

pygame.mouse.set_visible(False)
#camPos = pygame.Rect(pygame.Rect(0, 0, 20, 20))
color = (255, 0, 0)

font = pygame.font.Font(None, 32)
font2 = pygame.font.Font(None, 64)

#speed_interval = 5000
#last_speed = pygame.time.get_ticks()
#elapsed_time = 0

ghostSpeed1 = 1
ghostSpeed2 = 1
ghostSpeed3 = 1
ghostSpeed4 = 1
bossSpeed = 0

ghost_speed = 0

bossGhost = False

gameState = 1
#1=menu
#2=instructions
#3=game
#4=endscreen
gameStart = False

lives = 5
bossHealth = 18

killCount = 0

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

def spawn_boss(spawn):
    if spawn == 0:
        boss_x = 1000
        boss_y = 1000
    if spawn == 1:
        spawn_boss_x = [0,725]
        boss_x = random.choice(spawn_boss_x)
        spawn_boss_y = [0, 725]
        boss_y = random.choice(spawn_boss_y)
    return pygame.Rect((boss_x, boss_y, 75, 75))

ghost = spawn_ghost_x(1)
ghost2 = spawn_ghost_x(2)
ghost3 = spawn_ghost_y(1)
ghost4 = spawn_ghost_y(2)
bossNum = 0
ghostBoss = spawn_boss(bossNum)

def move_towards(target, ghost, ghost_speed):
    if ghost.x <= target.x:
        ghost.x += ghost_speed
    elif ghost.x >= target.x + target.width:
        ghost.x -= ghost_speed

    if ghost.y <= target.y:
        ghost.y += ghost_speed
    elif ghost.y >= target.y + target.height:
        ghost.y -= ghost_speed
while gameState != 6:
    while gameState == 1: #menu
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = 6 #full quit
                if event.key == pygame.K_1: #start
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("game-music.mp3")
                    pygame.mixer.music.play(-1)
                    gameState = 3
                if event.key == pygame.K_2: #instructions
                    gameState = 2


        screen.fill((0, 0, 0))
        title = font2.render('Ghost Game', True,(255, 255, 255))
        screen.blit(title, (250, 200))
        startText = font.render("Start: 1", True, (255,255,255))
        screen.blit(startText, (340, 400))
        instructText = font.render("Instructions: 2", True, (255,255,255))
        screen.blit(instructText, (305, 450))
        quitText = font.render("Quit: esc", True, (255, 255, 255))
        screen.blit(quitText, (325, 600))
        pygame.display.flip()
        laugh = 1


    while gameState == 2:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = 6  # full quit
                if event.key == pygame.K_1:  # start
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("game-music.mp3")
                    pygame.mixer.music.play(-1)
                    gameState = 3

        screen.fill((0, 0, 0))
        instructLine1 = font.render("Stop the ghosts from reaching the crystal by flashing them with the", True, (255, 255, 255))
        screen.blit(instructLine1, (40, 180))
        instructLine2 = font.render("camera. Each time they reach the crystal, you lose a life. If you lose", True, (255, 255, 255))
        screen.blit(instructLine2, (40, 210))
        instructLine3 = font.render("them all, you lose.", True,(255, 255, 255))
        screen.blit(instructLine3, (40, 240))
        instructLine4 = font.render("After a certain amount of kills, the boss will spawn. Defeat him", True, (255, 255, 255))
        screen.blit(instructLine4, (40, 280))
        instructLine5 = font.render("before he reaches you or you will lose. (will take multiple flashes)",True, (255, 255, 255))
        screen.blit(instructLine5, (40, 310))
        instructLine6 = font.render("Camera Flash: left-click (tip: sometimes the flash may not work, It",True, (255, 255, 255))
        screen.blit(instructLine6, (40, 350))
        instructLine6 = font.render("is more reliable to aim to the prt of the ghost closest to you.",True, (255, 255, 255))
        screen.blit(instructLine6, (40, 380))
        startText = font.render("Start: 1", True, (255, 255, 255))
        screen.blit(startText, (330, 550))
        quitText = font.render("Quit: esc", True, (255, 255, 255))
        screen.blit(quitText, (325, 600))
        pygame.display.flip()

    while gameState == 3:
        #timer
        if not gameStart:
            start_time = time.time()
            gameStart = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = 6 #full quit
                if event.key == pygame.K_b:
                    bossGhost = True
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                camPos.x = pos[0] - camera_image.get_width() // 2
                camPos.y = pos[1] - camera_image.get_height() // 2


            if event.type == pygame.MOUSEBUTTONDOWN:
                #color = (0, 255, 0)
                flash = pygame.draw.circle(screen, (255, 255, 255), (camPos.x, camPos.y), 30)
                cameraFlash.play()

            # unclick
            if event.type == pygame.MOUSEBUTTONUP:
                color = (255, 0, 0)



        current_time = pygame.time.get_ticks()

        elapsed_time = (time.time() - start_time)
        elapsed_minutes = int(elapsed_time // 60)
        elapsed_seconds = elapsed_time % 60

        #pygame.mixer.music.load("game-music.mp3")
        #pygame.mixer.music.play(-1)

        if killCount == 20:
            bossGhost = True
            speedDuringBoss = True


        #if bossGhost == True:
         #   print("boss")
            #ghost_speed = -.75

        #elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        timer_text = font.render(f"Time: {elapsed_minutes:02d}:{elapsed_seconds:05.2f}", True, (255, 255, 255))

        lives_text = font.render(f"Lives:  {int(lives)}", True, (255,255,255))



        #if gameState == 3:
        move_towards(artifact, ghost, ghostSpeed1)
        move_towards(artifact, ghost2, ghostSpeed2)
        move_towards(artifact, ghost3, ghostSpeed3)
        move_towards(artifact, ghost4, ghostSpeed4)


        if bossGhost == True:
            bossNum = 1
            ghostBoss = spawn_boss(bossNum)
            bossSpeed = 1
            killCount += 1
            bossGhost = False

        move_towards(artifact, ghostBoss, bossSpeed)

        if ghostBoss.colliderect(artifact) == True:
            lives = 0


        if ghost.colliderect(artifact) == True:
            ghostSigh.play()
            lives -= 1
            print("Lives: " + str(lives))
            ghost = spawn_ghost_x(1)

            if speedDuringBoss == False:
                speedChoice = random.randint(1, 10)
            elif speedDuringBoss == True:
                speedChoice = 1
            #print(speedChoice)
            if speedChoice <= 3:
                #print("1 slow")
                ghostSpeed1 = 1 + ghost_speed
            elif 4 <= speedChoice <= 9:
                #print("1 med")
                ghostSpeed1 = 2 + ghost_speed
            elif speedChoice == 10:
                #print("1 fast")
                ghostSpeed1 = 2 + ghost_speed

            move_towards(artifact, ghost, ghostSpeed1)

        if ghost2.colliderect(artifact) == True:
            ghostSigh.play()
            lives -= 1
            print("Lives: " + str(lives))
            ghost2 = spawn_ghost_x(2)

            if speedDuringBoss == False:
                speedChoice = random.randint(1, 10)
            elif speedDuringBoss == True:
                speedChoice = 1
            #print(speedChoice)
            if speedChoice <= 3:
                #print("2 slow")
                ghostSpeed2 = 1 + ghost_speed
            elif 4 <= speedChoice <= 9:
                #print("2 med")
                ghostSpeed = 2 + ghost_speed
            elif speedChoice == 10:
                #print("2 fast")
                ghostSpeed2 = 2 + ghost_speed

            move_towards(artifact, ghost2, ghostSpeed2)

        if ghost3.colliderect(artifact) == True:
            ghostSigh.play()
            lives -= 1
            print("Lives: " + str(lives))
            ghost3 = spawn_ghost_y(1)

            if speedDuringBoss == False:
                speedChoice = random.randint(1, 10)
            elif speedDuringBoss == True:
                speedChoice = 1
            #print(speedChoice)
            if speedChoice <= 3:
                #print("3 slow")
                ghostSpeed3 = 1 + ghost_speed
            elif 4 <= speedChoice <= 9:
                #print("3 med")
                ghostSpeed3 = 2 + ghost_speed
            elif speedChoice == 10:
                #print("3 fast")
                ghostSpeed3 = 2 + ghost_speed

            move_towards(artifact, ghost3, ghostSpeed3)

        if ghost4.colliderect(artifact) == True:
            ghostSigh.play()
            lives -= 1
            print("Lives: " + str(lives))
            ghost4 = spawn_ghost_y(2)

            if speedDuringBoss == False:
                speedChoice = random.randint(1, 10)
            elif speedDuringBoss == True:
                speedChoice = 1
            #print(speedChoice)
            if speedChoice <= 3:
                #print("4 slow")
                ghostSpeed4 = 1 + ghost_speed
            elif 4 <= speedChoice <= 9:
                #print("4 med")
                ghostSpeed4 = 2 + ghost_speed
            elif speedChoice == 10:
                #print("4 fast")
                ghostSpeed4 = 2 + ghost_speed

            move_towards(artifact, ghost4, ghostSpeed4)
        if lives <= 0:
            pass
            pygame.mixer.music.stop()
            #gameState = 4

    #camera reaction
        if camPos.colliderect(ghost) == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                killCount += 1
                if speedDuringBoss == False:
                    ghost_speed += .025
                ghost = spawn_ghost_x(1)

                if speedDuringBoss == False:
                    speedChoice = random.randint(1, 10)
                elif speedDuringBoss == True:
                    speedChoice = 1
                #print(speedChoice)
                if speedChoice <= 3:
                    #print("1 slow")
                    ghostSpeed1 = 1 + ghost_speed
                elif 4 <= speedChoice <= 9:
                    #print("1 med")
                    ghostSpeed1 = 2 + ghost_speed
                elif speedChoice == 10:
                    #print("1 fast")
                    ghostSpeed1 = 2 + ghost_speed

                move_towards(artifact, ghost, ghostSpeed1)

        if camPos.colliderect(ghost2) == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                killCount += 1
                if speedDuringBoss == False:
                    ghost_speed += .025
                ghost2 = spawn_ghost_x(2)

                if speedDuringBoss == False:
                    speedChoice = random.randint(1, 10)
                elif speedDuringBoss == True:
                    speedChoice = 1
                #print(speedChoice)
                if speedChoice <= 3:
                    #print("2 slow")
                    ghostSpeed2 = 1 + ghost_speed
                elif 4 <= speedChoice <= 9:
                    #print("2 med")
                    ghostSpeed = 2 + ghost_speed
                elif speedChoice == 10:
                    #print("2 fast")
                    ghostSpeed2 = 2 + ghost_speed

                move_towards(artifact, ghost2, ghostSpeed2)

        if camPos.colliderect(ghost3) == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                killCount += 1
                if speedDuringBoss == False:
                    ghost_speed += .025
                ghost3 = spawn_ghost_y(1)

                if speedDuringBoss == False:
                    speedChoice = random.randint(1, 10)
                elif speedDuringBoss == True:
                    speedChoice = 1
                #print(speedChoice)
                if speedChoice <= 3:
                    #print("3 slow")
                    ghostSpeed3 = 1 + ghost_speed
                elif 4 <= speedChoice <= 9:
                    #print("3 med")
                    ghostSpeed3 = 2 + ghost_speed
                elif speedChoice == 10:
                    #print("3 fast")
                    ghostSpeed3 = 2 + ghost_speed

                move_towards(artifact, ghost3, ghostSpeed3)

        if camPos.colliderect(ghost4) == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                killCount += 1
                if speedDuringBoss == False:
                    ghost_speed += .05
                ghost4 = spawn_ghost_y(2)

                if speedDuringBoss == False:
                    speedChoice = random.randint(1, 10)
                elif speedDuringBoss == True:
                    speedChoice = 1
                #print(speedChoice)
                if speedChoice <= 3:
                    #print("4 slow")
                    ghostSpeed4 = 1 + ghost_speed
                elif 4 <= speedChoice <= 9:
                    #print("4 med")
                    ghostSpeed4 = 2 + ghost_speed
                elif speedChoice == 10:
                    #print("4 fast")
                    ghostSpeed4 = 2 + ghost_speed

                move_towards(artifact, ghost4, ghostSpeed4)

        if camPos.colliderect(ghostBoss) == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                bossHealth -= 1
                print(bossHealth)

            if bossHealth <= 0:
                gameState = 5
                pygame.mixer.music.stop()

        screen.fill((0, 0, 0))
        screen.blit(timer_text, (0, 0))
        screen.blit(lives_text, (700,0))
        screen.blit(center_image, artifact)
        screen.blit(ghost_image, ghost)
        screen.blit(ghost_image, ghost2)
        screen.blit(ghost_image, ghost3)
        screen.blit(ghost_image, ghost4)
        screen.blit(ghostboss_image, ghostBoss)
        screen.blit(camera_image, (camPos.x, camPos.y))
        pygame.display.flip()
        clock.tick(60)

    while gameState == 4:
        #game loss
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = 6  # full quit
                if event.key == pygame.K_r:
                    gameState = 1


                    ghostSpeed1 = 1
                    ghostSpeed2 = 1
                    ghostSpeed3 = 1
                    ghostSpeed4 = 1
                    bossSpeed = 0
                    ghost_speed = 0
                    bossGhost = False
                    speedDuringBoss = False
                    lives = 5
                    bossHealth = 25
                    killCount = 0
                    ghost = spawn_ghost_x(1)
                    ghost2 = spawn_ghost_x(2)
                    ghost3 = spawn_ghost_y(1)
                    ghost4 = spawn_ghost_y(2)
                    bossNum = 0
                    ghostBoss = spawn_boss(bossNum)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("menu.mp3")
                    pygame.mixer.music.play(-1)
                    start_time = time.time()
                    gameStart = False

        screen.fill((0, 0, 0))
        if laugh == 1:
            deathLaugh.play()
            laugh+=1
        deathText = font2.render("YOU DIED" , True, (255,0,0))
        final_time_text = font2.render(f'You lasted: {elapsed_minutes:02d}:{elapsed_seconds:05.2f}', True, (255, 255, 255))
        restartText = font.render("Restart: r", True, (255,255,255))
        screen.blit(deathText, (275, 300))
        screen.blit(final_time_text, (200, 400))
        screen.blit(restartText, (320, 500))
        quitText = font.render("Quit: esc", True, (255, 255, 255))
        screen.blit(quitText, (320, 550))
        pygame.display.flip()

    while gameState == 5:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameState = 6  # full quit
                if event.key == pygame.K_r:
                    gameState = 1

                    ghostSpeed1 = 1
                    ghostSpeed2 = 1
                    ghostSpeed3 = 1
                    ghostSpeed4 = 1
                    bossSpeed = 0
                    ghost_speed = 0
                    bossGhost = False
                    speedDuringBoss = False
                    lives = 5
                    bossHealth = 25
                    killCount = 0
                    ghost = spawn_ghost_x(1)
                    ghost2 = spawn_ghost_x(2)
                    ghost3 = spawn_ghost_y(1)
                    ghost4 = spawn_ghost_y(2)
                    bossNum = 0
                    ghostBoss = spawn_boss(bossNum)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("menu.mp3")
                    pygame.mixer.music.play(-1)
                    start_time = time.time()
                    gameStart = False

        if laugh == 1:
            victoryTheme.play()
            laugh += 1

        screen.fill((0, 0, 0))
        winText = font2.render("YOU Win", True, (0, 255, 0))
        final_time_text = font2.render(f'You lasted: {elapsed_minutes:02d}:{elapsed_seconds:05.2f}', True, (255, 255, 255))
        restartText = font.render("Restart: r", True, (255, 255, 255))
        screen.blit(winText, (285, 300))
        screen.blit(final_time_text, (190, 400))
        screen.blit(restartText, (320, 500))
        quitText = font.render("Quit: esc", True, (255, 255, 255))
        screen.blit(quitText, (320, 550))
        pygame.display.flip()
