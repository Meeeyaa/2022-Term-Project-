#__Term Project__: Cat vs. Cats
#   Goal is to beat the evil boss (cat ai character) that gets more difficult 
#   each level


#Characters: 
# Player class
#   attributes: cx, cy, hp, attack
#   methods: getCx, getCy, getHp, attack_1, attack_2, attack_3

# Boss class
#   attributes: cx, cy, hp, attack
#   methods: getCx, getCy, getHp, attack_1, attack_2, attack_3
#   ai--> minimax algorithm + heuristic function



#Model:
#--appStarted; modes, level, turns


#Controller:
#--keyPressed; handles character and boss movement
#--timerFired; animates sprites



#View:
#--redrawAll; calls draw functions
#--createBackground
#--drawSprites
#--drawHealthBars



###################################################################

from cmu_112_graphics import *
from bossAndPlayerClass import *
import random
import time 


##################### MODEL #######################################



def changeLevel(app, level, wins):
    appStarted(app)
    app.level = level
    app.gamesWon = wins

def appStarted(app):
    restartGame(app)
    app.level = 1
    app.gamesWon = 0

def restartGame(app):
    app.mode = "splashScreenMode"
    

    app.width = 960
    app.height = 650

    app.gameOver = False

    app.bossTurn = False

    app.bossAttacking = False
    app.bigAttack = True
    app.recharging = False
    app.tooFar = True
    app.instructions = True

    app.paused = False



    app.dx = 10
    app.dy = 0

    

    app.msg = "The cat king has taken a little too much catnip and has become greedy and evil :O\nIts up to to cat knight to save the land from his corrupt rule!\nPress M to learn how to move or A to learn how to attack"


    #__Player Sprites and Images__
    #source: https://9e0.itch.io/cute-legends-cat-heroes

    #--idle right
    img1 = app.loadImage("Meow-Knight_Idle_0.1.png")
    app.idlePlyrImageR = app.scaleImage(img1, 1)
    
    #--idle left
    app.idlePlyrImageL = app.idlePlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--run right
    img2 = app.loadImage("Meow-Knight_Run_0.1.png")
    app.runPlyrImageR = app.scaleImage(img2, 1)
    #--run left
    app.runPlyrImageL = app.runPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)


    #--attack1 right
    img4 = app.loadImage("Meow-Knight_Attack_0.1.png")
    app.attack1PlyrImageR = app.scaleImage(img4, 2)
    #--attack1 left
    app.attack1PlyrImageL = app.attack1PlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack2 right
    img5 = app.loadImage("Meow-Knight_Attack_0.2.png")
    app.attack2PlyrImageR = app.scaleImage(img5, 3)
    #--attack2 left
    app.attack2PlyrImageL = app.attack2PlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack3 right
    img6 = app.loadImage("Meow-Knight_Attack_0.3.png")
    app.attack3PlyrImageR = app.scaleImage(img6, 2)
    #--attack3 left
    app.attack3PlyrImageL = app.attack3PlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img7 = app.loadImage("Meow-Knight_Death_0.1.png")
    app.deathPlyrImageR = app.scaleImage(img7, 2.5)
    #--dead left
    app.deathPlyrImageL = app.deathPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dodge left
    img8 = app.loadImage("Meow-Knight_Dodge_0.1.png")
    app.dodgePlyrImageL = app.scaleImage(img8, 2)
    #--dodge right
    app.dodgePlyrImageR = app.dodgePlyrImageL.transpose(Image.FLIP_LEFT_RIGHT)
    

    #list of player images
    app.plyrImages = [(app.idlePlyrImageL, app.idlePlyrImageR), (app.runPlyrImageL, app.runPlyrImageR),
                     (app.attack1PlyrImageL, app.attack1PlyrImageR), (app.attack2PlyrImageL, app.attack2PlyrImageR),
                     (app.attack3PlyrImageL, app.attack3PlyrImageR), (app.deathPlyrImageL, app.deathPlyrImageR),
                     (app.dodgePlyrImageR, app.dodgePlyrImageL)]




    app.Player = Player(app, 200, 500)






    #__BossSprites and Images__
    #source: https://9e0.itch.io/cute-legends-cat-heroes

    #--idle right
    img1 = app.loadImage("King_Mewrthur_Idle_0.1.png")
    img2 = app.scaleImage(img1, 2)   #left, upper, right, lower
    app.idleBossImageR = img2
    #--idle left
    app.idleBossImageL = app.idleBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--run right
    img2 = app.loadImage("King_Mewrthur_Run_0.1.png")
    app.runBossImageR = app.scaleImage(img2, 3)
    #--run left
    app.runBossImageL = app.runBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack1 right
    img4 = app.loadImage("King_Mewrthur_Attack_0.1.png")
    app.attack1BossImageR = app.scaleImage(img4, 3)
    #--attack1 left
    app.attack1BossImageL = app.attack1BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack2 right
    img5 = app.loadImage("King_Mewrthur_Attack_0.2.png")
    app.attack2BossImageR = app.scaleImage(img5, 3)
    #--attack2 left
    app.attack2BossImageL = app.attack2BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack3 right
    img6 = app.loadImage("King_Mewrthur_Attack_0.3.png")
    app.attack3BossImageR = app.scaleImage(img6, 2.5)
    #--attack3 left
    app.attack3BossImageL = app.attack3BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img7 = app.loadImage("King_Mewrthur_Death_0.1.png")
    app.deathBossImageR = app.scaleImage(img7, 2.5)
    #--dead left
    app.deathBossImageL = app.deathBossImageR.transpose(Image.FLIP_LEFT_RIGHT)
    

    #list of boss images
    app.bossImages = [(app.idleBossImageL, app.idleBossImageR), (app.runBossImageL, app.runBossImageR),
                       (app.attack1BossImageL, app.attack1BossImageR), (app.attack2BossImageL, app.attack2BossImageR),
                       (app.attack3BossImageL, app.attack3BossImageR),(app.deathBossImageL, app.deathBossImageR)]



    app.Boss = Boss(app, 700, 500)






    
    #__Background Images__
    #source: https://trixelized.itch.io/starstring-fields
    
    #layer 1
    app.bckgrndImg1 = app.loadImage("background_0.1.png")
    app.bckgrndLyr1 = app.scaleImage(app.bckgrndImg1, 4)

    #layer2
    app.bckgrndImg2 = app.loadImage("background_1.1.png")
    app.bckgrndLyr2 = app.scaleImage(app.bckgrndImg2, 4)

    #layer3
    app.bckgrndImg3 = app.loadImage("background_2.1.png")
    app.bckgrndLyr3 = app.scaleImage(app.bckgrndImg3, 4)

    #layer 4
    app.bckgrndImg4 = app.loadImage("background_3.png")
    app.bckgrndLyr4 = app.scaleImage(app.bckgrndImg4, 0.7)

    #layer 5
    app.bckgrndImg5 = app.loadImage("fg_0.png")
    app.bckgrndLyr5 = app.scaleImage(app.bckgrndImg5, 1)


    #list of background layers
    app.gameBackgrounds = [app.bckgrndLyr1, app.bckgrndLyr2, app.bckgrndLyr3, app.bckgrndLyr4]
    app.splashscreenBackgrounds = [app.bckgrndLyr1, app.bckgrndLyr3, app.bckgrndLyr5]
    app.helpscreenBackgrounds = [app.bckgrndLyr1, app.bckgrndLyr3]


def getCachedImage(app, image):
    #stores a cached version of the PhotoImage in the PIL/Pillow image
    #source: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingUrl
    if ('cachedPhotoImage' not in image.__dict__):
        image.cachedPhotoImage = ImageTk.PhotoImage(image)
    return image.cachedPhotoImage


################### CONTROLLER #################################


def gameOverMode_keyPressed(app, event):
    if event.key == "r":
        appStarted(app)


def instructionsMode_keyPressed(app, event):
    if event.key == "e":
        app.instructions = False
        app.paused = True
        app.mode = "gameMode"
    


def helpMode_keyPressed(app, event):
    if event.key == "a":
        app.msg = "Attack 1:\n  This attack inflicts -5 damage on the king, but it has +15 health effect\nUse when in dire need!\n  Attack 2: This attack inflicts -10 damage on the king, but it has +10 health effect\nAttack 3:\n    This attack inflicts -10 damage on the king, but it has +5 health effect\nThis move can only be used once every 10secs!"
    if event.key == "m":
        app.msg = "Use A and D to move left or right. Use W to dodge\nWhile dodging, the king will not be able to attack you!"
    if event.key == "e":
        app.mode = "splashScreenMode"
        app.msg = "The cat king has taken a little too much catnip and has become greedy and evil :O\nIts up to to cat knight to save the land from his corrupt rule!\nPress M to learn how to move or A to learn how to attack"
    if event.key == "b":
        app.msg = "The cat king has taken a little too much catnip and has become greedy and evil :O\nIts up to to cat knight to save the land from his corrupt rule!\nPress M to learn how to move or A to learn how to attack"



def splashScreenMode_keyPressed(app, event):
    if event.key == "c":
        app.mode = "gameMode"
    if event.key == "h":
        app.mode = "helpMode"



def gameMode_keyPressed(app, event):

    if event.key == "h":
        app.mode = "instructionsMode"
    else:
        app.instructions = False

    if app.gameOver:

        if event.key == "r":
            appStarted(app)

        elif event.key == "n":
            level = app.level
            wins = app.gamesWon

            if app.Player.currState != "Death":
                changeLevel(app, level+1, wins+1)
    
            else:
                changeLevel(app, level+1, wins)

        else:
            return

    if not app.paused:
        app.Player.action(app, event)

    if event.key == "p":
        app.paused = not app.paused

    


        
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2) + ((y2-y1)**2)**0.5

            


def gameMode_timerFired(app):

    if app.Player.currState == "Death" or app.Boss.currState == "Death":
        app.gameOver = True

    if app.level == 4:
        app.mode = "gameOverMode"

    if not app.Player.facingRight and app.Player.cx >= 960/2:
        app.Boss.facingRight = True
    else:
        app.Boss.facingRight = False

    if not app.paused and not app.gameOver:

        if time.time() - app.Boss.timeStart >= 1:
            #boss moves randomly and attacks within a certain distance
            app.Boss.cx = random.randint(400, 800)
            app.Boss.timeStart = time.time()

        if distance(app.Player.cx, app.Player.cy, app.Boss.cx, app.Boss.cy) <= 30000:
            app.Boss.action(app)
            app.tooFar = False
            app.bossTurn = True
        else:
            app.bossTurn = False
            app.tooFar = True
            app.Boss.currState = "Idle"
            app.Boss.health, app.Player.health = 0, 0
            app.Player.attack, app.Boss.attack = 0, 0


        #makes sure the player cannot go off the screen
        if app.Player.cx + 50 >= app.width:
            app.Player.cx = app.Player.cx%app.width
        if app.Player.cx - 50 <= 0:
            app.Player.cx = app.Player.cx%app.width

        if time.time() - app.Player.timeStart  >= 11:
            app.recharging = False
    


######################### VIEW ##################################



def gameOverMode_createBackground(app, canvas):
    for layer in range(len(app.splashscreenBackgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.splashscreenBackgrounds[layer]))


    
def gameOverMode_redrawAll(app, canvas):
    gameOverMode_createBackground(app, canvas)
    canvas.create_text(app.width/2, (app.height/2), text = f"Player won {app.gamesWon} out of 3 games",
                          font = "Arial 50", fill = "white")
    if app.gamesWon == 3 and app.level == 4:
        canvas.create_text(app.width/2, (app.height/2)+50, text = f"-- Player Won! :) --",
                           font = "Arial 18", fill = "white")
    else:
        canvas.create_text(app.width/2, (app.height/2)+50, text = f"-- Player Lost :( --",
                           font = "Arial 18", fill = "white")
    
    canvas.create_text(app.width/2, app.height*(9/10), text = "Press R to restart game",
                           font = "Arial 20 bold", fill = "white")



def gameMode_drawTimeRestriction(app, canvas):
    canvas.create_text(app.width*(1/40), app.height*(19/20)-10, text = f"Attack 3 Charging: {int(time.time()-app.Player.timeStart)}", fill = "white",
                        font = "Arial 10 bold", anchor = "w")


def gameMode_drawDamage(app, canvas):
    if app.Player.currState == "Attack_3" and app.recharging:
        canvas.create_text(app.width*(1/40), app.height*(2/20), text = f"Recharging! Cannot use Attack_3",
                            fill = "white", font = "Arial 10 bold", anchor = "w")
    else:
        canvas.create_text(app.width*(1/40), app.height*(2/20), text = f"{app.Player.currState}", fill = "white", font = "Arial 10 bold", anchor = "w")



def gameMode_drawAttack(app, canvas):
    if not app.gameOver:
        
        canvas.create_text(app.width*(5/40), app.height*(2/20)+80, text = f"Dmg: -{app.Boss.getAttack()}",
                            fill = "white", font = "Arial 12 bold", anchor = "e")
        canvas.create_text(app.width*(5/40), app.height*(2/20)+40, text = f"Hp: +{app.Player.getHealth()}",
                            fill = "white", font = "Arial 12 bold", anchor = "e")
        

        canvas.create_text(app.width*(35/40), app.height*(2/20)+80, text = f"Dmg: -{app.Player.getAttack()}",
                            fill = "white", font = "Arial 12 bold", anchor = "w")
        canvas.create_text(app.width*(35/40), app.height*(2/20)+40, text = f"Hp: +{app.Boss.getHealth()}",
                            fill = "white", font = "Arial 12 bold", anchor = "w")




def gameMode_drawHealthBars(app, canvas):
    if app.gameOver:

        if app.Player.currState == "Death":
            canvas.create_text(app.width/2, app.height/2, text = "Player dead",
                               fill = "white", font = "Arial 20 bold")
        else:
            canvas.create_text(app.width/2, app.height/2, text = "Boss dead",
                               fill = "white", font = "Arial 20 bold")

        canvas.create_text(app.width/2, (app.height/2)+40, text = "Press N for next level",
                           fill = "white", font = "Arial 18 bold")
  
        
    else:
    
        playerHp = app.Player.getHp()
        pTopX = app.width*(1/40)
        pTopY = app.height*(1/20)
        pBtmX = playerHp
        pBtmY = app.height*(2/30)
        canvas.create_rectangle(pTopX, pTopY, pBtmX, pBtmY, fill = "blue")
        # canvas.create_text(150, 55, text = f"{int(app.Player.getHp())}/960", fill = "white", font = "Arial 8 bold")

        bossHp = app.Boss.getHp()
        bTopX = app.width*(39/40)
        bTopY = app.height*(1/20)
        bBtmX = bossHp
        bBtmY = app.height*(2/30)
        canvas.create_rectangle(bTopX, bTopY, bBtmX, bBtmY, fill = "orange")
        # canvas.create_text(800, 55, text = f"{int(960-app.Boss.getHp())}/960", fill = "white", font = "Arial 8 bold" )

        if pBtmX <= pTopX:
            app.Player.currState = "Death"
        
        if bTopX <= bBtmX:
            app.Boss.currState = "Death"
    
    

def gameMode_drawDistanceWarning(app, canvas):
    canvas.create_text(app.width/2, app.height*(2/20)+40, text = "Get closer to attack the king!", fill = "white", font = "Arial 14 bold")
    

    
def gameMode_drawSprites(app, canvas):
    #player
    
    imagePlyr = app.Player.getImage()
    canvas.create_image(app.Player.cx, app.Player.cy, image=getCachedImage(app, imagePlyr))


    #boss
    imageBoss = app.Boss.getImage()
    canvas.create_image(app.Boss.cx, app.Boss.cy, image=getCachedImage(app, imageBoss))




def drawLevel(app, canvas):
    canvas.create_text(app.width*(1/2), app.height*(1/20), text = f"Level {app.level}",
                       fill = "white", font = "Arial 20 bold")


def gameMode_createBackground(app, canvas):
    for layer in range(len(app.gameBackgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.gameBackgrounds[layer]))



def gameMode_redrawAll(app, canvas): 

    gameMode_createBackground(app, canvas)
    drawLevel(app, canvas)
    gameMode_drawSprites(app, canvas)
    gameMode_drawHealthBars(app, canvas)
    if not app.gameOver: 
        gameMode_drawAttack(app, canvas)

        if app.recharging:
            canvas.create_text(app.width*(1/40), app.height*(18/20), text = f"\nPress J for Attack 1\nK for Attack 2\nAttack 3 Charging: {int(time.time()-app.Player.timeStart)}",
                            fill = "white", font = "Arial 10 bold", anchor = "w")
                

        else:
            canvas.create_text(app.width*(1/40), app.height*(18/20), text = "\nPress J for Attack 1\nK for Attack 2\nL for Attack 3",
                                fill = "white", font = "Arial 10 bold", anchor = "w")

        canvas.create_text(app.width*(39/40), app.height*(18/20), text = "\nPress H for help",
                            fill = "white", font = "Arial 10 bold", anchor = "e")
        canvas.create_text(app.width*(39/40), app.height*(18/20)+20, text = "\nPress P to pause/unpause",
                            fill = "white", font = "Arial 10 bold", anchor = "e")

        if app.Player.currState == "Attack_1" or app.Player.currState == "Attack_2" or app.Player.currState == "Attack_3" and distance(app.Player.cx, app.Player.cy, app.Boss.cx, app.Boss.cy) <= 30000:
            gameMode_drawDamage(app, canvas)

        if app.tooFar:
            gameMode_drawDistanceWarning(app, canvas)

        if app.bossTurn and app.Player.currState != "Dodge" and not app.gameOver:
            canvas.create_text(app.width/2, app.height*(3/20), text = "Oh no! Boss attacking!",
                            fill = "white", font = "Arial 14 bold")

        if app.paused:
            canvas.create_text(app.width*(1/2), app.height*(1/2), text = "-- Paused --",
                            fill = "white", font = "Arial 18 bold")
                            
        
        else:
            pass


    
        


def splashScreenMode_createBackground(app, canvas):
    for layer in range(len(app.splashscreenBackgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.splashscreenBackgrounds[layer]))


def splashScreenMode_redrawAll(app, canvas):
    splashScreenMode_createBackground(app, canvas)

    if app.level == 1:
        canvas.create_text(app.width/2, app.height/3, text = "Cats vs. Cats",
                           font = "Arial 50 bold", fill = "white")
        canvas.create_text(app.width/2, app.height/2, text = "Press C to continue or H for help",
                       font = "Arial 23 bold", fill = "white")


    elif app.level == 4:
        canvas.create_text(app.width/2, app.height/3, text = "Game Over",
                          font = "Arial 50 bold", fill = "white")
        canvas.create_text(app.width/2, app.height*(9/10), text = "Press C to continue",
                           font = "Arial 20 bold", fill = "white")
    else:
        canvas.create_text(app.width/2, app.height/3, text = f"Level: {app.level}",
                          font = "Arial 50 bold", fill = "white")
        canvas.create_text(app.width/2, (app.height/3)+50, text = f"-- Games Won: {app.gamesWon} --",
                          font = "Arial 18", fill = "white")

        canvas.create_text(app.width/2, app.height*(9/10), text = "Press C to continue",
                           font = "Arial 23 bold", fill = "white")


def helpMode_createBackground(app, canvas):
    for layer in range(len(app.helpscreenBackgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.helpscreenBackgrounds[layer]))



def helpMode_redrawAll(app, canvas):

    helpMode_createBackground(app, canvas)
    canvas.create_text(app.width/2, app.height*(1/4), text = app.msg,
                           font = "Arial 18 bold", fill = "white")

    if app.msg != "The cat king has taken a little too much catnip and has become greedy and evil :O\nIts up to to cat knight to save the land from his corrupt rule!\nPress M to learn how to move or A to learn how to attack":
        canvas.create_text(app.width*(1/3), app.height*(9/10), text = "Press B to go back",
                           font = "Arial 18 bold", fill = "white")
        canvas.create_text(app.width*(2/3), app.height*(9/10), text = "Press E to exit",
                           font = "Arial 18 bold", fill = "white")
    else:
        canvas.create_text(app.width/2, app.height*(9/10), text = "Press E to exit",
                           font = "Arial 18 bold", fill = "white")

def instructionsMode_createBackground(app, canvas):
    for layer in range(len(app.helpscreenBackgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.helpscreenBackgrounds[layer]))

def instructionsMode_redrawAll(app, canvas):

    instructionsMode_createBackground(app, canvas)
    canvas.create_text(app.width*(2/40), app.height*(1/3)-70, text = "-- Attacks --", font = "Arial 19 bold", fill = "white", anchor = "w")
    canvas.create_text(app.width*(30/40), app.height*(1/3)-70, text = "-- Movement --", font = "Arial 19 bold", fill = "white")
    
    msg1 = "\n\n    Attack 1:\n   -5 damage\n   +15 health\n\n  Attack 2:\n   -10 damage\n  +10 health\n\n   Attack 3:\n    -10 damage\n    +5 health\n** This move can only be used once every 10secs! **"
    msg2 = "\nUse A and D to move left or right.\nUse W to dodge\nWhile dodging, the king will not\nbe able to attack you!"
    canvas.create_text(app.width*(1/40), app.height/2, text = msg1, fill = "white", font = "Arial 16 bold", anchor = "w")
    canvas.create_text(app.width*(39/40), (app.height/2)-70, text = msg2, fill = "white", font = "Arial 16 bold", anchor = "e" )
    canvas.create_text(app.width/2, app.height*(9/10), text = "Press E to exit", font = "Arial 18 bold", fill = "white")
    
    

runApp(width=960, height=650)

