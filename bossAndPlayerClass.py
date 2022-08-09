#Boss Class

from cmu_112_graphics import *

#__Parent Class__

class Character:
    def __init__(self, app, cx, cy):
        self.cx = cx
        self.cy = cy
        self.states = ["Idle", "Run", "Jump", "Attack1", "Attack2", "Attack3", "Death"]
        
        

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




####################################################################




#__SubClass: Player___

class Player(Character):

    def __init__(self, app, cx, cy):
        super().__init__(app, cx, cy)
        self.hp = app.width*(1/3)
        self.attack = 15
        self.images = app.plyrImages
        self.facingRight = True
        self.currState = self.states[1]


    def attack_1(self):
        self.currState = "Attack1"
        self.attack = 20
    

    def attack_2(self):
        self.currState = "Attack2"
        self.attack = 10


    def attack_3(self):
        self.currState = "Attack3"
        self.attack = 30




    def action(self, app, event):
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


        elif event.key == "h":
            self.currState = "Attack1"
            self.attack_1()
            self.damage(app.Boss)

        elif event.key == "j":
            self.currState = "Attack2"
            self.attack_2()
            self.damage(app.Boss)

        elif event.key == "k":
            self.currState = "Attack3"
            self.attack_3()
            self.damage(app.Boss)
        

        elif event.key == None:
            self.currState = "Idle"


    



####################################################################




#__SubClass Boss__
class Boss(Character):

    def __init__(self, app, cx, cy):
        super().__init__(app, cx, cy)
        self.hp = app.width*(2/3)
        self.attack = 20
        self.images = app.bossImages
        self.facingRight = False
        self.currState = self.states[0]


    def attack_1(self):
        self.currState = "Attack1"
        self.attack = 1
    
    def attack_2(self):
        self.currState = "Attack2"
        self.attack = 20


    def attack_3(self):
        self.currState = "Attack3"
        self.attack = 50



    def action(self, app, event):
        if event.key == "Left":
            self.facingRight = False
            self.scurrState = "Run"
            self.cx -= 10

        elif event.key == "Right":
            self.facingRight = True
            self.currState = "Run"
            self.cx += 10

        elif event.key == "Up":
            self.currState = "Jump"
            self.cy -= 10

        elif event.key == "b":
            self.currState = "Attack"
            self.attack_1()
            self.damage(app.Player)
        
        elif event.key == "n":
            self.currState = "Attack2"
            self.attack_2()
            self.damage(app.Player)

        elif event.key == "m":
            self.currState = "Attack3"
            self.attack_3()
            self.damage(app.Player)
        
        elif event.key == None:
            self.currState = "Idle"


