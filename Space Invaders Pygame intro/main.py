import pygame
import random
import math

#initilizing pygame
pygame.init()

#creating a screen with 800 pixles width 600 pixles height
screen = pygame.display.set_mode((800,600))

#creating background
background = pygame.image.load("background.jpeg")

#Making title of game window
pygame.display.set_caption("Space Invaders")

points = 0
#Font type
font = pygame.font.Font("freesansbold.ttf", 32)
#score x and y pos (where it is displayed)
scoreX = 20
scoreY = 20

def showScore(x,y):
    score = font.render("Score: " + str(points), True, (255,255,255))
    screen.blit(score, (x, y))
#player image variable
playerImage = pygame.image.load("spaceship.png")
#Initial player position on screen in pixles
playerXPos = 370
playerYPos = 480
playerXChange = 0

def player(x, y):
    #draws png on screen using x and y cords passed in
    screen.blit(playerImage, (x, y))

enemyImage = []
enemyXPos = []
enemyYPos = []
enemyXChange = []
enemyYChange = []
numOfEn = 6

for i in range (numOfEn):
    enemyImage.append(pygame.image.load("enemy.png"))
    enemyXPos.append(random.randint(1,735))
    enemyYPos.append(random.randint(50,150))
    enemyXChange.append(0.22)
    enemyYChange.append(40)

def enemy(x, y, i):
    #draws enemy png on screen using x and y cords passed in
    screen.blit(enemyImage[i], (x, y))

#ready state of bullet means you cant see bullet on screen and fire means bullet is moving
bulletImage = pygame.image.load("bullet.png")
bulletXPos = 0
bulletYPos = 480
bulletXPos = 0
bulletYChange = 1
bulletState = "ready"

def fireBullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x+16,y+10))

def collision(eX, eY, bX, bY):
    dis = math.sqrt((math.pow(eX-bX,2))+(math.pow(eY-bY,2)))
    if dis <= 27:
        return True
    else:
        return False
#Game Loop
running = True
while running == True:
    #RGB values for backround of display
    #Must have this before everything getting drawn or else it draws over it
    screen.fill((0,0,0))
    #creating background
    screen.blit(background, (0,0))
    #loops through all events in pygame
    for event in pygame.event.get():
        #if event == exit button on display stop running
        if event.type == pygame.QUIT:
            running = False

        #Checks keystrokes to see which key was pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange -= 0.3
            if event.key == pygame.K_RIGHT:
                playerXChange += 0.3
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletXPos = playerXPos
                    fireBullet(bulletXPos,bulletYPos)
        
        #checks what key was unpressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0

#Checking boundaries for player
    playerXPos += playerXChange
    if playerXPos <=0:
        playerXPos = 0
    #736 becase you subtract 64 pixles of player png from 800 pixles from total screen width
    elif playerXPos >= 736:
        playerXPos = 736

    #enemy movement
    for i in range(numOfEn):
        enemyXPos[i] += enemyXChange[i]
        if enemyXPos[i] <=0:
            enemyXChange[i] = 0.22
            enemyYPos[i] += enemyYChange[i]
        elif enemyXPos[i] >= 736:
            enemyXChange[i] = -0.22
            enemyYPos[i] += 40
#collision
        col = collision(enemyXPos[i], enemyYPos[i], bulletXPos, bulletYPos)
        if col == True:
            bulletYPos = 480
            bulletState = "ready"
            points+=1
            enemyXPos[i] = random.randint(1,735)
            enemyYPos[i] = random.randint(50,150)
        
        enemy(enemyXPos[i], enemyYPos[i], i)
        
    if bulletYPos <= -10:
        bulletYPos = 480
        bulletState = "ready"
    #Bullet movement
    if bulletState == "fire":
        fireBullet(bulletXPos, bulletYPos)
        bulletYPos -= bulletYChange
    #draws player & enemy png after filling the screen
    showScore(scoreX, scoreY)
    player(playerXPos, playerYPos)
    

    #Updates the screen
    pygame.display.update()