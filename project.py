#__Term Project__: Cat vs. Dogs
#Idea: Player can chose which cat to play as
#goal is to beat the evil boss (dog ai character) that gets more difficult 
#once level is passed, player earns prize which can be used to
#boss is AI

#Characters: 
# cat class
# attributes: hp, healing, damage, duration of special skill

# dog class
# attributes: hp, damage, healing, skill (best choice made by ai)
# ai--> level 1; easy ai, random number genrator for moves
#       level 2; medium ai, if statement 
#       level 3; minimax ai

#Model:
#--


#View:
#--modes for different parts of game (start screen, game screen, store)
#--

#Controller:
#--keyPressed for moving character (a,w,s,d)
#--timerFired for duration of special skill, timed quest


#add music: fight musics, victory toon, loser toon


###################################################################

from cmu_112_graphics import *
from characterClass import *





###################################################################


def appStarted(app):
    app.width = 1000
    app.height = 720

    app.gameOver = False

    



    #__Player Sprites and Images__

    #--idle right
    img1 = app.loadImage("heroIdle.png")
    app.idlePlyrImageR = app.scaleImage(img1, 3)
    #--idle left
    app.idlePlyrImageL = app.idlePlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--run right
    img2 = app.loadImage("heroRun.png")
    app.runPlyrImageR = app.scaleImage(img2, 3)
    #--run left
    app.runPlyrImageL = app.runPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--jump right
    img3 = app.loadImage("heroJumpUp.png")
    app.jumpPlyrImageR = app.scaleImage(img3, 3)
    #--jump left
    app.jumpPlyrImageL = app.jumpPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack right
    img4 = app.loadImage("heroAttack.png")
    app.attackPlyrImageR = app.scaleImage(img4, 3)
    #--attack left
    app.attackPlyrImageL = app.attackPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img5 = app.loadImage("heroDeath.png")
    app.deathPlyrImageR = app.scaleImage(img5, 3)
    #--dead left
    app.deathPlyrImageL = app.deathPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)
    

    #list of player images
    app.plyrImages = [(app.idlePlyrImageL, app.idlePlyrImageR), (app.runPlyrImageL, app.runPlyrImageR),
                      (app.jumpPlyrImageL, app.jumpPlyrImageR), (app.attackPlyrImageL, app.attackPlyrImageR),
                      (app.deathPlyrImageL, app.deathPlyrImageR)]


    app.Player = Player(app, 200, 500)





    #__BossSprites and Images__

    #--idle right
    img1 = app.loadImage("goblinIdle.png")
    app.idleBossImageR = app.scaleImage(img1, 3)
    #--idle left
    app.idleBossImageL = app.idleBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--run right
    img2 = app.loadImage("goblinRun.png")
    app.runBossImageR = app.scaleImage(img2, 3)
    #--run left
    app.runBossImageL = app.runBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--jump right
    img3 = app.loadImage("goblinIdle.png")
    app.jumpBossImageR = app.scaleImage(img3, 3)
    #--jump left
    app.jumpBossImageL = app.jumpBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack right
    img4 = app.loadImage("goblinAttack.png")
    app.attackBossImageR = app.scaleImage(img4, 3)
    #--attack left
    app.attackBossImageL = app.attackBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img5 = app.loadImage("goblinDeath.png")
    app.deathBossImageR = app.scaleImage(img5, 3)
    #--dead left
    app.deathBossImageL = app.deathBossImageR.transpose(Image.FLIP_LEFT_RIGHT)
    

    #list of boss images
    app.bossImages = [(app.idleBossImageL, app.idleBossImageR), (app.runBossImageL, app.runBossImageR),
                      (app.jumpBossImageL, app.jumpBossImageR), (app.attackBossImageL, app.attackBossImageR),
                      (app.deathBossImageL, app.deathBossImageR)]



    app.Boss = Boss(app, 700, 500)





    
    #__Background Images__
    
    #layer 1
    app.bckgrdImg1 = app.loadImage("background_0.png")
    app.bckgrndLyr1 = app.scaleImage(app.bckgrdImg1, 4)

    #layer2
    app.bckgrdImg2 = app.loadImage("background_1.png")
    app.bckgrndLyr2 = app.scaleImage(app.bckgrdImg2, 4)

    #layer3
    app.bckgrdImg3 = app.loadImage("background_2.png")
    app.bckgrndLyr3 = app.scaleImage(app.bckgrdImg3, 4)

    #layer 4
    app.bckgrdImg4 = app.loadImage("tileset.png")
    app.bckgrndLyr4 = app.scaleImage(app.bckgrdImg4, 4)


    #list of background layers
    app.backgrounds = [app.bckgrndLyr1, app.bckgrndLyr2, app.bckgrndLyr3]


def gameOver(app):
    if app.Player.currState == "death" or app.Boss.currState == "death":
        app.gameOver = True



def keyPressed(app, event):
    if not app.gameOver:
        print(app.Player.currState)
        app.Player.move(app, event)
        print(app.Boss.currState)
        app.Boss.move(app, event)
    else:
        return




def drawHealthBars(app, canvas):
    
    playerHp = app.Player.getHp()
    pTopX = app.width*(1/40)
    pTopY = app.height*(1/20)
    pBtmX = playerHp
    pBtmY = app.height*(2/30)
    canvas.create_rectangle(pTopX, pTopY, pBtmX, pBtmY, fill = "blue")

    bossHp = app.Boss.getHp()
    bTopX = app.width*(39/40)
    bTopY = app.height*(1/20)
    bBtmX = bossHp
    bBtmY = app.height*(2/30)
    canvas.create_rectangle(bTopX, bTopY, bBtmX, bBtmY, fill = "green")



    if pBtmX <= pTopX:
        app.Player.currState = "death"
        canvas.create_text(app.width/2, app.height/2, text = "Player dead")
    
    if bTopX <= bBtmX:
        app.Boss.currState = "death"
        canvas.create_text(app.width/2, app.height/2, text = "Boss dead")
    

    


def drawSprites(app, canvas):
    #player
    app.Player.draw(app, canvas)

    #boss
    app.Boss.draw(app, canvas)


    

def createBackground(app, canvas):
    for layer in range(len(app.backgrounds)-1):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.backgrounds[layer]))


def redrawAll(app, canvas):
    createBackground(app, canvas)
    drawSprites(app, canvas)
    drawHealthBars(app, canvas)
    
    

    

runApp(width=960, height=650)

