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