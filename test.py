from cmu_112_graphics import *
from characterClass import *


def appStarted(app):

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
    app.plyrImages = [(app.idlePlyrImageL, app.idlePlyrImageR), (app.runPlyrImageL, app.runPlyrImageR),
                      (app.jumpPlyrImageL, app.jumpPlyrImageR), (app.attackPlyrImageL, app.attackPlyrImageR),
                      (app.deathPlyrImageL, app.deathPlyrImageR)]

    app.Player = Player(app, 700, 700)
    app.timerDelay = 150
    img1 = app.loadImage(f"hero{app.Player.currState}.png")
    app.idlePlyrImageR = app.scaleImage(img1, 3)
    spritestrip = app.idlePlyrImageR
    app.sprites = [ ]
    for i in range(4):
        sprite = spritestrip.crop((48*i, 0, 48*(i+1), 48))
        app.sprites.append(sprite)
    app.spriteCounter = 0


def keyPressed(app, event):
    app.Player.move(app, event)
    print(app.Player.currState)

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
    

def redrawAll(app, canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(sprite))

runApp(width=960, height=650)








