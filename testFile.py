

"""
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
    image = app.loadImage("Meow-Knight_Idle.png")
    spritestrip = app.scaleImage(image, 3)
    app.sprites = [ ]
    for i in range(6):
        sprite = spritestrip.crop((16*3, (64*3)*i, 16*3, (64*3)*(i+1)))
        app.sprites.append(sprite)
    app.spriteCounter = 0

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def redrawAll(app, canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(500, 500, image=ImageTk.PhotoImage(sprite))

runApp(width=900, height=900)