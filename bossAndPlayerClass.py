from cmu_112_graphics import *
from minimaxAlgorithm import *
import time

###############################################################


#__Parent Class__

class Character:
    def __init__(self, app, cx, cy):
        self.cx = cx
        self.cy = cy
        self.states = ["Idle", "Run", "Attack_1", "Attack_2", "Attack_3", "Death", "Dodge"]
        self.timeStart = 0
        
        

    def getImage(self):
        index = self.states.index(self.currState)
        if self.facingRight:
            return self.images[index][1]
        else:
            return self.images[index][0]


    def draw(self, app, canvas):
        canvas.create_image(self.cx, self.cy, image=ImageTk.PhotoImage(self.getImage()))


    def getCx(self):
        return self.cx
    
    def getCy(self):
        return self.cy

    def getAttack(self):
        return self.attack


    def getHealth(self):
        return self.health
    

    def getHp(self):
        return self.hp

    
    def damage(self, other):
        if isinstance(other, Player):
            if other.currState == "Dodge":
                pass
            else:
                other.hp -= self.attack
                if self.hp < 960*(2/3):
                    self.hp -= self.health
        else:
            other.hp += self.attack
            if self.hp < 960*(1/3):
                self.hp += self.health




def distance(x1, y1, x2, y2):
    return ((x2-x1)**2) + ((y2-y1)**2)**0.5


####################################################################



#__SubClass: Player___

class Player(Character):

    def __init__(self, app, cx, cy):
        super().__init__(app, cx, cy)
        self.rdx = 0
        self.ldx = 0
        self.hp = app.width*(1/3)
        self.attack = 15
        self.health = 0
        self.images = app.plyrImages
        self.facingRight = True
        self.currState = self.states[1]



    def attack_1(self, app):
        #low damage; high healing
        self.currState = "Attack_1"
        self.attack = 50//(2**app.level-1)
        self.health = 20
        
    

    def attack_2(self, app):
        #middle damage, middle healing
        self.currState = "Attack_2"
        self.attack = 60//(2**app.level-1)
        self.health = 10



    def attack_3(self, app):
        #high damage; low healing
        self.currState = "Attack_3"
        self.attack = 120//(2**app.level-1)
        self.health = 5




    def action(self, app, event):

        if event.key == "a":
            app.Player.facingRight = False
            app.Player.currState = "Run"
            self.rdx = 0
            self.ldx -= 10
            app.Player.cx += self.ldx
            

        elif event.key == "d":
            app.Player.facingRight = True
            app.Player.currState = "Run"
            self.ldx = 0
            self.rdx += 10
            app.Player.cx += self.rdx
            

        elif event.key == "w":
            app.Player.currState = "Dodge"


        if event.key == "j":
            self.currState = "Attack_1"
            if distance(app.Boss.cx, app.Boss.cy, app.Player.cx, app.Player.cy) <= 40000:
                self.attack_1(app)
                self.damage(app.Boss)
                app.bossTurn = True



        elif event.key == "k":
            self.currState = "Attack_2"
            if distance(app.Boss.cx, app.Boss.cy, app.Player.cx, app.Player.cy) <= 40000:
                self.attack_2(app)
                self.damage(app.Boss)
                app.bossTurn = True


        elif event.key == "l":
            
            self.currState = "Attack_3"

            if not app.recharging and distance(app.Boss.cx, app.Boss.cy, app.Player.cx, app.Player.cy) <= 40000:
                app.tooFar = False
                self.attack_3(app)
                self.damage(app.Boss)
                self.timeStart = time.time()
                app.bossTurn = True
                app.recharging = True

            if distance(app.Boss.cx, app.Boss.cy, app.Player.cx, app.Player.cy) > 40000:
                app.tooFar = True
                
        else:
            return
            
            
        
        

####################################################################




#__SubClass Boss__

class Boss(Character):

    def __init__(self, app, cx, cy):
        super().__init__(app, cx, cy)
        self.hp = app.width*(2/3)
        self.attack = 20
        self.health = 0
        self.images = app.bossImages
        self.facingRight = False
        self.currState = self.states[0]
        self.timeStart = time.time()


    def attack_1(self, app):
        #low damage; high healing
        self.currState = "Attack_1"
        self.attack = 5
        self.health = 15
        


    
    def attack_2(self, app):
        #middlle damage; middle healing
        self.currState = "Attack_2"
        self.attack = 10
        self.health = 10



    def attack_3(self, app):
        #high damage, low healing
        self.currState = "Attack_3"
        self.attack = 50
        self.health = 5



            

    def action(self, app):
        state = [app.Boss.getHp(), app.Player.getHp()]

        if miniMax(state, 2, app.bossTurn) == 1:
            self.attack_1(app)

        elif miniMax(state, 2, app.bossTurn) == 2:
            
            self.attack_2(app)
        else:
            self.attack_3(app)

        self.damage(app.Player)

   
        


