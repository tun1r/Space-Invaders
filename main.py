import math
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
Enemy=[]
EnemyX=[]
EnemyY=[]
exchange=[]
eychange=[]
num=6
for i in range(num):
    Enemy.append(pygame.image.load('enemy.png'))
    EnemyX.append(random.randint(0,800))
    EnemyY.append(random.randint(50,150))
    exchange.append(0.2)
    eychange.append(40)

# Bullet
bulletImg = pygame.image.load('b.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"
score_value=0

font = pygame.font.Font('font.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x,y):
    screen.blit(Player,(PlayerX,PlayerY))

def enemy(x,y,i):
    screen.blit(Enemy[i],(EnemyX[i],EnemyY[i]))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def Collision(EnemyX, EnemyY, bulletX, bulletY):
    d = math.sqrt(math.pow(EnemyX - bulletX, 2) + (math.pow(EnemyY - bulletY, 2)))
    if d < 27:
        return True
    else:
        return False


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
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=PlayerX
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
             pchange=0

    PlayerX+=pchange

    if PlayerX <=0:
        PlayerX=0
    elif PlayerX>=736:
        PlayerX=736

    for i in range(num):
        if EnemyY[i] > 440:
            for j in range(num):
                EnemyY[j] = 2000
            game_over_text()
            break
        EnemyX[i]+=exchange[i]

        if EnemyX[i] <=0:
            exchange[i]=0.2
            EnemyY[i]+= eychange[i]   
        elif EnemyX[i]>=736:
            exchange[i]=-0.2
            EnemyY[i]+= eychange[i]      
        collision=Collision(EnemyX[i], EnemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480 
            bullet_state="ready"
            score_value +=1
        
            EnemyX[i] = random.randint(0, 736)
            EnemyY[i] = random.randint(50, 150)
        enemy(EnemyX[i],EnemyY[i],i)

    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
   
    

    player(PlayerX,PlayerY)
    show_score(textX, testY)
    pygame.display.update()   