# Trying to figure out how to animate sprites T_T
# Need to also figure out how to update animation when charater state changes

"""
Dimensions of Spritesheets for Player Character


Idle:
width - 16
height - 146
number - 6


Run:
width - 16
height - 230
number - 8


Jump:
width - 16
height - 366
number - 12


Attack:
width - 48
height - 142
number - 4


Damage:
width -  16
height - 68
number - 3



Death:
width - 32
height - 146
number - 6

"""




from cmu_112_graphics import *
from bossAndPlayerClass import *


def appStarted(app):

    app.timerDelay = 150

    #--idle right
    img1 = app.loadImage("Meow-Knight_idle.png")
    app.idlePlyrImageR = app.scaleImage(img1, 3)
    #--idle left
    app.idlePlyrImageL = app.idlePlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--run right
    img2 = app.loadImage("Meow-Knight_run.png")
    app.runPlyrImageR = app.scaleImage(img2, 3)
    #--run left
    app.runPlyrImageL = app.runPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--jump right
    img3 = app.loadImage("Meow-Knight_jump.png")
    app.jumpPlyrImageR = app.scaleImage(img3, 3)
    #--jump left
    app.jumpPlyrImageL = app.jumpPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--attack right
    img4 = app.loadImage("Meow-Knight_attack_2.png")
    app.attackPlyrImageR = app.scaleImage(img4, 3)
    #--attack left
    app.attackPlyrImageL = app.attackPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)

    #--dead right
    img5 = app.loadImage("Meow-Knight_death.png")
    app.deathPlyrImageR = app.scaleImage(img5, 3)
    #--dead left
    app.deathPlyrImageL = app.deathPlyrImageR.transpose(Image.FLIP_LEFT_RIGHT)


    app.plyrImages = [(app.idlePlyrImageL, app.idlePlyrImageR), (app.runPlyrImageL, app.runPlyrImageR),
                      (app.jumpPlyrImageL, app.jumpPlyrImageR), (app.attackPlyrImageL, app.attackPlyrImageR),
                      (app.deathPlyrImageL, app.deathPlyrImageR)]

    app.plyrImgDims = {"Idle": [16, 146, 6], "Run": [16, 230, 8], "Jump": [12, 366, 6],
                    "Attack3": [48, 142, 4], "Death": [32, 146, 6]}


    app.Player = Player(app, 700, 500)


    # app.spritestrip = app.loadImage("King_Mewrthur_Idle.png")
    # app.sprites = [ ]
    # for i in range(6):
    #     print(app.spritestrip.size)
    #     width, height = app.spritestrip.size
    #     left = 0
    #     upper = (height)*(i/6)
    #     right = left + width
    #     lower = (height)*((i+1)/6)
    #     sprite = app.spritestrip.crop((left, upper, right, lower))
    #     app.sprites.append(sprite)
    # app.spriteCounter = 0
    app.sprites = []
    app.spritecounter = 0
    app.sprites = getAnimation(app, app.Player.getImage())

def getAnimation(app, img):
    spritestrip = img
    num = getImage(app)[2] 
    sprites = [ ]
    for i in range(num):
        print(spritestrip.size)
        width, height = spritestrip.size
        left = 0
        upper = (height)*(i/num)
        right = left + width
        lower = (height)*((i+1)/num)
        sprite = spritestrip.crop((left, upper, right, lower))
        sprites.append(sprite)
    app.spriteCounter = 0
    return sprites



def getImage(app):
    for key in app.plyrImgDims:
        if key == app.Player.currState:
            return app.plyrImgDims[key]


def keyPressed(app, event):
    if event.key == "i":
        app.Player.currState = "Idle"

    if event.key == "r":
        app.Player.currState = "Run"
        


def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
    app.sprites = getAnimation(app, app.Player.getImage())
    


def redrawAll(app, canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(900/2, 900/2, image=ImageTk.PhotoImage(sprite))



runApp(width=900, height=900)