import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
RCTRL = 4
RSHIFT = 5

A=0
D=1
W = 2
S = 3
LCTRL = 4
Q = 5

#MAP: 1 is grass, 2 is brick
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 1],
       [0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0 ,0 ,0, 1],
       [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 3 ,0 ,0, 1],
       [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 3, 3, 3 ,3 ,0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 1],
       [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0 ,0 ,0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 1],
       [0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0 ,0 ,0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0 ,0 ,0, 1],
       [2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0 ,0 ,0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 1],
       [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2 ,0 ,0, 1],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2 ,0 ,0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1]]

brick = pygame.image.load('brick.png') #load your spritesheet
dirt = pygame.image.load('dirt.png') #load your spritesheet
cloud = pygame.image.load('block.png')
Link = pygame.image.load('chicken.png') #load your spritesheet
Rabbit = pygame.image.load('rabbit.png') #load your spritesheet
SwordL = pygame.image.load('swordL.png')
SwordR = pygame.image.load('swordR.png')

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
Xspeed = 0 #guess what this is
Yspeed = 0 #guess what this also is
sword1 = False

#player2 variables
xpos2 = 200 #xpos of player
ypos2 = 200 #ypos of player
vx2 = 0 #x velocity of player
vy2 = 0 #y velocity of player
keys2 = [False, False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround2 = False #this variable stops gravity from pulling you down more when on a platform
Xspeed2 = 0 #guess what this is
Yspeed2 = 0 #guess what this also is
sword2 = False

#animation variables
frameWidth = 48
frameHeight = 48
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

#animation variables
frameWidth2 = 32
frameHeight2 = 32
RowNum2 = 0 #for left animation, this will need to change for other animations
frameNum2 = 0
ticker2 = 0
direction2 = DOWN

while not gameover:
    clock.tick(60) #FPS
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_RCTRL:
                keys[RCTRL]=True
            elif event.key == pygame.K_RSHIFT:
                keys[RSHIFT]=True
            elif event.key == pygame.K_a:
                keys2[A]=True
            elif event.key == pygame.K_d:
                keys2[D]=True
            elif event.key == pygame.K_w:
                keys2[W]=True
            elif event.key == pygame.K_LCTRL:
                keys2[LCTRL]=True
            elif event.key == pygame.K_q:
                keys2[Q]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_RCTRL:
                keys[RCTRL]=False
            elif event.key == pygame.K_RSHIFT:
                keys[RSHIFT]=False
            elif event.key == pygame.K_a:
                keys2[A]=False
            elif event.key == pygame.K_d:
                keys2[D]=False
            elif event.key == pygame.K_w:
                keys2[W]=False
            elif event.key == pygame.K_LCTRL:
                keys2[LCTRL]=False
            elif event.key == pygame.K_q:
                keys2[Q]=False
          

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        if keys[RCTRL] == True: #only jump when on the ground
            Xspeed = -5
            vx = Xspeed
        else:
            Xspeed = -3
            vx = Xspeed
        RowNum = 0
        direction = LEFT
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        if keys[RCTRL] == True: #only jump when on the ground
            Xspeed = 5
            vx = Xspeed
        else:
            Xspeed = 3
            vx = Xspeed
        RowNum = 1
        direction = RIGHT
    #turn off velocity
    else:
        Xspeed = 0
        vx = 0
    #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        if keys[RCTRL] == True: #only jump when on the ground
            Yspeed = -7
            vy = Yspeed
        else:
            Yspeed = -5
            vy = Yspeed
        RowNum = 4
        isOnGround = False
        direction = UP
    #ATTACKING
    if keys[RSHIFT] == True:
        sword1 = True
    else:
        sword1 = False
    
        
    xpos+=vx #update player xpos
    ypos+=vy

    #LEFT MOVEMENT
    if keys2[A]==True:
        if keys2[LCTRL] == True: #only jump when on the ground
            Xspeed2 = -5
            vx2 = Xspeed2
        else:
            Xspeed2 = -3
            vx2 = Xspeed2
        RowNum2 = 1
        direction2 = LEFT
    #RIGHT MOVEMENT
    elif keys2[D] == True:
        if keys2[LCTRL] == True: #only jump when on the ground
            Xspeed2 = 5
            vx2 = Xspeed2
        else:
            Xspeed2 = 3
            vx2 = Xspeed2
        RowNum2 = 2
        direction2 = RIGHT
    #turn off velocity
    else:
        Xspeed2 = 0
        vx2 = 0
    #JUMPING
    if keys2[W] == True and isOnGround2 == True: #only jump when on the ground
        if keys2[LCTRL] == True: #only jump when on the ground
            Yspeed2 = -7
            vy2 = Yspeed2
        else:
            Yspeed2 = -5
            vy2 = Yspeed2
        RowNum2 = 0
        isOnGround2 = False
        direction2 = UP
    
    
        
    xpos2+=vx2 #update player xpos
    ypos2+=vy2
    
    
    #COLLISION
    
    #collision with feetsies
    if map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==2:
        isOnGround = True
        Yspeed=0
        vy=0
        
    else:
        isOnGround = False
        
    #bump your head, ouch!
    if map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==2:
        Yspeed=0
        vy=0
        
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos+frameHeight-10)/50)][int((xpos)/50)]==1 or map[int((ypos)/50)][int((xpos)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos)/50)]==2 or map[int((ypos)/50)][int((xpos)/50)]==2 ) and direction == LEFT:
        xpos-=Xspeed
        
    #right collision needed here
    if (map[int((ypos+frameHeight-10)/50)][int((xpos+frameWidth)/50)]==1 or map[int((ypos)/50)][int((xpos+frameWidth)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos+frameWidth)/50)]==2 or map[int((ypos)/50)][int((xpos+frameWidth)/50)]==2 ) and direction == RIGHT:
        xpos-=Xspeed
        
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos+frameWidth > 800:
        xpos-=(Xspeed*-1)
    if xpos<0:
        xpos+=(Xspeed*-1)

    
    #stop falling if on bottom of game screen
    if ypos > 800-frameHeight:
        isOnGround = True
        Yspeed = 0
        vy = 0
        ypos = 800-frameHeight
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
        
        
    #collision with feetsies
    if map[int((ypos2+frameHeight2)/50)][int((xpos2+frameWidth2/2)/50)]==1 or map[int((ypos2+frameHeight2)/50)][int((xpos2+frameWidth2/2)/50)]==2:
        isOnGround2 = True
        Yspeed2=0
        vy2=0
        
    else:
        isOnGround2 = False
        
    #bump your head, ouch!
    if map[int((ypos2)/50)][int((xpos2+frameWidth2/2)/50)]==1 or map[int((ypos2)/50)][int((xpos2+frameWidth2/2)/50)]==2:
        Yspeed2=0
        vy2=0
        
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos2+frameHeight2-10)/50)][int((xpos2)/50)]==1 or map[int((ypos2)/50)][int((xpos2)/50)]==1 or map[int((ypos2+frameHeight2-10)/50)][int((xpos2)/50)]==2 or map[int((ypos2)/50)][int((xpos2)/50)]==2 ) and direction2 == LEFT:
        xpos2-=Xspeed2
        
    #right collision needed here
    if (map[int((ypos2+frameHeight2-10)/50)][int((xpos2+frameWidth2)/50)]==1 or map[int((ypos2)/50)][int((xpos2+frameWidth2)/50)]==1 or map[int((ypos2+frameHeight2-10)/50)][int((xpos2+frameWidth2)/50)]==2 or map[int((ypos2)/50)][int((xpos2+frameWidth2)/50)]==2 ) and direction2 == RIGHT:
        xpos2-=Xspeed2
        
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos2+frameWidth2 > 800:
        xpos2-=(Xspeed2*-1)
    if xpos2<0:
        xpos2+=(Xspeed2*-1)

    
    #stop falling if on bottom of game screen
    if ypos2 > 800-frameHeight2:
        isOnGround2 = True
        Yspeed2 = 0
        vy2 = 0
        ypos2 = 800-frameHeight2
    
    #gravity
    if isOnGround2 == False:
        vy2+=.2 #notice this grows over time, aka ACCELERATION
    

        
    #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information

    if vx != 0 or vy!=0: #animate when moving
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>3: 
           frameNum = 0

    if vx2 != 0 or vy2!=0: #animate when moving
        ticker2+=1
        if ticker2%10==0: #only change frames every 10 ticks
          frameNum2+=1
        if frameNum2>3: 
           frameNum2 = 0
  
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
            
    screen.fill((104, 153, 252)) #wipe screen so it doesn't smear
    
    #draw map
    for i in range (16):
        for j in range(16):
            if map[i][j]==1:
                screen.blit(dirt, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(brick, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==3:
                screen.blit(cloud, (j*50, i*50), (0, 0, 50, 50))
        
    
    screen.blit(Link, (xpos, ypos), (frameWidth*RowNum, frameNum*frameHeight, frameWidth, frameHeight))
    screen.blit(Rabbit, (xpos2, ypos2), (frameWidth2*RowNum2, frameNum2*frameHeight2, frameWidth2, frameHeight2))
    if sword1 == True:
        if direction == RIGHT:
            screen.blit(SwordR, (xpos-(frameWidth/2)+frameWidth+5, ypos), (0, 0, 160, 160))
        else:
            screen.blit(SwordL, (xpos-(frameWidth/2), ypos), (0, 0, 160, 160))
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()


