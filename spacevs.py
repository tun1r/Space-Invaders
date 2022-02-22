import pygame 
import random
# Initializing pygame    
pygame.init()

 # Screen Assignment
screen=pygame.display.set_mode((800,600))

background=pygame.image.load('space.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load('icon.png'))




# Player 
Player=pygame.image.load('player.png')
PlayerX=370
PlayerY=480
pchange=0

  

# Enemy 
Enemy=pygame.image.load('enemy.png')
EnemyX=random.randint(0,800)
EnemyY=random.randint(50,150)
exchange=0.2
eychange=40

# Bullet
Bullet=pygame.image.load('bullet.png')
BulletX=0
BulletY=480
bxchange=0
bychange=8
b_behaviour= "ready"

def player(x,y):
    screen.blit(Player,(PlayerX,PlayerY))

def enemy(x,y):
    screen.blit(Enemy,(EnemyX,EnemyY))
# The main body of the loop is not going to matter because value of running is always true
#Bullet


def shoot(x,y):
    global b_behaviour
    b_behaviour="fire"
    screen.blit(Bullet,(x+16,y+10))


# Game Loop
running=True
while(running):
    
    screen.fill((0,0,0))
    screen.blit(background,(0,0)) 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

     # All event if statements
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
             pchange=-0.45
            if event.key==pygame.K_RIGHT:
             pchange=0.45
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
             pchange=0
        if event.type==pygame.K_SPACE:
            shoot(PlayerX,BulletY)
        

    PlayerX+=pchange

    if PlayerX <=0:
        PlayerX=0
    elif PlayerX>=736:
        PlayerX=736


    EnemyX+=exchange

    if EnemyX <=0:
        exchange=0.2
        EnemyY+= eychange   
    elif EnemyX>=736:
        exchange=-0.2
        EnemyY+= eychange
    
    if b_behaviour is "fire":
        shoot(PlayerX,EnemyY)
        BulletY -= bychange
     
    player(PlayerX,PlayerY)
    enemy(EnemyX,EnemyY)
    pygame.display.update()
     
                   