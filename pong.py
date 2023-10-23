import pygame
pygame.init()

lPX = 10
lPY = 250

rPX = 788
rPY = 250
DeltaRPY = 0
DeltaLPY = 0

pW = 5
pH = 100

bX = 395
bY = 300
DeltaBX = .25
DeltaBY = 0
rvertVel = 0.0
lvertVel = 0.0

pLScore = 0
pRScore = 0
start = True
screen = pygame.display.set_mode((800,600))

def reset():
    global bX, bY, DeltaBX, DeltaBY, rvertVel, lvertVel, lPY, rPY
    bX = 395
    bY = 300
    DeltaBX = .25
    DeltaBY = 0
    rvertVel = 0.0
    lvertVel = 0.0
    lPY = 250
    rPY = 250

def collision(rPY,rPX, lPY, lPX, bY, bX, rvV, lvV):
    global DeltaBX, DeltaBY, pLScore, pRScore
    if ((abs(rPY+100 - bY) <= 100) and abs(bX-rPX)<= 1):
        DeltaBX*=-1
        DeltaBY+=rvV/10
    if ((abs(lPY+100 - bY) <= 100) and abs(bX-lPX)<= 1):
        DeltaBX*=-1
        DeltaBY+=lvV/10
    if bY >= 595:
        DeltaBY*=-1
    elif bY <= 5:
        DeltaBY*=-1
    if bX >= 800:
        pLScore += 1
        print(pLScore)
        reset()
    elif bX <= 0:
        pRScore += 1
        print(pRScore)
        reset()



game = True
while game:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                DeltaRPY -= 0.5
                if rvertVel > 0:
                    rvertVel += 1
                elif rvertVel == 0:
                    rvertVel+=1
                else:
                    rvertVel = 0
                    rvertVel += 1
            if event.key == pygame.K_DOWN:
                DeltaRPY += 0.5
                if rvertVel > 0:
                    rvertVel = 0
                    rvertVel -= 1
                elif rvertVel == 0:
                    rvertVel-= 1
                else:
                    rvertVel -= 1
            if event.key == pygame.K_w:
                DeltaLPY -= 0.5
                if lvertVel > 0:
                    lvertVel += 1
                elif lvertVel == 0:
                    lvertVel+=1
                else:
                    lvertVel = 0
                    lvertVel += 1
            if event.key == pygame.K_s:
                DeltaLPY += 0.5
                if lvertVel > 0:
                    lvertVel = 0
                    lvertVel -= 1
                elif lvertVel == 0:
                    lvertVel-= 1
                else:
                    lvertVel -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                DeltaRPY = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                DeltaLPY = 0
    collision(rPY,rPX, lPY, lPX, bY, bX, rvertVel, lvertVel)
    bX += DeltaBX
    bY += DeltaBY
    rPY += DeltaRPY
    lPY += DeltaLPY
    if rPY >= 550:
        rPY = 550
    elif rPY <= 0:
        rPY = 0
    if lPY >= 550:
        lPY = 550
    elif lPY <= 0:
        lPY = 0
    
    pygame.draw.circle(screen,(255,255,255), (bX, bY), 10.0)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(lPX, lPY, pW, pH))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(rPX, rPY, pW, pH))
    pygame.display.update()
    

