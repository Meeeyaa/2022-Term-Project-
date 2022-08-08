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
from playerClass import *
from bossClass import *




###################################################################


def appStarted(app):

    app.width = 960
    app.height = 650

    app.gameOver = False

    



    #__Player Sprites and Images__

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

    #--attack right
    img4 = app.loadImage("Meow-Knight_Attack_2.png")
    app.attackPlyrImageR = app.scaleImage(img4, 3)
    #--attack left
    app.attackPlyrImageL = app.attackPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img5 = app.loadImage("Meow-Knight_Death.png")
    app.deathPlyrImageR = app.scaleImage(img5, 3)
    #--dead left
    app.deathPlyrImageL = app.deathPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)
    

    #list of player images
    app.plyrImages = [(app.idlePlyrImageL, app.idlePlyrImageR), (app.runPlyrImageL, app.runPlyrImageR),
                      (app.jumpPlyrImageL, app.jumpPlyrImageR), (app.attackPlyrImageL, app.attackPlyrImageR),
                      (app.deathPlyrImageL, app.deathPlyrImageR)]


    app.Player = Player(app, 200, 500)
    spritestrip = app.idlePlyrImageR
    app.sprites = [ ]
    for i in range(6):
        sprite = spritestrip.crop((16*3, (64*3)*i, 16*3, (64*3)*(i+1)))
        app.sprites.append(sprite)
    app.spriteCounter = 0





    #__BossSprites and Images__

    #--idle right
    img1 = app.loadImage("Cat_itch_idle.png")
    app.idleBossImageR = app.scaleImage(img1, 3)
    #--idle left
    app.idleBossImageL = app.idleBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--run right
    img2 = app.loadImage("Cat_itch_walk.png")
    app.runBossImageR = app.scaleImage(img2, 3)
    #--run left
    app.runBossImageL = app.runBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--jump right
    img3 = app.loadImage("Cat_itch_jump.png")
    app.jumpBossImageR = app.scaleImage(img3, 3)
    #--jump left
    app.jumpBossImageL = app.jumpBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack right
    img4 = app.loadImage("Cat_itch_attack.png")
    app.attackBossImageR = app.scaleImage(img4, 3)
    #--attack left
    app.attackBossImageL = app.attackBossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img5 = app.loadImage("Cat_itch_attack.png")
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


    #list of background layers
    app.backgrounds = [app.bckgrndLyr1, app.bckgrndLyr2, app.bckgrndLyr3, app.bckgrndLyr4]








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


def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)



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
    canvas.create_rectangle(bTopX, bTopY, bBtmX, bBtmY, fill = "orange")



    if pBtmX <= pTopX:
        app.Player.currState = "death"
        canvas.create_text(app.width/2, app.height/2, text = "Player dead")
    
    if bTopX <= bBtmX:
        app.Boss.currState = "death"
        canvas.create_text(app.width/2, app.height/2, text = "Boss dead")
    

    


def drawSprites(app, canvas):
    #player
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(500, 500, image=ImageTk.PhotoImage(sprite))
    app.Player.draw(app, canvas)

    #boss
    app.Boss.draw(app, canvas)


    

def createBackground(app, canvas):
    for layer in range(len(app.backgrounds)):
        canvas.create_image(app.width/2, app.height/2,
                        image=ImageTk.PhotoImage(app.backgrounds[layer]))


def redrawAll(app, canvas):
    createBackground(app, canvas)
    drawSprites(app, canvas)
    drawHealthBars(app, canvas)
    
    

    

runApp(width=960, height=650)

