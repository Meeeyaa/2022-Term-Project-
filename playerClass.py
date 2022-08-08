#Player Class

from cmu_112_graphics import *
from bossClass import *


class Character:
    def __init__(self, app, cx, cy):
        self.cx = cx
        self.cy = cy
        self.states = ["Idle", "Run", "Jump", "Attack", "Death"]
        
        

    def getImage(self):
        for state in range(len(self.states)):
            if self.states[state] == self.currState:
                if self.facingRight:
                    return self.images[state][1]
                else:
                    return self.images[state][0]


    def draw(self, app, canvas):
        canvas.create_image(self.cx, self.cy, image=ImageTk.PhotoImage(self.getImage()))


    def cx(self):
        return self.cx
    
    def cy(self):
        return self.cy
    
    def getHp(self):
        return self.hp

    def getDamage(self):
        return self.damage

    def healing(self):
        self.hp += 75

    def __repr__ (self):
        return f'Character(name: {self.name}, hp {self.hp}, damage{self.damage}'

    
    def damage(self, other):
        if isinstance(other, Player):
            other.hp -= self.attack
        else:
            other.hp += self.attack
class Player(Character):

    def __init__(self, app, cx, cy):
        super().__init__(app, cx, cy)
        self.hp = app.width*(1/3)
        self.attack = 5
        self.images = app.plyrImages
        self.facingRight = True
        self.currState = self.states[0]



    def move(self, app, event):
        if event.key == "a":
            self.facingRight = False
            self.currState = "Run"
            self.cx -= 10

        elif event.key == "d":
            self.facingRight = True
            self.currState = "Run"
            self.cx += 10

        elif event.key == "w":
            self.currState = "Jump"
            self.cy -= 10

        elif event.key == "p":
            self.currState = "Attack"
            self.damage(app.Boss)
        
        elif event.key == None:
            self.currState = "Idle"