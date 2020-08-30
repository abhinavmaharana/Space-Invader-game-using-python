#--------------------------------------#
#             Libraries                #
#--------------------------------------#
import pygame
from pygame.locals import *
import sys,random,time

#--------------------------------------#
#       Creating Global Variable       #
#--------------------------------------#

SCREENWIDTH=1000
SCREENHEIGHT=600
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption('Space Invader Game by Abhinav Maharana')
FPS = 60
FPSCLOCK=pygame.time.Clock()
RED = (255,0,0)

#----------------------------------------#
#         Setting up the Game UI         #
#----------------------------------------#

background=pygame.image.load("C:/Users/abhin/OneDrive/Desktop/Space Invader Game/gamebg.jfif")
background=pygame.transform.scale(background,(SCREENWIDTH,SCREENHEIGHT))
gamebackground=pygame.image.load("C:/Users/abhin/OneDrive/Desktop/Space Invader Game/BG.jfif")
gamebackground=pygame.transform.scale(gamebackground,(SCREENWIDTH,SCREENHEIGHT))
gameoverbackground=pygame.image.load("C:/Users/abhin/OneDrive/Desktop/Space Invader Game/gameover.jfif")
gameoverbackground=pygame.transform.scale(gameoverbackground,(SCREENWIDTH,SCREENHEIGHT))
enemy=pygame.image.load("C:/Users/abhin/OneDrive/Desktop/Space Invader Game/enemy.jfif")
enemy=pygame.transform.scale(enemy,(50,50))
player=pygame.image.load("C:/Users/abhin/OneDrive/Desktop/Space Invader Game/player.jfif")
player=pygame.transform.scale(player,(50,50))
bullet=pygame.image.load("C:/Users/abhin/OneDrive/Desktop/Space Invader Game/bullet.jfif")
bullet=pygame.transform.scale(bullet,(10,50))
destroyimg=pygame.image.load("C:/Users/abhin/OneDrive/Desktop/Space Invader Game/")
destroyimg=pygame.transform.scale(destroyimg,(60,100))
pygame.mixer.init()


#----------------------------#
# Displaying score on screen #
#----------------------------#

def score_screen(text,color,x,y):
    font=pygame.font.SysFont("comicsansms",30)
    scoreonscreen=font.render(text,True,color)
    SCREEN.blit(scoreonscreen,(x,y))

#-------------------------------------------------------#
#   Welcome screen to user and asking to start the game #
#-------------------------------------------------------#

def WELCOMESCREEN():
    pygame.mixer.music.load("C:/Users/abhin/OneDrive/Desktop/Space Invader Game/LostSky.mp3")
    pygame.mixer.music.play()
    playerpos=[500,530];enemypos=[500,50];bulletpos=[520,150]
    SCREEN.blit(background(0,0))
    SCREEN.blit(player,(playerpos[0],playerpos[1]))
    SCREEN.blit(enemy,(enemypos[0],enemypos[1]))
    SCREEN.blit(bullet,(bulletpos[0],bulletpos[1]))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type==pygame.KEYDOWN and (event.key==pygame.K_UP or event.key == pygame.K_SPACE):
                MYGAME()

    FPSCLOCK.tick(FPS)

#------------------------------------------------------------#
#                   Main Game starts here                    #
#------------------------------------------------------------#

def MYGAME():
    #----------------------------------#
    #     Game is getting started      #
    #----------------------------------#
    pygame.mixer.music.load()
    pygame.mixer.music.play()
    time.sleep(1)

    pygame.mixer.music.load()
    pygame.mixer.music.play()
    time.sleep(1)

    pygame.mixer.music.load()
    pygame.mixer.music.play()
    time.sleep(1)

    pygame.mixer.music.load()
    pygame.mixer.music.play()

    #------------------------------------------#
    # GLOBAL AND LOCAL VARIABLE INITIALIZATION #
    #------------------------------------------#

    global gamebackground
    playerpos=[500,530];enemypos=[100,100]
    bulletpos=[playerpos[0]+20,playerpos[1]-50]
    playervelocity=0; enemyvelocity=0.8
    bulletvelocity=0; score=0
    tscore="0"; temp=0

    while True:
        #-------------------------------------#
        #   game event handling starts here   #
        #-------------------------------------#
        for event in pygame.event.get():
            #-------------------------------------------------------#
            # Checking if thr quit button is pressed or not by user #
            #-------------------------------------------------------#
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #--------------------------------------------------------#
            # If the player press right key, player velocity changes #
            #--------------------------------------------------------#    
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    playervelocity=4
                #-------------------------------------------------------#
                # If the player press left key, player velocity changes #
                #-------------------------------------------------------#
                if event.key==pygame.K_LEFT:
                    playervelocity=-4
                #----------------------------------------------#
                # if player presses space bar bullet get fired #
                #----------------------------------------------#
                if event.key==pygame.K_SPACE:                 
                    bulletvelocity=-12
            
            if event.type==pygame.KEYUP:
                if event.key==K_SPACE:
                    SCREEN.blit(bullet,(playerpos[0]+20,playerpos[1]-50))
                    pygame.display.update()
                    bulletpos[1]=int(playerpos[1]-50)
                    bulletpos[0]=int(playerpos[0]+20)

        #-----------------------------------#
        #   game event handling ends here   #
        #-----------------------------------#

        #----------------------------------------------------------------------------------------#
        # Checking if enemy is hit by bullet if so replacing it from screen and increasing score #
        #----------------------------------------------------------------------------------------#
        if abs(int(bulletpos[0])-int(enemypos[0]))<=40 and abs(int(bulletpos[1])-int(enemypos[1]))<=75:
            score+=1
            tscore=str(score*10) 
            SCREEN.blit(destroyimg,(bulletpos[0],bulletpos[1]-80))
            pygame.display.update()
            enemypos[0]=random.randint(100,SCREENWIDTH-100)
            enemypos[1]=50
            pygame.mixer.music.load("")
            pygame.mixer.music.play()
        
        #---------------------------------------------#
        # Giving a warning to player as enemy is near #
        #---------------------------------------------#

        if abs(int(playerpos[1])-int(enemypos[1]))==200:
            pygame.mixer.music.load()
            pygame.mixer.music.play()

        #---------------------------------------------#
        #   Leveling up with changing enemy velocity  #
        #---------------------------------------------#
        if int(tscore)>=100 and temp==0:
            temp=1
            enemyvelocity=1.0
            pygame.mixer.music.load()
            pygame.mixer.music.play()

        elif int(tscore)>=200 and temp==1:      
            temp=2
            enemyvelocity=1.5
            playervelocity=10
            pygame.mixer.music.load()
            pygame.mixer.music.play()

        elif int(tscore)>=300 and temp==2:
            enemyvelocity=2.0
            playervelocity=12
            temp=3
            pygame.mixer.music.load()
            pygame.mixer.music.play()
            
        elif int(tscore)>=400 and temp==3:
            enemyvelocity=2.5
            playervelocity=14
            temp=4
            pygame.mixer.music.load()
            pygame.mixer.music.play()
            
        elif int(tscore)>=500 and temp==4:
            enemyvelocity=3.5
            playervelocity=18
            temp=5
            pygame.mixer.music.load()
            pygame.mixer.music.play()

    #-------------------------------------------------------#
    #        Changing bullet,player,enemy position          #
    #-------------------------------------------------------#

    bulletpos[1]+=bulletvelocity
    playerpos[0]+=playervelocity
    enemypos[1]+=enemyvelocity

    #-----------------------------------------------------------------------------------------------------#
    #   Checking if player is at extreme left and repositioning on screen if player going out of screen   #
    #-----------------------------------------------------------------------------------------------------#

    if playerpos[0]<=0:
        playerpos[0]=50

    #----------------------------------------------------------------------------#
    # checking if player is at extreme right of screen and repositioning player  #
    #----------------------------------------------------------------------------#

    if playerpos[0]>=SCREENWIDTH:
        playerpos[0]=-30

    #----------------------------------------------------------------------------------#
    # checking if enemy is about to approach the player if so  game over is to be done #
    #----------------------------------------------------------------------------------#

    if (enemypos[1]>=(SCREENHEIGHT-100)):
        GAMEOVER()

    #------------------------------------------------------------------------#
    # blitting images of game background,player,bullet,enemy and setting FPS #
    #------------------------------------------------------------------------#

        SCREEN.blit(gamebackground,(0,0))
        score_screen(f"SCORE:{tscore}",RED,450,30) 
        SCREEN.blit(player,(playerpos[0],playerpos[1]))
        SCREEN.blit(bullet,(bulletpos[0],bulletpos[1]))
        SCREEN.blit(enemy,(int(enemypos[0]),int(enemypos[1])))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def GAMEOVER():
    pygame.mixer.music.load()
    pygame.mixer.music.play()

    playerpos=[500,530]
    enemypos=[500,50]
    bulletpos=[520,150]
    
    SCREEN.blit(gameoverbackground,(0,0))
    SCREEN.blit(player,(playerpos[0],playerpos[1]))
    SCREEN.blit(enemy,(enemypos[0],enemypos[1]))
    SCREEN.blit(bullet,(bulletpos[0],bulletpos[1]))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.mixer.music.load()
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.quit()
                sys.exit()

            if event.type==pygame.KEYDOWN and (event.key==pygame.K_UP or event.key==pygame.K_SPACE):
                WELCOMESCREEN()
                
                
    FPSCLOCK.tick(FPS)

#----------------------------------------#
#          Running the program           #
#----------------------------------------#

if __name__ == "__main__":
    WELCOMESCREEN()