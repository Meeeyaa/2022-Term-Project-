#__Term Project__: Cat vs. Cats
#Goal is to beat the evil boss (dog ai character) that gets more difficult 
#each level

#Characters: 
# player class
# attributes: hp, healing, damage

# boss class
# attributes: hp, damage, healing, attack (best choice made by ai)
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
from bossAndPlayerClass import *




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

    #--attack1 right
    img4 = app.loadImage("Cat_itch_attack.png")
    app.attack1BossImageR = app.scaleImage(img4, 3)
    #--attack1 left
    app.attack1BossImageL = app.attack1BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack2 right
    img5 = app.loadImage("Cat_itch_attack.png")
    app.attack2BossImageR = app.scaleImage(img5, 3)
    #--attack2 left
    app.attack2BossImageL = app.attack2BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack3 right
    img6 = app.loadImage("Cat_itch_attack.png")
    app.attack3BossImageR = app.scaleImage(img6, 3)
    #--attack3 left
    app.attack3BossImageL = app.attack3BossImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img7 = app.loadImage("Cat_itch_attack.png")
    app.deathBossImageR = app.scaleImage(img7, 3)
    #--dead left
    app.deathBossImageL = app.deathBossImageR.transpose(Image.FLIP_LEFT_RIGHT)
    

    #list of boss images
    app.bossImages = [(app.idleBossImageL, app.idleBossImageR), (app.runBossImageL, app.runBossImageR),
                      (app.jumpBossImageL, app.jumpBossImageR), (app.attack1BossImageL, app.attack1BossImageR),
                      (app.attack2BossImageL, app.attack2BossImageR), (app.attack3BossImageL, app.attack3BossImageR),
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
    if app.Player.currState == "Death" or app.Boss.currState == "Death":
        app.gameOver = True



def keyPressed(app, event):
    if app.gameOver:
        if event.key == "r":
            appStarted(app)
        else:
            return
    else:
        print(app.Player.currState)
        app.Player.action(app, event)
        print(app.Boss.currState)
        app.Boss.action(app, event)

    if event.key == "r":
        appStarted(app)


def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
    gameOver(app)



def drawHealthBars(app, canvas):
    if app.gameOver:

        if app.Player.currState == "Death":
            canvas.create_text(app.width/2, app.height/2, text = "Player dead", fill = "white", font = "Arial 20 bold")
            canvas.create_text(app.width/2, (app.height/2)+40, text = "Press R to restart", fill = "white", font = "Arial 18 bold")
        else:
            canvas.create_text(app.width/2, app.height/2, text = "Boss dead", fill = "white", font = "Arial 20 bold")
            canvas.create_text(app.width/2, (app.height/2)+40, text = "Press R to restart", fill = "white", font = "Arial 18 bold")
        
    else:
    
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
            app.Player.currState = "Death"
        
        if bTopX <= bBtmX:
            app.Boss.currState = "Death"
          

    
    

    


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
    #for testing/debugging:
    canvas.create_text(150, 100, text = "Press P for Player to Attack", fill = "white", font = "Arial/20")
    canvas.create_text(800, 100, text = "Press L for Boss to Attack", fill = "white", font = "Arial/20")
    
    

    

runApp(width=960, height=650)

