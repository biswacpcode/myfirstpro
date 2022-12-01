import pygame
import time
import random
pygame.init()
speed=15
#size of window
x=1200
y=800
#Colors
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
#Window Design
pygame.display.set_caption("Snack Game By Biswajit")
gamewindow=pygame.display.set_mode((x,y))#check agaiin
fps=pygame.time.Clock()
snakepos=[100,50]#change if needed
#Initial length of snake in blocks
body=[[100,50],[90,50],[80,50],[70,50]]
fruitpos=[random.randrange(1,(x//10))*10, random.randrange(1,(y//10))*10 ]
spawn=True
direction="RIGHT"
change=direction
score=0

def showscore(choice, color, font, size):
    sfont=pygame.font.SysFont(font, size)
    ssurf=sfont.render("Score : " + str(score), True, color)
    srect=ssurf.get_rect()
    gamewindow.blit(ssurf,srect)

def gameover():
    myfont=pygame.font.SysFont("tw cen mt", 50)
    gosurf=myfont.render("Wowwww! Your Score is : " + str(score), True, red)
    gorect=gosurf.get_rect()
    gorect.midtop=(x/2,y/2)#change if needed
    gamewindow.blit(gosurf,gorect)
    pygame.display.flip()
    '''with open(f"{name}.txt","r") as f:
        if int(f.read())<score:
            with open(f"{name}.txt","w") as f:
                f.write(f"{score}")'''
    try:
        f=open(f"{name.lower()}.txt","r")
        k=open(f"{name.lower()}.txt","w")
        if int(f.read())<score:
            k.write(f"{score}")
    except:
        with open(f"{name.lower()}.txt","w") as f:
            f.write(f"{score}")
    time.sleep(2)
    pygame.quit()
    quit()

#MAIN CODE
name =input("Enter Your Name: ")
while True:
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                change="UP"
            if i.key == pygame.K_DOWN:
                change="DOWN"
            if i.key == pygame.K_RIGHT:
                change="RIGHT"
            if i.key == pygame.K_LEFT:
                change="LEFT"
            if i.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    #If 2 keys are presssed
    if change == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == "UP":
        snakepos[1]-=10
    elif direction =='DOWN':
        snakepos[1]+=10
    elif direction=="RIGHT":
        snakepos[0]+=10
    elif direction=="LEFT":
        snakepos[0]-=10

    #SNake Growing
    body.insert(0,list(snakepos))
    if snakepos[0]==fruitpos[0] and snakepos[1]==fruitpos[1]:
        score+=10
        spawn=False
    else:
        body.pop()

    if not spawn:
        fruitpos=[random.randrange(1,(x//10))*10,random.randrange(1,(y//10))*10]
        speed+=2

    spawn=True
    gamewindow.fill(black)

    for i in body:
        pygame.draw.rect(gamewindow,green, pygame.Rect(i[0],i[1],10,10))

    pygame.draw.rect(gamewindow,white,pygame.Rect(fruitpos[0],fruitpos[1], 10, 10))

    #Game Over
    if snakepos[0]<0 or snakepos[0]>x-10 or snakepos[1]<0 or snakepos[1]>y-10:
        gameover()

    for i in body[1:]:
        if snakepos[0]==i[0] and snakepos[1]== i[1]:
            gameover()

    showscore(1, white, 'tw cen mt', 40)
    pygame.display.update()
    fps.tick(speed)