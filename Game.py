#**********************************************************
# Program	:  Game
# Author	:  Christian Majid
# Due Date	:  The End of This Unit
# Description	:  Mario Game
#**********************************************************
import pygame
import sys
import time
import random
import sys,pygame,pygame.mixer
from pygame.locals import *
pygame.init()

#Set Window
WINDOW = pygame.display.set_mode((700, 424))
window =(166,0,0)
colour=(0,0,0)
black=(0,0,0)
white=(255,255,255)
WINDOW.fill(black)

#Program Title
pygame.display.set_caption("Mario")

#Assigning
GameOver=("You Died. Press Space to Play Again.")
GameOver2=("Or Press Escape to Go to Settings.")
FPS = 50
fpsClock = pygame.time.Clock()
pcountR=0
pcountL=0
font1 = pygame.font.SysFont('Times New Roman', 20, 0, 0)
LastDir = "L"
Char="Mario"
Dead=False
RectY=-800
RectX=-1000
Rect1=False
Rect2=False
UnderGround=False
LeftWall=0
RightWall=0
CoinCollect=0
DeadGuyX=190
DeadGuyCounter=0
Invincibility=False
DevTools=True
Finish=False
StarCounter=0
StarY=0
EndCounter=0
MoveFinish=0
Endx=-700
H=False
#Menu
Menu=True
mx=0
MenuOrder=1

#Pictures
Sprite = pygame.image.load("Character.gif")
Stage = pygame.image.load("Stage.png")
Coin = pygame.image.load("Coin.png")
Block = pygame.image.load("Empty Block.png")
DeadGuy = pygame.image.load("DeadGuy.png")
ShyGuy = pygame.image.load("ShyGuy.png")
ShyGuy2 = pygame.image.load("ShyGuy.png")
Menu1 = pygame.image.load("Menu1.png")
Menu2 = pygame.image.load("Menu2.png")
Menu3 = pygame.image.load("Menu3.png")
Star= pygame.image.load("Star.png")
Left = pygame.image.load("Left.png")
Right = pygame.image.load("Right.png")
EndScreen = pygame.image.load("End.png")
Help = pygame.image.load("Help.png")



#Location
#Character
x=20
y=389

#Sprite
px=150
py=0
ph=30
pw=30
phcounter=0

#Detect Movement
moveL=1
moveR=1
zU=0
fast = 0
tempx=x
tempy=y
#Landing False = Not Falling
#landing True = Falling
Landing = False

#Going in Pipes
GoingDown=0
GoingIn=0


#Stage
sx=0
sy=0

#ShyGuys
ShyGuypx1=5
ShyGuypy1=86
ShyGuyx1=249
ShyGuyDir1=1
ShyGuy1="Alive"

ShyGuypx2=5
ShyGuypy2=86
ShyGuyx2=91
ShyGuyDir2=-1
ShyGuy2="Alive"

ShyGuypx3=5
ShyGuypy3=86
ShyGuyx3=1180
ShyGuyDir3=1
ShyGuy3="Alive"

ShyGuypx4=5
ShyGuypy4=86
ShyGuyx4=790
ShyGuyDir4=1
ShyGuy4="Alive"

ShyGuypx5=5
ShyGuypy5=86
ShyGuyx5=830
ShyGuyDir5=1
ShyGuy5="Alive"

ShyGuypx6=5
ShyGuypy6=86
ShyGuyx6=870
ShyGuyDir6=1
ShyGuy6="Alive"

ShyCounter1=0
ShyCounter2=0
ShyCounter3=0
ShyCounter4=0
ShyCounter5=0
ShyCounter6=0

#Coins
Collect=0
Coin1=True
Coin2=True
Coin3=True
Coin4=True
Coin5=True
Coin6=True
Coin7=True
Coin8=True
Coin9=True
Coin10=True
Coin11=True
Coin12=True
Coin13=True
Coin14=True
Coin15=True
Coin16=True
Coin17=True
Coin18=True
Coin19=True
Coin20=True
Coin21=True
Coin22=True
Coin23=True
Coin24=True
Coin25=True
Coin26=True
Coin27=True
Coin28=True
Coin29=True
Coin30=True
Coin31=True
Coin32=True
Coin33=True
Coin34=True
Coin35=True
Coin36=True
Coin37=True
Coin38=True
Coin39=True
Coin40=True
Coin41=True
Coin42=True
Coin43=True
Coin44=True
Coin45=True
Coin46=True

#Block State
block1=0
block2=0
block3=0
block4=0
block5=0
block6=0
block7=0
CoinCounter1=20
CoinCounter2=20
CoinCounter3=20
CoinCounter4=20
CoinCounter5=20
CoinCounter6=20
CoinCounter7=20

#Sound
SoundJump = pygame.mixer.Sound("Jump.wav")
Pipe = pygame.mixer.Sound("Pipe.wav")
CoinSound = pygame.mixer.Sound("Coin.wav")
Theme = pygame.mixer.Sound("Theme.wav")
ShyGuySound = pygame.mixer.Sound("ShyGuy.wav")
Underground = pygame.mixer.Sound("Underground.wav")
SoundMusic = pygame.mixer.Sound("Overworld.wav")
DeadSound = pygame.mixer.Sound("Dead.wav")
Clear = pygame.mixer.Sound("Clear.wav")
Sunshine = pygame.mixer.Sound("Sunshine.wav")

Theme.play()

#Main Graphics
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

#Pressing a Key
      if event.type == pygame.KEYDOWN:
         #Left
         if event.key == pygame.K_LEFT and GoingDown!=1 and Finish!=True:
            moveL=0
            px=150
            LastDir="L"
            
         #Right
         elif event.key == pygame.K_RIGHT and GoingDown!=1 and Finish!=True:
            moveR=0
            px=210
            LastDir="R"
            
         #Up
         if event.key == pygame.K_UP and Landing==False and GoingDown!=1 and Dead!=True and Finish!=True:
            zU=100
            Landing=True
            SoundJump.play()

         #Down Pipe
         if event.key == pygame.K_DOWN and x+sx>2240 and x+sx<2284and y>254 and y<260:
            GoingDown=1
            tempx=x
            tempy=y
            Pipe.play()

         if event.key == pygame.K_SPACE and Dead==True:
            Dead=False
            pygame.mixer.stop()
            SoundMusic.play()

         #Respawn
         if event.key == pygame.K_ESCAPE and Dead==True:
            Dead=False
            Menu=True
            pygame.mixer.stop()
            Theme.play()

         #Close
         if event.key == pygame.K_ESCAPE and MoveFinish==5:
            pygame.quit()
            sys.exit()

            
         #Fast
         if event.key == pygame.K_a:
            fast = 1
            
         #Help
         if event.key == pygame.K_h:
            H=True
 

         #Reset#
         if event.key == pygame.K_r and DevTools==True:
            y=200
            ShyGuy1="Alive"
            ShyGuy2="Alive"
            ShyGuy3="Alive"
            ShyGuy4="Alive"
            ShyGuy5="Alive"
            ShyGuy6="Alive"

         #Teleport#
         if event.key == pygame.K_t and DevTools==True:
            sx=2160
            
         #Character
         if event.key == pygame.K_1:
            Char="Mario"

         if event.key == pygame.K_2:
            Char="Luigi"
            
#Letting Go a Key
      if event.type == pygame.KEYUP:
         #Left
         if event.key == pygame.K_LEFT:
            moveL=1
            px=150
            
         #Right
         if event.key == pygame.K_RIGHT:
            moveR=1
            px=150

         #Speed
         if event.key == pygame.K_a:
            fast = 0

         #Menu
         if event.key == pygame.K_SPACE and Menu==True and MenuOrder==1:
            if LastDir=="L":
               Char="Mario"
               
            elif LastDir=="R":
               Char="Luigi"
            MenuOrder=2

         elif event.key == pygame.K_SPACE and Menu==True and MenuOrder==2:
            if LastDir=="L":
               Invincibility=False

            elif LastDir=="R":
               Invincibility=True
            MenuOrder=3

         elif event.key == pygame.K_SPACE and Menu==True and MenuOrder==3:
            if LastDir=="L":
               DevTools=False

            elif LastDir=="R":
               DevTools=True
               Stage = pygame.image.load("StageDev.png")
            pygame.mixer.stop()
            SoundMusic.play()
            MenuOrder=1
            Menu=False
            x=20
            y=389

         elif Menu==True and event.key == pygame.K_a:
            DevTools=True
            Char="Mario"
            Invincibility=False
            pygame.mixer.stop()
            SoundMusic.play()
            MenuOrder=1
            Menu=False
            x=20
            y=389
            
         #Respawn Win
         if event.key == pygame.K_SPACE and MoveFinish==5:
            Dead=False
            Menu=True
            Finish=False
            pygame.mixer.stop()
            Theme.play()
            MoveFinish=0
            moveL=1
            moveR=1
            
         #Help
         if event.key == pygame.K_h:
            H=False

#Animation
   WINDOW.fill(black)
   WINDOW.blit(Stage, (0,0),(sx, sy, 700, 450))
   #Character Set
   if Char=="Mario" and MoveFinish!=2:
      py=0
   if Char=="Luigi" and MoveFinish!=2:
      py=200
      
#Movement
   #Left
   if moveL==0:
      x=x-1
      if fast == 1:
         x=x-2
      pcountL=pcountL + 1
      if pcountL == 5:
         px=px-30
         pcountL=0
      if px <= 60:
         px = 120
         
   #Right
   if moveR==0:
      x=x+1
      if fast == 1:
         x=x+2
      pcountR=pcountR + 1
      if pcountR == 5:
         px=px+30
         pcountR=0
      if px >= 300:
         px = 210
   #Jump      
   if zU>0:
      y=y-3
      zU=zU-5
      if moveL==0:
         px=30
      elif moveR==0:
         px=300
      elif LastDir=="L":
         px=30
      elif LastDir=="R":
         px=300

   #Fall
   elif zU==0 and Landing==True:
      y=y+3
      if moveL==0:
         px=0
      elif moveR==0:
         px=330
      
   #Stage Edges
   if x<=0:
      x=0
      sx=0
   if x>=685 and MoveFinish!=4:
      x=685

   if GoingDown==1:
      Landing=True
      x=tempx
      y=tempy
      zU=0
      moveR=1
      moveL=1
      px=150
      if ph<=0:
         pcounter=0
         y=1000
      elif phcounter == 1:
         ph=ph-1
         tempy=tempy+1
         phcounter=0
      phcounter=phcounter+1

   if GoingIn==1:
      Landing=True
      y=tempy
      zU=0
      moveR=1
      moveL=1
      px=270
      if pw<=0:
         phcounter=0
         x=1000
      elif phcounter == 2:
         pw=pw-1
         moveL=1
         x=x+1
         phcounter=0
      phcounter=phcounter+1
      
#Stage Collision
#See Stage Reference for Sections
#####################    Top/Landing on Blocks    #####################
#Death Bed
   if y>450 and y<500 :
      y=450
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()
      
#Section 1
   #Ground
   elif x+sx>-5 and x+sx<649 and y>388 and y<396 and zU==0:
      y=389
      Landing=False

   #First Pink Box
   elif x+sx>224 and x+sx<284 and y>335 and y<341 and zU==0:
      y=339
      Landing=False

   #Blue Rectangle
   elif x+sx>256 and x+sx<316 and y>302 and y<308 and zU==0:
      y=307
      Landing=False

   #Pipe
   elif x+sx>334 and x+sx<382 and y>336 and y<342 and zU==0:
      y=339
      Landing=False
      
   #Green Rectangle
   elif x+sx>384 and x+sx<476 and y>336 and y<342 and zU==0:
      y=339
      Landing=False

   #Pink Rectangle
   elif x+sx>448 and x+sx<524 and y>303 and y<311 and zU==0:
      y=307
      Landing=False

   #Green Long Rectangle
   elif x+sx>496 and x+sx<604 and y>352 and y<358 and zU==0:
      y=355
      Landing=False

   #White Tall Rectangle
   elif x+sx>496 and x+sx<572 and y>272 and y<278 and zU==0:
      y=275
      Landing=False


#Section 2
   #Second Ground
   elif x+sx>608 and x+sx<1081 and y>368 and y<374 and zU==0:
      y=371
      Landing=False


#Section 3
   #Third Ground
   elif x+sx>1136 and x+sx<1500 and y>384 and y<390 and zU==0:
      y=387
      Landing=False
      
   #Green Rectangle
   elif x+sx>1248 and x+sx<1372 and y>352 and y<358 and zU==0:
      y=355
      Landing=False

   #Pink Rectangle
   elif x+sx>1280 and x+sx<1404 and y>320 and y<326 and zU==0:
      y=323
      Landing=False

   #Blue Rectangle
   elif x+sx>1312 and x+sx<1436 and y>288 and y<294 and zU==0:
      y=291
      Landing=False
      
   #Two Wood Things
   elif x+sx>1483 and x+sx<1529 and y>320 and y<328 and zU==0:
      y=327
      Landing=False


#Section 3.5
   #Three Point Five Ground
   elif x+sx>1521 and x+sx<1612 and y>384 and y<390 and zU==0:
      y=387
      Landing=False
      
   #Stairs 1
      #Bottom 1
   elif x+sx>1550 and x+sx<1612 and y>369 and y<375 and zU==0:
      y=372
      Landing=False

      #Bottom 2
   elif x+sx>1566 and x+sx<1612 and y>352 and y<358 and zU==0:
      y=355
      Landing=False

      #Bottom 3
   elif x+sx>1582 and x+sx<1612 and y>336 and y<342 and zU==0:
      y=339
      Landing=False
      
   #Stairs 2
      #Bottom 1
   elif x+sx>1648 and x+sx<1678 and y>336 and y<342 and zU==0:
      y=339
      Landing=False

      #Bottom 2
   elif x+sx>1648 and x+sx<1694 and y>352 and y<358 and zU==0:
      y=355
      Landing=False
      
      #Bottom 3
   elif x+sx>1648 and x+sx<1710 and y>368 and y<374 and zU==0:
      y=371
      Landing=False

#Section 4
   #Fourth Ground
   elif x+sx>1648 and x+sx<2236 and y>384 and y<390 and zU==0:
      y=387
      Landing=False

   #Pipe 1
      #Top
   elif x+sx>1774 and x+sx<1822 and y>352 and y<358 and zU==0:
      y=355
      Landing=False

   #Pipe 2
      #Top
   elif x+sx>1838 and x+sx<1886 and y>337 and y<343 and zU==0:
      y=340
      Landing=False

   #First Stair Box Thing
      #First Step
   elif x+sx>1932 and x+sx<2040 and y>368 and y<374 and zU==0:
      y=371
      Landing=False

      #Second Step
   elif x+sx>1950 and x+sx<2040 and y>352 and y<358 and zU==0:
      y=355
      Landing=False

      #Third Step
   elif x+sx>1966 and x+sx<2040 and y>336 and y<342 and zU==0:
      y=339
      Landing=False
      
   #Second Stair Box Thing
      #First Step Top
   elif x+sx>2082 and x+sx<2126 and y>368 and y<374 and zU==0:
      y=371
      Landing=False

      #Second Step Top
   elif x+sx>2082 and x+sx<2110 and y>352 and y<358 and zU==0 :
      y=355
      Landing=False

   #Pink Box
   elif x+sx>2128 and x+sx<2188 and y>336 and y<342 and zU==0 and UnderGround==False:
      y=339
      Landing=False

   #Green Rectangle
   elif x+sx>2160 and x+sx<2220 and y>284 and y<290 and zU==0 and UnderGround==False:
      y=287
      Landing=False

#Section 5
   #Ground
   elif x+sx>2240 and x+sx<3200 and y>384 and y<390 and zU==0 and UnderGround==False:
      y=387
      Landing=False

   #Top Pipe
   elif x+sx>2238 and x+sx<2286 and y>254 and GoingDown==1 and UnderGround==False:
      Landing=False
      
   elif x+sx>2238 and x+sx<2286 and y>254 and y<260 and zU==0 and GoingDown==0 and UnderGround==False:
      y=257
      Landing=False

   #Bottom Pipe
   elif x+sx>2238 and x+sx<2286 and y>349 and y<355 and zU==0 and UnderGround==False:
      y=352
      Landing=False

   #Another Pipe
   elif x+sx>2302 and x+sx<2350 and y>352 and y<358 and zU==0 and UnderGround==False:
      y=355
      Landing=False

#Underground   
   #Underground Floor
   elif x+sx>2121 and x+sx<2523 and y>292 and y<298 and zU==0 and UnderGround==True:
      y=295
      Landing=False
      
   #Pipe Ledge
   elif x+sx>2584 and x+sx<2656 and y>132 and y<138 and zU==0 and UnderGround==True:
      y=135
      Landing=False

   #First Step
   elif x+sx>2424 and x+sx<2471 and y>260 and y<266 and zU==0 and UnderGround==True:
      y=263
      Landing=False

   #Second Step
   elif x+sx>2456 and x+sx<2503 and y>228 and y<234 and zU==0 and UnderGround==True:
      y=231
      Landing=False

   #Third Step
   elif x+sx>2488 and x+sx<2535 and y>196 and y<202 and zU==0 and UnderGround==True:
      y=199
      Landing=False

   #Fourth Step
   elif x+sx>2520 and x+sx<2567 and y>164 and y<170 and zU==0 and UnderGround==True:
      y=167
      Landing=False

   #Fifth Step
   elif x+sx>2552 and x+sx<2599 and y>132 and y<138 and zU==0 and UnderGround==True:
      y=135
      Landing=False

      #Right Pipe
   elif x+sx>2601 and x+sx<2649 and y>103 and y<107 and zU==0:
      y=102
      Landing=False
      
   else:
      Landing=True

#####################   All Other Sides for Block   #####################
#Left Wall Collision:
   if LeftWall==1:
      x=x-1
      if fast==1:
         x=x-2
      if x==600:
         x=x-1

   if RightWall==1:
      x=x+1
      if fast==1:
         x=x+2
      if x==100:
         x=x+1
         
#Section 1
   #Pipe
      #Left
   if x+sx>334 and x+sx<340 and y>336 and y<417:
      LeftWall=1

      #Right
   elif x+sx>376 and x+sx<382 and y>337 and y<416:
      RightWall=1
      
   # Left Ledge
   elif x+sx>606 and x+sx<612 and y>368 and y<420:
      LeftWall=1

#Section 2
   #Right Cliff - Dead
   elif x+sx>1081 and x+sx<1087 and y>369 and y<500:
      RightWall=1
      Landing=True
         
#Section 3
   #Left Cliff
   elif x+sx>1133 and x+sx<1139 and y>392:
      LeftWall=1
      Landing=True
         
   #Two Wood Things
      #Bottom
   elif x+sx>1488 and x+sx<1532 and y>368 and y<374:
      y=371
      zU=0

      #Left
   elif x+sx>1483 and x+sx<1490 and y>320 and y<373:
      LeftWall=1
         
      #Right
   elif x+sx>1529 and x+sx<1535 and y>322 and y<373:
      RightWall=1

      #Right Cliff
   elif x+sx>1497 and x+sx<1503 and y>385:
      RightWall=1
      Landing=True

         
#Section 3.5
   #Left Cliff - Dead
   elif x+sx>1517 and x+sx<1523 and y>384 and y<500:
      LeftWall=1
      Landing=True
      
   #Stairs 1
      #Left 1
   elif x+sx>1550 and x+sx<1556 and y>368 and y<417:
      LeftWall=1
         
      #Left 2
   elif x+sx>1566 and x+sx<1572 and y>352 and y<417:
      LeftWall=1

      #Left 3
   elif x+sx>1582 and x+sx<1588 and y>336 and y<417:
      LeftWall=1
         
      #Right Cliff - Dead
   elif x+sx>1609 and x+sx<1615 and y>336 and y<500:
      RightWall=1
      Landing=True

         
   #Stairs 2
      #Right 1
   elif x+sx>1672 and x+sx<1678 and y>337 and y<417:
      RightWall=1

      #Right 2
   elif x+sx>1688 and x+sx<1694 and y>352 and y<417:
      RightWall=1
         
      #Right 3
   elif x+sx>1704 and x+sx<1710 and y>368 and y<417:
      RightWall=1
         
      #Left Cliff - Dead
   elif x+sx>1648 and x+sx<1652 and y>336  and y<500:
      LeftWall=1
      Landing=True

#Section 4
   #Pipe 1
      #Left
   elif x+sx>1774 and x+sx<1780 and y>352 and y<421:
      LeftWall=1

      #Right
   elif x+sx>1816 and x+sx<1822 and y>353 and y<420:
      RightWall=1

   #Pipe 2
      #Left
   elif x+sx>1838 and x+sx<1844 and y>337 and y<421:
      LeftWall=1

      #Right
   elif x+sx>1880 and x+sx<1886 and y>338 and y<420:
      RightWall=1
         
   #First Stair Box Thing
      #First Step Left 
   elif x+sx>1934 and x+sx<1940 and y>368 and y<421:
      LeftWall=1

      #Second Step Left
   elif x+sx>1950 and x+sx<1956 and y>352 and y<421:
      LeftWall=1

      #Third Step Left
   elif x+sx>1966 and x+sx<1972 and y>336 and y<421:
      LeftWall=1

      #Right
   elif x+sx>2040 and x+sx<2046 and y>337 and y<420:
      RightWall=1

   #Second Stair Box Thing
      #First Step Right
   elif x+sx>2120 and x+sx<2126 and y>369 and y<420 and UnderGround==False:
      RightWall=1

      #Second Step Right
   elif x+sx>2104 and x+sx<2110 and y>353 and y<420 and UnderGround==False:
      RightWall=1

      #Left
   elif x+sx>2078 and x+sx<2084 and y>352 and y<421 and UnderGround==False:
      LeftWall=1

   #Right Cliff - Dead
   elif x+sx>2233 and x+sx<2239 and y>385 and y<500 and y<500 and UnderGround==False:
      RightWall=1
      Landing=True

#Section 5
   #Left Cliff - Dead
   elif x+sx>2237 and x+sx<2243 and y>385  and y<500 and UnderGround==False:
      LeftWall=1
      Landing=True

   #Top Pipe
      #Bottom
   elif x+sx>2240 and x+sx<2284 and y>325 and y<340 and UnderGround==False:
      y=337
      zU=0

      #Left
   elif x+sx>2238 and x+sx<2244 and y>254 and y<321 and UnderGround==False:
      LeftWall=1

      #Right
   elif x+sx>2280 and x+sx<2286 and y>255 and y<320 and UnderGround==False:
      RightWall=1

   #Bottom Pipe
      #Left
   elif x+sx>2238 and x+sx<2244 and y>349 and y<418 and UnderGround==False:
      LeftWall=1

      #Right
   elif x+sx>2280 and x+sx<2286 and y>350 and y<417 and UnderGround==False:
      RightWall=1

   #Another Pipe
      #Left
   elif x+sx>2302 and x+sx<2308 and y>352 and y<418 and UnderGround==False:
      LeftWall=1

      #Right
   elif x+sx>2344 and x+sx<2350 and y>353 and y<417 and UnderGround==False:
      RightWall=1

#Underground
   #Walls
      #Left Wall
   elif x+sx>2130 and x+sx<2136 and y>-31 and y<817 and UnderGround==True:
      RightWall=1
         
      #Right Wall
   elif x+sx>2632 and x+sx<2638 and y>68 and y<818 and UnderGround==True:
      LeftWall=1

      #Top Wall
   elif x+sx>2121 and x+sx<2647 and y>96 and y<102 and UnderGround==True:
      y=99
      zU=0

   #Stairs
      #First Step
   elif x+sx>2424 and x+sx<2430 and y>260 and y<326 and UnderGround==True:
      LeftWall=1
         
      #Second Step
   elif x+sx>2456 and x+sx<2462 and y>224 and y<326 and UnderGround==True:
      LeftWall=1

      #Third Step
   elif x+sx>2488 and x+sx<2494 and y>192 and y<326 and UnderGround==True:
      LeftWall=1

      #Fourth Step
   elif x+sx>2520 and x+sx<2526 and y>160 and y<326 and UnderGround==True:
      LeftWall=1

      #Fifth Step
   elif x+sx>2552 and x+sx<2558 and y>128 and y<326 and UnderGround==True:
      LeftWall=1

      #Right Pipe Going in 
   elif x+sx>=2603 and y>103 and y<166 and UnderGround==True and moveR==0 and GoingIn!=1:
      GoingIn=1
      Pipe.play()
      tempy=135
      pw=10
      x=x+4

      #Right Pipe
   elif x+sx>2602 and x+sx<2607 and y>103 and y<166 and UnderGround==True and GoingIn!=1:
      LeftWall=1
      
   else:
      LeftWall=0
      RightWall=0
      
###?Blocks###
#1 Location
   if x+sx>162 and x+sx<187 and y>320 and y<326 and zU==0:
      y=323
      Landing=False

   #Empty
   if block1==1:
      WINDOW.blit(Block, (176-sx,352),(0, 0, 16, 16))
      if CoinCounter1==10:
         CoinSound.play()
         CoinCollect=CoinCollect+1
      if CoinCounter1>0:
         WINDOW.blit(Coin, (176-sx,336-20+CoinCounter1),(0, 0, 14, 16))
         CoinCounter1=CoinCounter1-1
         
      #Bottom
   if x+sx>161 and x+sx<188 and y>364 and y<370:
      y=367
      zU=0
      block1=1

      #Left
   if x+sx>158 and x+sx<164 and y>320 and y<369:
      LeftWall=1

#2 Location
   elif x+sx>176 and x+sx<203 and y>320 and y<326 and zU==0:
      y=323
      Landing=False
      
   #Empty
   if block2==1:
      WINDOW.blit(Block, (192-sx,352),(0, 0, 16, 16))
      if CoinCounter2==10:
         CoinSound.play()
         CoinCollect=CoinCollect+1
      if CoinCounter2>0:
         WINDOW.blit(Coin, (192-sx,336-20+CoinCounter2),(0, 0, 14, 16))
         CoinCounter2=CoinCounter2-1
         
      #Bottom
   if x+sx>176 and x+sx<203 and y>364 and y<370:
      y=367
      zU=0
      block2=1

      #Right
   if x+sx>200 and x+sx<206 and y>321 and y<368:
      RightWall=1

#3 Location
   elif x+sx>209 and x+sx<235 and y>272 and y<278 and zU==0:
      y=275
      Landing=False
      
   #Empty
   if block3==1:
      WINDOW.blit(Block, (224-sx,304),(0, 0, 16, 16))
      if CoinCounter3==10:
         CoinSound.play()
         CoinCollect=CoinCollect+1
      if CoinCounter3>0:
         WINDOW.blit(Coin, (224-sx,288-20+CoinCounter3),(0, 0, 14, 16))
         CoinCounter3=CoinCounter3-1
         
      #Bottom
   if x+sx>210 and x+sx<236 and y>316 and y<322:
      y=319
      zU=0
      block3=1

      #Left
   if x+sx>206 and x+sx<212 and y>272 and y<321:
      LeftWall=1

#4 Location
   elif x+sx>224 and x+sx<250 and y>272 and y<278 and zU==0:
      y=275
      Landing=False

   #Empty
   if block4==1:
      WINDOW.blit(Block, (240-sx,304),(0, 0, 16, 16))
      if CoinCounter4==10:
         CoinSound.play()
         CoinCollect=CoinCollect+1
      if CoinCounter4>0:
         WINDOW.blit(Coin, (240-sx,288-20+CoinCounter4),(0, 0, 14, 16))
         CoinCounter4=CoinCounter4-1

      #Bottom
   if x+sx>224 and x+sx<251 and y>316 and y<322:
      y=319
      zU=0
      block4=1

      #Right
   if x+sx>248 and x+sx<254 and y>273 and y<320:
      RightWall=1

#5 Location
   elif x+sx>401 and x+sx<429 and y>272 and y<278 and zU==0:
      y=275
      Landing=False
   #Empty
   if block5==1:
      WINDOW.blit(Block, (416-sx,304),(0, 0, 16, 16))
      if CoinCounter5==10:
         CoinSound.play()
         CoinCollect=CoinCollect+1
      if CoinCounter5>0:
         WINDOW.blit(Coin, (416-sx,288-20+CoinCounter5),(0, 0, 14, 16))
         CoinCounter5=CoinCounter5-1

      #Bottom
   if x+sx>405 and x+sx<431 and y>316 and y<322:
      y=335
      zU=0
      block5=1

      #Left
   if x+sx>398 and x+sx<404 and y>272 and y<321:
      LeftWall=1

      #Right
   if x+sx>427 and x+sx<433 and y>273 and y<320:
      RightWall=1


#6 Location
   elif x+sx>688 and x+sx<716 and y>304 and y<310 and zU==0:
      y=307
      Landing=False

   #Empty
   if block6==1:
      WINDOW.blit(Block, (704-sx,336),(0, 0, 16, 16))
      if CoinCounter6==10:
         CoinSound.play()
         CoinCollect=CoinCollect+1
      if CoinCounter6>0:
         WINDOW.blit(Coin, (704-sx,320-20+CoinCounter6),(0, 0, 14, 16))
         CoinCounter6=CoinCounter6-1
         
      #Bottom
   if x+sx>692 and x+sx<712 and y>348 and y<354:
      y=351
      zU=0
      block6=1

      #Left
   if x+sx>686 and x+sx<692 and y>304 and y<353:
      LeftWall=1

      #Right
   if x+sx>712 and x+sx<718 and y>305 and y<352:
      RightWall=1

#7 Location
   elif x+sx>1440 and x+sx<1467 and y>325 and y<330 and zU==0:
      y=327
      Landing=False
      
   #Empty
   if block7==1:
      WINDOW.blit(Block, (1456-sx,356),(0, 0, 16, 16))
      if CoinCounter7==10:
         CoinSound.play()
         CoinCollect=CoinCollect+1
      if CoinCounter7>0:
         WINDOW.blit(Coin, (1456-sx,340-20+CoinCounter7),(0, 0, 14, 16))
         CoinCounter7=CoinCounter7-1


      #Bottom
   if x+sx>1444 and x+sx<1464 and y>368 and y<374:
      y=371
      zU=0
      block7=1
      
      #Left
   if x+sx>1438 and x+sx<1444 and y>324 and y<373:
      LeftWall=1

      #Right
   if x+sx>1464 and x+sx<1470 and y>325 and y<372:
      RightWall=1

#End Block
      #Top
   elif x+sx>2665 and x+sx<2707 and y>299 and y<305 and zU==0:
      y=302
      Landing=False

      #Bottom
   elif x+sx>2667 and x+sx<2705 and y>353 and y<359:
      y=356
      zU=0
      Finish=True
      pygame.mixer.stop()
      Clear.play()
      

      #Left
   elif x+sx>2665 and x+sx<2671 and y>299 and y<358:
      LeftWall=1

      #Right
   elif x+sx>2701 and x+sx<2707 and y>300 and y<357:
      RightWall=1
      
         
#Stage Moving Left
   if x<=100 and moveL==0 and sx>0:
      x=100
      sx=sx-1
      if moveL==0 and fast == 1:
         sx=sx-3
      else:
         sx=sx-1

#Stage Moving Right
   if x>=600 and moveR==0 and sx<2030:
      x=600
      if moveR==0 and fast == 1:
         sx=sx+3
      else:
         sx=sx+1

#Coin Blit
   if sx>=1830:
      colour =(255,255,255)
      
   else:
      colour = (0,0,0)
      
   if UnderGround==True:
      colour = (0,0,0)
   CoinText = ("x")
   
   CoinRender = font1.render(str(CoinText), True, colour)
   CoinNumRender = font1.render(str(CoinCollect), True, colour)
   WINDOW.blit(CoinRender,(620,17))
   WINDOW.blit(CoinNumRender,(635,17))
   WINDOW.blit(Coin, (600,20),(0, 0, 14, 16))

#Shy Guys
   #Shy 1
   ShyCounter1=ShyCounter1+1
   if ShyCounter1==6:
      ShyCounter1=0
      if ShyGuy1=="Alive":
         ShyGuypx1=ShyGuypx1+23
      
   if ShyGuy1=="Alive":
      ShyGuyx1=ShyGuyx1+1*ShyGuyDir1
      WINDOW.blit(ShyGuy, (ShyGuyx1-sx,392),(ShyGuypx1, ShyGuypy1, 23, 30))
      
   if ShyGuy1=="Dead":
      WINDOW.blit(ShyGuy, (ShyGuyx1-sx,387),(ShyGuypx1, 176, 28, 37))

   if ShyGuypx1>=74 and ShyGuy1=="Alive":
      ShyGuypx1=5
      
   if ShyGuyx1<=50 and ShyGuy1=="Alive":
      ShyGuyDir1=1
      ShyGuypy1=68
      
   if ShyGuyx1>=250 and ShyGuy1=="Alive":
      ShyGuyDir1=-1
      ShyGuypy1=34

   if x+sx>ShyGuyx1 and x+sx<ShyGuyx1+21 and y>364 and y<368 and ShyGuy1=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx1=290
      ShyGuy1="Dead"
      
   elif x+sx+18>ShyGuyx1 and x+sx+18<ShyGuyx1+21 and y>364 and y<368 and ShyGuy1=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx1=290
      ShyGuy1="Dead"
      
   elif x+sx>ShyGuyx1-16 and x+sx<ShyGuyx1-18+6 and y>364 and y<396 and ShyGuy1=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   elif x+sx>ShyGuyx1-16+23 and x+sx<ShyGuyx1-12+6+23 and y>364 and y<396 and ShyGuy1=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   if ShyGuy1=="Dead" and ShyCounter1==0:
      if ShyGuypx1>=326:
         ShyGuypx1=262
         ShyGuyx1=ShyGuyx1+3

      if ShyCounter1==0:
         ShyGuypx1=ShyGuypx1+28
         ShyGuyx1=ShyGuyx1-1

   #Shy 2
   ShyCounter2=ShyCounter2+1
   if ShyCounter2==6:
      ShyCounter2=0
      if ShyGuy2=="Alive":
         ShyGuypx2=ShyGuypx2+23
      
   if ShyGuy2=="Alive":
      ShyGuyx2=ShyGuyx2+1*ShyGuyDir2
      WINDOW.blit(ShyGuy, (ShyGuyx2-sx,392),(ShyGuypx2, ShyGuypy2, 23, 30))
      
   if ShyGuy2=="Dead":
      WINDOW.blit(ShyGuy, (ShyGuyx2-sx,387),(ShyGuypx2, 176, 28, 37))

   if ShyGuypx2>=74 and ShyGuy2=="Alive":
      ShyGuypx2=5
      
   if ShyGuyx2<=90 and ShyGuy2=="Alive":
      ShyGuyDir2=1
      ShyGuypy2=68
      
   if ShyGuyx2>=250 and ShyGuy2=="Alive":
      ShyGuyDir2=-1
      ShyGuypy2=34

   if x+sx>ShyGuyx2 and x+sx<ShyGuyx2+21 and y>364 and y<368 and ShyGuy2=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx2=290
      ShyGuy2="Dead"
      
   elif x+sx+18>ShyGuyx2 and x+sx+18<ShyGuyx2+21 and y>364 and y<368 and ShyGuy2=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx2=290
      ShyGuy2="Dead"
      
   elif x+sx>ShyGuyx2-16 and x+sx<ShyGuyx2-18+6 and y>364 and y<396 and ShyGuy2=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   elif x+sx>ShyGuyx2-16+23 and x+sx<ShyGuyx2-12+6+23 and y>364 and y<396 and ShyGuy2=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   if ShyGuy2=="Dead" and ShyCounter2==0:
      if ShyGuypx2>=326:
         ShyGuypx2=262
         ShyGuyx2=ShyGuyx2+3

      if ShyCounter2==0:
         ShyGuypx2=ShyGuypx2+28
         ShyGuyx2=ShyGuyx2-1
   
   #Shy 3
   ShyCounter3=ShyCounter3+1
   if ShyCounter3==6:
      ShyCounter3=0
      if ShyGuy3=="Alive":
         ShyGuypx3=ShyGuypx3+23
      
   if ShyGuy3=="Alive":
      ShyGuyx3=ShyGuyx3+1*ShyGuyDir3
      WINDOW.blit(ShyGuy, (ShyGuyx3-sx,392),(ShyGuypx3, ShyGuypy3, 23, 30))
      
   if ShyGuy3=="Dead":
      WINDOW.blit(ShyGuy, (ShyGuyx3-sx,387),(ShyGuypx3, 176, 28, 37))

   if ShyGuypx3>=74 and ShyGuy3=="Alive":
      ShyGuypx3=5
      
   if ShyGuyx3<=1180 and ShyGuy3=="Alive":
      ShyGuyDir3=1
      ShyGuypy3=68
      
   if ShyGuyx3>=1450 and ShyGuy3=="Alive":
      ShyGuyDir3=-1
      ShyGuypy3=34

   if x+sx>ShyGuyx3 and x+sx<ShyGuyx3+21 and y>364 and y<368 and ShyGuy3=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx3=290
      ShyGuy3="Dead"
      
   elif x+sx+18>ShyGuyx3 and x+sx+18<ShyGuyx3+21 and y>364 and y<368 and ShyGuy3=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx3=290
      ShyGuy3="Dead"
      
   elif x+sx>ShyGuyx3-16 and x+sx<ShyGuyx3-18+6 and y>364 and y<396 and ShyGuy3=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   elif x+sx>ShyGuyx3-16+23 and x+sx<ShyGuyx3-12+6+23 and y>364 and y<396 and ShyGuy3=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   if ShyGuy3=="Dead" and ShyCounter3==0:
      if ShyGuypx3>=326:
         ShyGuypx3=262
         ShyGuyx3=ShyGuyx3+3

      if ShyCounter3==0:
         ShyGuypx3=ShyGuypx3+28
         ShyGuyx3=ShyGuyx3-1
         
   #Shy 4
   ShyCounter4=ShyCounter4+1
   if ShyCounter4==6:
      ShyCounter4=0
      if ShyGuy4=="Alive":
         ShyGuypx4=ShyGuypx4+23
      
   if ShyGuy4=="Alive":
      ShyGuyx4=ShyGuyx4+1*ShyGuyDir4
      WINDOW.blit(ShyGuy, (ShyGuyx4-sx,376),(ShyGuypx4, ShyGuypy4, 23, 30))
      
   if ShyGuy4=="Dead":
      WINDOW.blit(ShyGuy, (ShyGuyx4-sx,371),(ShyGuypx4, 176, 28, 37))

   if ShyGuypx4>=74 and ShyGuy4=="Alive":
      ShyGuypx4=5
      
   if ShyGuyx4<=660 and ShyGuy4=="Alive":
      ShyGuyDir4=1
      ShyGuypy4=68
      
   if ShyGuyx4>=1028 and ShyGuy4=="Alive":
      ShyGuyDir4=-1
      ShyGuypy4=34

   if x+sx>ShyGuyx4 and x+sx<ShyGuyx4+21 and y>348 and y<352 and ShyGuy4=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx4=290
      ShyGuy4="Dead"
      
   elif x+sx+18>ShyGuyx4 and x+sx+18<ShyGuyx4+21 and y>348 and y<352 and ShyGuy4=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx4=290
      ShyGuy4="Dead"
      
   elif x+sx>ShyGuyx4-16 and x+sx<ShyGuyx4-18+6 and y>348 and y<380 and ShyGuy4=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   elif x+sx>ShyGuyx4-16+23 and x+sx<ShyGuyx4-12+6+23 and y>348 and y<380 and ShyGuy4=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   if ShyGuy4=="Dead" and ShyCounter4==0:
      if ShyGuypx4>=326:
         ShyGuypx4=262
         ShyGuyx4=ShyGuyx4+3

      if ShyCounter4==0:
         ShyGuypx4=ShyGuypx4+28
         ShyGuyx4=ShyGuyx4-1

   #Shy 5
   ShyCounter5=ShyCounter5+1
   if ShyCounter5==6:
      ShyCounter5=0
      if ShyGuy5=="Alive":
         ShyGuypx5=ShyGuypx5+23
      
   if ShyGuy5=="Alive":
      ShyGuyx5=ShyGuyx5+1*ShyGuyDir5
      WINDOW.blit(ShyGuy, (ShyGuyx5-sx,376),(ShyGuypx5, ShyGuypy5, 23, 30))
      
   if ShyGuy5=="Dead":
      WINDOW.blit(ShyGuy, (ShyGuyx5-sx,371),(ShyGuypx5, 176, 28, 37))

   if ShyGuypx5>=74 and ShyGuy5=="Alive":
      ShyGuypx5=5
      
   if ShyGuyx5<=660 and ShyGuy5=="Alive":
      ShyGuyDir5=1
      ShyGuypy5=68
      
   if ShyGuyx5>=1028 and ShyGuy5=="Alive":
      ShyGuyDir5=-1
      ShyGuypy5=34

   if x+sx>ShyGuyx5 and x+sx<ShyGuyx5+21 and y>348 and y<352 and ShyGuy5=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx5=290
      ShyGuy5="Dead"
      
   elif x+sx+18>ShyGuyx5 and x+sx+18<ShyGuyx5+21 and y>348 and y<352 and ShyGuy5=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx5=290
      ShyGuy5="Dead"
      
   elif x+sx>ShyGuyx5-16 and x+sx<ShyGuyx5-18+6 and y>348 and y<380 and ShyGuy5=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   elif x+sx>ShyGuyx5-16+23 and x+sx<ShyGuyx5-12+6+23 and y>348 and y<380 and ShyGuy5=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   if ShyGuy5=="Dead" and ShyCounter5==0:
      if ShyGuypx5>=326:
         ShyGuypx5=262
         ShyGuyx5=ShyGuyx5+3

      if ShyCounter5==0:
         ShyGuypx5=ShyGuypx5+28
         ShyGuyx5=ShyGuyx5-1

   #Shy 6
   ShyCounter6=ShyCounter6+1
   if ShyCounter6==6:
      ShyCounter6=0
      if ShyGuy6=="Alive":
         ShyGuypx6=ShyGuypx6+23
      
   if ShyGuy6=="Alive":
      ShyGuyx6=ShyGuyx6+1*ShyGuyDir6
      WINDOW.blit(ShyGuy, (ShyGuyx6-sx,376),(ShyGuypx6, ShyGuypy6, 23, 30))
      
   if ShyGuy6=="Dead":
      WINDOW.blit(ShyGuy, (ShyGuyx6-sx,371),(ShyGuypx6, 176, 28, 37))

   if ShyGuypx6>=74 and ShyGuy6=="Alive":
      ShyGuypx6=5
      
   if ShyGuyx6<=660 and ShyGuy6=="Alive":
      ShyGuyDir6=1
      ShyGuypy6=68
      
   if ShyGuyx6>=1028 and ShyGuy6=="Alive":
      ShyGuyDir6=-1
      ShyGuypy6=34

   if x+sx>ShyGuyx6 and x+sx<ShyGuyx6+21 and y>348 and y<352 and ShyGuy6=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx6=290
      ShyGuy6="Dead"
      
   elif x+sx+18>ShyGuyx6 and x+sx+18<ShyGuyx6+21 and y>348 and y<352 and ShyGuy6=="Alive" and zU==0:
      ShyGuySound.play()
      zU=30
      ShyGuypx6=290
      ShyGuy6="Dead"
      
   elif x+sx>ShyGuyx6-16 and x+sx<ShyGuyx6-18+6 and y>348 and y<380 and ShyGuy6=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   elif x+sx>ShyGuyx6-16+23 and x+sx<ShyGuyx6-12+6+23 and y>348 and y<380 and ShyGuy6=="Alive":
      Dead=True
      pygame.mixer.stop()
      DeadSound.play()

   if ShyGuy6=="Dead" and ShyCounter6==0:
      if ShyGuypx6>=326:
         ShyGuypx6=262
         ShyGuyx6=ShyGuyx6+3

      if ShyCounter6==0:
         ShyGuypx6=ShyGuypx6+28
         ShyGuyx6=ShyGuyx6-1

#Coins
#Ground
   if Coin1==True and UnderGround==True:
      WINDOW.blit(Coin, (185,308),(0, 0, 14, 16))
      if x>170 and x<194 and y>293 and y<325:
         Coin1=False
         CoinSound.play()
         Collect=Collect+1

   if Coin2==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*1,308),(0, 0, 14, 16))
      if x>170+14*1 and x<194+14*1 and y>293 and y<325:
         Coin2=False
         CoinSound.play()
         Collect=Collect+1
         
   if Coin3==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*2,308),(0, 0, 14, 16))
      if x>170+14*2 and x<194+14*2 and y>293 and y<325:
         Coin3=False
         CoinSound.play()
         Collect=Collect+1

   if Coin4==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*3,308),(0, 0, 14, 16))
      if x>170+14*3 and x<194+14*3 and y>293 and y<325:
         Coin4=False
         CoinSound.play()
         Collect=Collect+1

   if Coin5==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*4,308),(0, 0, 14, 16))
      if x>170+14*4 and x<194+14*4 and y>293 and y<325:
         Coin5=False
         CoinSound.play()
         Collect=Collect+1
         
   if Coin6==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*5,308),(0, 0, 14, 16))
      if x>170+14*5 and x<194+14*5 and y>293 and y<325:
         Coin6=False
         CoinSound.play()
         Collect=Collect+1

   if Coin7==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*6,308),(0, 0, 14, 16))
      if x>170+14*6 and x<194+14*6 and y>293 and y<325:
         Coin7=False
         CoinSound.play()
         Collect=Collect+1

   if Coin8==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*7,308),(0, 0, 14, 16))
      if x>170+14*7 and x<194+14*7 and y>293 and y<325:
         Coin8=False
         CoinSound.play()
         Collect=Collect+1

   if Coin9==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*8,308),(0, 0, 14, 16))
      if x>170+14*8 and x<194+14*8 and y>293 and y<325:
         Coin9=False
         CoinSound.play()
         Collect=Collect+1

   if Coin10==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*9,308),(0, 0, 14, 16))
      if x>170+14*9 and x<194+14*9 and y>293 and y<325:
         Coin10=False
         CoinSound.play()
         Collect=Collect+1

   if Coin11==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*10,308),(0, 0, 14, 16))
      if x>170+14*10 and x<194+14*10 and y>293 and y<325:
         Coin11=False
         CoinSound.play()
         Collect=Collect+1

   if Coin12==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*11,308),(0, 0, 14, 16))
      if x>170+14*11 and x<194+14*11 and y>293 and y<325:
         Coin12=False
         CoinSound.play()
         Collect=Collect+1

   if Coin13==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*12,308),(0, 0, 14, 16))
      if x>170+14*12 and x<194+14*12 and y>293 and y<325:
         Coin13=False
         CoinSound.play()
         Collect=Collect+1

   if Coin14==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*13,308),(0, 0, 14, 16))
      if x>170+14*13 and x<194+14*13 and y>293 and y<325:
         Coin14=False
         CoinSound.play()
         Collect=Collect+1

   if Coin15==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*14,308),(0, 0, 14, 16))
      if x>170+14*14 and x<194+14*14 and y>293 and y<325:
         Coin15=False
         CoinSound.play()
         Collect=Collect+1
         
   if Coin16==True and UnderGround==True:
      WINDOW.blit(Coin, (185,292),(0, 0, 14, 16))
      if x>170 and x<194 and y>277 and y<325:
         Coin16=False
         CoinSound.play()
         Collect=Collect+1

   if Coin17==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*1,292),(0, 0, 14, 16))
      if x>170+14*1 and x<194+14*1 and y>277 and y<325:
         Coin17=False
         CoinSound.play()
         Collect=Collect+1
         
   if Coin18==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*2,292),(0, 0, 14, 16))
      if x>170+14*2 and x<194+14*2 and y>277 and y<325:
         Coin18=False
         CoinSound.play()
         Collect=Collect+1

   if Coin19==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*3,292),(0, 0, 14, 16))
      if x>170+14*3 and x<194+14*3 and y>277 and y<325:
         Coin19=False
         CoinSound.play()
         Collect=Collect+1

   if Coin20==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*4,292),(0, 0, 14, 16))
      if x>170+14*4 and x<194+14*4 and y>277 and y<325:
         Coin20=False
         CoinSound.play()
         Collect=Collect+1
         
   if Coin21==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*5,292),(0, 0, 14, 16))
      if x>170+14*5 and x<194+14*5 and y>277 and y<325:
         Coin21=False
         CoinSound.play()
         Collect=Collect+1

   if Coin22==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*6,292),(0, 0, 14, 16))
      if x>170+14*6 and x<194+14*6 and y>277 and y<325:
         Coin22=False
         CoinSound.play()
         Collect=Collect+1

   if Coin23==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*7,292),(0, 0, 14, 16))
      if x>170+14*7 and x<194+14*7 and y>277 and y<325:
         Coin23=False
         CoinSound.play()
         Collect=Collect+1

   if Coin24==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*8,292),(0, 0, 14, 16))
      if x>170+14*8 and x<194+14*8 and y>277 and y<325:
         Coin24=False
         CoinSound.play()
         Collect=Collect+1

   if Coin25==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*9,292),(0, 0, 14, 16))
      if x>170+14*9 and x<194+14*9 and y>277 and y<325:
         Coin25=False
         CoinSound.play()
         Collect=Collect+1

   if Coin26==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*10,292),(0, 0, 14, 16))
      if x>170+14*10 and x<194+14*10 and y>277 and y<325:
         Coin26=False
         CoinSound.play()
         Collect=Collect+1

   if Coin27==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*11,292),(0, 0, 14, 16))
      if x>170+14*11 and x<194+14*11 and y>277 and y<325:
         Coin27=False
         CoinSound.play()
         Collect=Collect+1

   if Coin28==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*12,292),(0, 0, 14, 16))
      if x>170+14*12 and x<194+14*12 and y>277 and y<325:
         Coin28=False
         CoinSound.play()
         Collect=Collect+1

   if Coin29==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*13,292),(0, 0, 14, 16))
      if x>170+14*13 and x<194+14*13 and y>277 and y<325:
         Coin29=False
         CoinSound.play()
         Collect=Collect+1

   if Coin30==True and UnderGround==True:
      WINDOW.blit(Coin, (185+14*14,292),(0, 0, 14, 16))
      if x>170+14*14 and x<194+14*14 and y>277 and y<325:
         Coin30=False
         CoinSound.play()
         Collect=Collect+1

#Falling

   if Coin31==True and UnderGround==True:
      WINDOW.blit(Coin, (190,136+16*1),(0, 0, 14, 16))
      if x>175 and x<200 and y>121+16*1 and y<152+16*1:
         Coin31=False
         CoinSound.play()
         Collect=Collect+1

   if Coin32==True and UnderGround==True:
      WINDOW.blit(Coin, (190,136+16*2),(0, 0, 14, 16))
      if x>175 and x<200 and y>121+16*2 and y<152+16*2:
         Coin32=False
         CoinSound.play()
         Collect=Collect+1

   if Coin33==True and UnderGround==True:
      WINDOW.blit(Coin, (190,136+16*3),(0, 0, 14, 16))
      if x>175 and x<200 and y>121+16*3 and y<152+16*3:
         Coin33=False
         CoinSound.play()
         Collect=Collect+1

   if Coin34==True and UnderGround==True:
      WINDOW.blit(Coin, (190,136+16*4),(0, 0, 14, 16))
      if x>175 and x<200 and y>121+16*4 and y<152+16*4:
         Coin34=False
         CoinSound.play()
         Collect=Collect+1

   if Coin35==True and UnderGround==True:
      WINDOW.blit(Coin, (190,136+16*5),(0, 0, 14, 16))
      if x>175 and x<200 and y>121+16*5 and y<152+16*5:
         Coin35=False
         CoinSound.play()
         Collect=Collect+1

   if Coin36==True and UnderGround==True:
      WINDOW.blit(Coin, (190,136+16*6),(0, 0, 14, 16))
      if x>175 and x<200 and y>121+16*6 and y<152+16*6:
         Coin36=False
         CoinSound.play()
         Collect=Collect+1

   if Coin37==True and UnderGround==True:
      WINDOW.blit(Coin, (190,136+16*7),(0, 0, 14, 16))
      if x>175 and x<200 and y>121+16*7 and y<152+16*7:
         Coin37=False
         CoinSound.play()
         Collect=Collect+1

   if Coin38==True and UnderGround==True:
      WINDOW.blit(Coin, (190,136+16*8),(0, 0, 14, 16))
      if x>175 and x<200 and y>121+16*8 and y<152+16*8:
         Coin38=False
         CoinSound.play()
         Collect=Collect+1

   if Coin39==True and UnderGround==True:
      WINDOW.blit(Coin, (190+14,136+16*1),(0, 0, 14, 16))
      if x>175+14 and x<200+14 and y>121+16*1 and y<152+16*1:
         Coin39=False
         CoinSound.play()
         Collect=Collect+1

   if Coin40==True and UnderGround==True:
      WINDOW.blit(Coin, (190+14,136+16*2),(0, 0, 14, 16))
      if x>175+14 and x<200+14 and y>121+16*2 and y<152+16*2:
         Coin40=False
         CoinSound.play()
         Collect=Collect+1

   if Coin41==True and UnderGround==True:
      WINDOW.blit(Coin, (190+14,136+16*3),(0, 0, 14, 16))
      if x>175+14 and x<200+14 and y>121+16*3 and y<152+16*3:
         Coin41=False
         CoinSound.play()
         Collect=Collect+1

   if Coin42==True and UnderGround==True:
      WINDOW.blit(Coin, (190+14,136+16*4),(0, 0, 14, 16))
      if x>175+14 and x<200+14 and y>121+16*4 and y<152+16*4:
         Coin42=False
         CoinSound.play()
         Collect=Collect+1

   if Coin43==True and UnderGround==True:
      WINDOW.blit(Coin, (190+14,136+16*5),(0, 0, 14, 16))
      if x>175+14 and x<200+14 and y>121+16*5 and y<152+16*5:
         Coin43=False
         CoinSound.play()
         Collect=Collect+1

   if Coin44==True and UnderGround==True:
      WINDOW.blit(Coin, (190+14,136+16*6),(0, 0, 14, 16))
      if x>175+14 and x<200+14 and y>121+16*6 and y<152+16*6:
         Coin44=False
         CoinSound.play()
         Collect=Collect+1

   if Coin45==True and UnderGround==True:
      WINDOW.blit(Coin, (190+14,136+16*7),(0, 0, 14, 16))
      if x>175+14 and x<200+14 and y>121+16*7 and y<152+16*7:
         Coin45=False
         CoinSound.play()
         Collect=Collect+1

   if Coin46==True and UnderGround==True:
      WINDOW.blit(Coin, (190+14,136+16*8),(0, 0, 14, 16))
      if x>175+14 and x<200+14 and y>121+16*8 and y<152+16*8:
         Coin46=False
         CoinSound.play()
         Collect=Collect+1

   if Collect>0:
      CoinCollect=CoinCollect+1
      Collect=Collect-1
   
#Character Blit
   if Menu!=True:
      WINDOW.blit(Sprite, (x,y),(px, py, pw, ph))

#UnderGround Variables
   #Going Down
   if ph<=23 and GoingDown==1:
      Rect1=True
      
   if Rect1==True:
      pygame.draw.rect(WINDOW, black, (0, RectY, 1000, 800))
      RectY=RectY+5
      
   if RectY==-100:
      pygame.mixer.stop()
      Underground.play()
      GoingDown=0
      sx=2017
      sy=492
      ph=30
      phcounter=0
      x=199
      y=0
      UnderGround=True
      Pipe.play()
      
   if RectY>=900:
      Rect1=False
      RectY=-800

   if UnderGround==True:
      sx=2016
      sy=492

   #Going In
   if pw<=7 and GoingIn==1:
      Rect2=True
      
   if Rect2==True:
      pygame.draw.rect(WINDOW, black, (RectX, 0, 1000, 800))
      RectX=RectX+10

   if RectX==-100:
      pygame.mixer.stop()
      SoundMusic.play()
      GoingIn=0

      ph=30
      phcounter=0
      x=599
      sx=1726
      y=250
      sy=0
      UnderGround=False
      Pipe.play()
      pw=30
      px=150

      
   if RectX>=1000:
      Rect2=False
      RectX=-1000


   #Menu
   if Menu==True:
      WINDOW.blit(Stage, (0,0),(mx, 0, 700, 450))
      if MenuOrder==1:
         WINDOW.blit(Menu1, (100,100),(0, 0, 500, 224))

      if MenuOrder==2:
         WINDOW.blit(Menu2, (100,100),(0, 0, 500, 224))

      if MenuOrder==3:
         WINDOW.blit(Menu3, (100,100),(0, 0, 500, 224))
      
   
      #Lock Movement
      zU=0
      x=0
      y=0

      #Arrow
      if LastDir=="L":
         WINDOW.blit(Left, (295,200),(0, 0, 100, 100))

      elif LastDir=="R":
         WINDOW.blit(Right, (295,200),(0, 0, 100, 100))
         

         
      #Moving Screen
      mx=mx+1
      if mx>2000:
         mx=0
       
#DEAD
   if Invincibility==True:
      Invincibility=True
      Dead=False

   elif Dead==True:
      #Reset
      x=20
      y=389
      px=150
      py=0
      sx=0
      sy=0
      StarCounter=0
      StarY=0
      EndCounter=0
      Endx=-700
      CoinCollect=0
      block1=0
      block2=0
      block3=0
      block4=0
      block5=0
      block6=0
      block7=0
      CoinCounter1=20
      CoinCounter2=20
      CoinCounter3=20
      CoinCounter4=20
      CoinCounter5=20
      CoinCounter6=20
      CoinCounter7=20
      ShyGuy1="Alive"
      ShyGuy2="Alive"
      ShyGuy3="Alive"
      ShyGuy4="Alive"
      ShyGuy5="Alive"
      ShyGuy6="Alive"
      ShyGuyx1=249
      ShyGuyx2=91
      ShyGuyx3=1180
      ShyGuyx4=790
      ShyGuyx5=830
      ShyGuyx6=870
      Coin1=True
      Coin2=True
      Coin3=True
      Coin4=True
      Coin5=True
      Coin6=True
      Coin7=True
      Coin8=True
      Coin9=True
      Coin10=True
      Coin11=True
      Coin12=True
      Coin13=True
      Coin14=True
      Coin15=True
      Coin16=True
      Coin17=True
      Coin18=True
      Coin19=True
      Coin20=True
      Coin21=True
      Coin22=True
      Coin23=True
      Coin24=True
      Coin25=True
      Coin26=True
      Coin27=True
      Coin28=True
      Coin29=True
      Coin30=True
      Coin31=True
      Coin32=True
      Coin33=True
      Coin34=True
      Coin35=True
      Coin36=True
      Coin37=True
      Coin38=True
      Coin39=True
      Coin40=True
      Coin41=True
      Coin42=True
      Coin43=True
      Coin44=True
      Coin45=True
      Coin46=True
      

      if Finish==False:
         pygame.draw.rect(WINDOW, black, (0, 0, 1000, 800))
         GameOverRender = font1.render((GameOver), True, white)
         GameOverRender2 = font1.render((GameOver2), True, white)

         WINDOW.blit(GameOverRender,(200,200))
         WINDOW.blit(GameOverRender2,(215,230))

#Finishing Game
   if Finish==True:
      pygame.draw.rect(WINDOW, black, (2685-sx, 333, 20, 20))
      WINDOW.blit(Star,(2685-sx,310-StarY))

      if StarCounter>=2:
         StarY=StarY+1
         StarCounter=0

      if StarY>30:
         StarY=1000

      if x>680 and MoveFinish==3:
         MoveFinish=4

      if MoveFinish==2:
         moveR=1
         moveL=1
         px=150
         music="play"
         
         if Char=="Mario":
            py=80

         elif Char=="Luigi":
            py=280

         if EndCounter>50:
            MoveFinish=3

      elif MoveFinish==3:
         if music=="play":
            Sunshine.play()
            music=0
         moveR=0
         
      elif MoveFinish==4:
         Endx=Endx+5
         WINDOW.blit(EndScreen, (Endx, 0),(0, 0, 700, 450))

         if Endx>=0:
            MoveFinish=5
            Dead=False

      elif MoveFinish==5:
         WINDOW.blit(EndScreen, (0, 0),(0, 0, 700, 450))
         Dead=True

      elif EndCounter<75:
         moveR=1
         moveL=0

      elif EndCounter>74 and EndCounter<150:
         moveL=1
         moveR=0

      else:
         EndCounter=0
         MoveFinish=MoveFinish+1
         
      StarCounter = StarCounter+1
      EndCounter = EndCounter+1

   if H==True:
      WINDOW.blit(Help,(50,35),(0,0,590,353))

#Display & FPS
   pygame.display.update()
   fpsClock.tick(FPS)
   print (x, y, Landing, zU, px)

