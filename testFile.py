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


def appStarted(app):

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




    app.spritestrip = app.idlePlyrImageR
    app.sprites = [ ]
    for i in range(6):
        sprite = app.spritestrip.crop((16*3, (146*3)*i, 16*3, (146*3)*(i+1)))
        app.sprites.append(sprite)
    app.spriteCounter = 0


def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)


def redrawAll(app, canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(900/2, 900/2, image=ImageTk.PhotoImage(app.spritestrip))



runApp(width=900, height=900)