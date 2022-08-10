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


##################### MODEL #######################################


def appStarted(app):

    app.mode = "splashScreenMode"
    

    app.width = 960
    app.height = 650

    app.gameOver = False

    app.bossTurn = False

    app.timerDelay = 150

    app.level = 1
    app.gamesWon = 0


    #__Player Sprites and Images__
    #source: https://9e0.itch.io/cute-legends-cat-heroes

    #--idle right
    img1 = app.loadImage("Meow-Knight_Idle.png")
    app.idlePlyrImageR = app.scaleImage(img1, 3)
    #--idle left
    app.idlePlyrImageL = app.idlePlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--run right
    img2 = app.loadImage("Meow-Knight_Run.png")
    app.runPlyrImageR = app.scaleImage(img2, 3)
    #--run left
    app.runPlyrImageL = app.runPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--jump right
    img3 = app.loadImage("Meow-Knight_Jump.png")
    app.jumpPlyrImageR = app.scaleImage(img3, 3)
    #--jump left
    app.jumpPlyrImageL = app.jumpPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack1 right
    img4 = app.loadImage("Meow-Knight_Attack_1.png")
    app.attack1PlyrImageR = app.scaleImage(img4, 3)
    #--attack1 left
    app.attack1PlyrImageL = app.attack1PlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack2 right
    img5 = app.loadImage("Meow-Knight_Attack_2.png")
    app.attack2PlyrImageR = app.scaleImage(img5, 3)
    #--attack2 left
    app.attack2PlyrImageL = app.attack2PlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack3 right
    img6 = app.loadImage("Meow-Knight_Attack_3.png")
    app.attack3PlyrImageR = app.scaleImage(img6, 3)
    #--attack3 left
    app.attack3PlyrImageL = app.attack3PlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img7 = app.loadImage("Meow-Knight_Death.png")
    app.deathPlyrImageR = app.scaleImage(img7, 3)
    #--dead left
    app.deathPlyrImageL = app.deathPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)
    

    #list of player images
    app.plyrImages = [(app.idlePlyrImageL, app.idlePlyrImageR), (app.runPlyrImageL, app.runPlyrImageR),
                      (app.jumpPlyrImageL, app.jumpPlyrImageR), (app.attack1PlyrImageL, app.attack1PlyrImageR),
                      (app.attack2PlyrImageL, app.attack2PlyrImageR), (app.attack3PlyrImageL, app.attack3PlyrImageR),
                      (app.deathPlyrImageL, app.deathPlyrImageR)]

    app.plyrImgDims = {"Idle": [6], "Run": [8], "Jump": [6], "Attack1": [4],
                        "Attack2": [4], "Attack3": [4], "Death": [6]}


    app.Player = Player(app, 200, 500)








    #__BossSprites and Images__
    #source: https://9e0.itch.io/cute-legends-cat-heroes

    #--idle right
    img1 = app.loadImage("King_Mewrthur_Idle.png")
    img2 = app.scaleImage(img1, 3)   #left, upper, right, lower
    app.idleBossImageR = img2
    #--idle left
    app.idleBossImageL = app.idleBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--run right
    img2 = app.loadImage("King_Mewrthur_Run.png")
    app.runBossImageR = app.scaleImage(img2, 3)
    #--run left
    app.runBossImageL = app.runBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--jump right
    img3 = app.loadImage("King_Mewrthur_Jump.png")
    app.jumpBossImageR = app.scaleImage(img3, 3)
    #--jump left
    app.jumpBossImageL = app.jumpBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack1 right
    img4 = app.loadImage("King_Mewrthur_Attack_1.png")
    app.attack1BossImageR = app.scaleImage(img4, 3)
    #--attack1 left
    app.attack1BossImageL = app.attack1BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack2 right
    img5 = app.loadImage("King_Mewrthur_Attack_2.png")
    app.attack2BossImageR = app.scaleImage(img5, 3)
    #--attack2 left
    app.attack2BossImageL = app.attack2BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack3 right
    img6 = app.loadImage("King_Mewrthur_Attack_3.png")
    app.attack3BossImageR = app.scaleImage(img6, 3)
    #--attack3 left
    app.attack3BossImageL = app.attack3BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img7 = app.loadImage("King_Mewrthur_Death.png")
    app.deathBossImageR = app.scaleImage(img7, 3)
    #--dead left
    app.deathBossImageL = app.deathBossImageR.transpose(Image.FLIP_LEFT_RIGHT)
    

    #list of boss images
    app.bossImages = [(app.idleBossImageL, app.idleBossImageR), (app.runBossImageL, app.runBossImageR),
                      (app.jumpBossImageL, app.jumpBossImageR), (app.attack1BossImageL, app.attack1BossImageR),
                      (app.attack2BossImageL, app.attack2BossImageR), (app.attack3BossImageL, app.attack3BossImageR),
                      (app.deathBossImageL, app.deathBossImageR)]

    app.bossImgDims = {"Idle": [6], "Run": [8], "Jump": [6], "Attack1": [4],
                        "Attack2": [4], "Attack3": [4], "Death": [6]}



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





################### CONTROLLER #################################


def gameOverMode_keyPressed(app, event):
    if event.key == "r":
        appStarted(app)



def gameMode_gameOver(app):
    if app.Player.currState == "Death" or app.Boss.currState == "Death":
        app.gameOver = True
        
        if app.level == 2:
            app.mode = "gameOverMode"



def splashScreenMode_keyPressed(app, event):
    if event.key == "c":
        app.mode = "gameMode"



def gameMode_keyPressed(app, event):

    if app.gameOver:

        if event.key == "r":
            appStarted(app)

        elif event.key == "n":

            if app.Boss.currState == "Death":
                appStarted(app)
                app.gamesWon += 1
                app.level += 1
    
    
            else:
                appStarted(app)
                app.level += 1  

        else:
            return


    if not app.bossTurn:
        app.Player.action(app, event)
        

        
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2) + ((y2-y1)**2)**5

def gameMode_timerFired(app):
    gameMode_gameOver(app) 
   
    

    

    if app.bossTurn:
        app.Boss.action(app)
        print(f'bossState: {app.Boss.currState}')
        print('boss Turn')

        
    

######################### VIEW ##################################



def gameOverMode_createBackground(app, canvas):
    for layer in range(len(app.splashscreenBackgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.splashscreenBackgrounds[layer]))

    
def gameOverMode_redrawAll(app, canvas):
    gameOverMode_createBackground(app, canvas)
    canvas.create_text(app.width/2, (app.height/2), text = f"Player won {app.gamesWon} out of 2 games",
                          font = "Arial 50", fill = "white")
    if app.gamesWon == 3:
        canvas.create_text(app.width/2, (app.height/2)+50, text = f"-- Player Won! :) --",
                           font = "Arial 18", fill = "white")
    else:
        canvas.create_text(app.width/2, (app.height/2)+50, text = f"-- Player Lost :( --",
                           font = "Arial 18", fill = "white")
    
    canvas.create_text(app.width/2, app.height*(9/10), text = "Press r to restart game",
                           font = "Arial 20 bold", fill = "white")


def gameMode_drawAttack(app, canvas):
    if app.Player.currState == "Attack1" or app.Player.currState == "Attack2" or app.Player.currState == "Attack3":
        canvas.create_text(app.width*(5/40), app.height*(2/20)+40, text = f"{app.Player.currState}\nDmge: {app.Player.getAttack()}",
                            fill = "white", font = "Arial 12", anchor = "e")
    
    if app.Boss.currState == "Attack1" or app.Boss.currState == "Attack2" or app.Boss.currState == "Attack3":
        canvas.create_text(app.width*(35/40), app.height*(2/20)+40, text = f"{app.Boss.currState}\nDmg: {app.Boss.getAttack()}",
                            fill = "white", font = "Arial 12", anchor = "w")


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
        canvas.create_text(150, 55, text = f"{int(app.Player.getHp())}/960", fill = "white", font = "Arial 8")

        bossHp = app.Boss.getHp()
        bTopX = app.width*(39/40)
        bTopY = app.height*(1/20)
        bBtmX = bossHp
        bBtmY = app.height*(2/30)
        canvas.create_rectangle(bTopX, bTopY, bBtmX, bBtmY, fill = "orange")
        canvas.create_text(800, 55, text = f"{int(app.Boss.getHp())}/960", fill = "white", font = "Arial 8" )

        if pBtmX <= pTopX:
            app.Player.currState = "Death"
        
        if bTopX <= bBtmX:
            app.Boss.currState = "Death"
    
    

    
    

    
def gameMode_drawSprites(app, canvas):
    #player
    app.Player.draw(app, canvas)

    #boss
    canvas.create_image(app.Boss.cx, app.Boss.cy, image=ImageTk.PhotoImage(app.Boss.getImage()))




def drawLevel(app, canvas):
    canvas.create_text(app.width*(1/2), app.height*(1/20), text = f"Level {app.level}",
                       fill = "white", font = "Arial 23")


def gameMode_createBackground(app, canvas):
    for layer in range(len(app.gameBackgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.gameBackgrounds[layer]))



def gameMode_redrawAll(app, canvas):
    gameMode_createBackground(app, canvas)
    drawLevel(app, canvas)
    gameMode_drawSprites(app, canvas)
    gameMode_drawHealthBars(app, canvas)
    gameMode_drawAttack(app, canvas)



def splashScreenMode_createBackground(app, canvas):
    for layer in range(len(app.splashscreenBackgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.splashscreenBackgrounds[layer]))


def splashScreenMode_redrawAll(app, canvas):
    splashScreenMode_createBackground(app, canvas)

    if app.level == 1:
        canvas.create_text(app.width/2, app.height/3, text = "Cats vs. Cats",
                           font = "Arial 50 bold", fill = "white")
        canvas.create_text(app.width/2, app.height/2, text = "Press C to continue",
                       font = "Arial 23 bold", fill = "white")

    else:
        canvas.create_text(app.width/2, app.height/3, text = f"Level {app.level}",
                          font = "Arial 50 bold", fill = "white")
        canvas.create_text(app.width/2, (app.height/3)+50, text = f"--Games Won: {app.gamesWon}--",
                          font = "Arial 18", fill = "white")

        canvas.create_text(app.width/2, app.height*(9/10), text = "Press C to continue",
                           font = "Arial 23 bold", fill = "white")


    

runApp(width=960, height=650)

