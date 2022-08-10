from cmu_112_graphics import *
from minimaxAlgorithm import *

###############################################################


#__Parent Class__

class Character:
    def __init__(self, app, cx, cy):
        self.cx = cx
        self.cy = cy
        self.dx = 0
        self.dy = 0
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


    def getCx(self):
        return self.cx
    
    def getCy(self):
        return self.cy



    def getHp(self):
        return self.hp

    
    def damage(self, other):
        if isinstance(other, Player):
            other.hp -= self.attack
        else:
            other.hp += self.attack
    
    def getAttack(self):
        return self.attack


    def getImgDims(self):
        for key in self.ImgDims:
            if key == self.currState:
                return self.ImgDims[key]


    def getAnimation(self, app):
        spritestrip = self.getImage()
        num = self.getImgDims()[0] 
        sprites = [ ]
        for i in range(num):
            width, height = spritestrip.size
            left = 0
            upper = (height)*(i/num)
            right = left + width
            lower = (height)*((i+1)/num)
            sprite = spritestrip.crop((left, upper, right, lower))
            sprites.append(sprite)
        if isinstance(self, Boss):
            app.bossSpriteCounter = 0
        else:
            app.plyrSpriteCounter = 0
        return sprites


def distance(x1, y1, x2, y2):
    return ((x2-x1)**2) + ((y2-y1)**2)**5
####################################################################



#__SubClass: Player___

class Player(Character):

    def __init__(self, app, cx, cy):
        super().__init__(app, cx, cy)
        self.hp = app.width*(1/3)
        self.attack = 15
        self.images = app.plyrImages
        self.ImgDims = app.plyrImgDims
        self.facingRight = True
        self.currState = self.states[1]



    def attack_1(self, app):
        #low damage; high healing
        self.currState = "Attack1"
        self.attack = 25//(2**app.level-1)


        if self.getHp() < app.width*(1/3):
            self.hp += 15
        
    

    def attack_2(self, app):
        #middle damage, middle healing
        self.currState = "Attack2"
        self.attack = 30//(2**app.level-1)


        if self.getHp() < app.width*(1/3):
            self.hp += 10



    def attack_3(self, app):
        #high damage; low healing
        self.currState = "Attack3"
        self.attack = 60//(2**app.level-1)

        if self.getHp() < app.width*(1/3):
            self.hp += 5




    def action(self, app, event):

        if event.key == "a":
            app.Player.facingRight = False
            app.Player.currState = "Run"
            app.Player.cx += -10
            app.Player.cy = 0

        elif event.key == "d":
            app.Player.facingRight = True
            app.Player.currState = "Run"
            app.Player.cx += 10
            app.Player.cy = 0

        elif event.key == "w":
            app.Player.currState = "Jump"
            app.Player.cx = 0
            app.Player.cy += -10

        if event.key == "j":
            self.currState = "Attack1"
            self.attack_1(app)
            self.damage(app.Boss)
            app.bossTurn = True


        elif event.key == "k":
            self.currState = "Attack2"
            self.attack_2(app)
            self.damage(app.Boss)
            app.bossTurn = True

        elif event.key == "l":
            self.currState = "Attack3"
            self.attack_3(app)
            self.damage(app.Boss)
            app.bossTurn = True
        else:
            return
            
            
        
        

####################################################################




#__SubClass Boss__

class Boss(Character):

    def __init__(self, app, cx, cy):
        super().__init__(app, cx, cy)
        self.hp = app.width*(2/3)
        self.attack = 20
        self.images = app.bossImages
        self.ImgDims = app.bossImgDims
        self.facingRight = False
        self.currState = self.states[0]


    def attack_1(self, app):
        #low damage; high healing
        self.currState = "Attack1"
        self.attack = 5

        if self.getHp() > app.width*(2/3):
            self.hp -= 15


    
    def attack_2(self, app):
        #middlle damage; middle healing
        self.currState = "Attack2"
        self.attack = 10

        if self.getHp() > app.width*(2/3):
            self.hp -= 10



    def attack_3(self, app):
        #high damage, low healing
        self.currState = "Attack3"
        self.attack = 50

        if self.getHp() > app.width*(2/3):
            self.hp -= 5



    def action(self, app):
        state = [app.Boss.getHp(), app.Player.getHp()]

        if miniMax(state, 2, app.bossTurn) == 1:
            self.attack_1(app)

        elif miniMax(state, 2, app.bossTurn) == 2:
            
            self.attack_2(app)
        else:
            self.attack_3(app)

        self.damage(app.Player)
        app.bossTurn = False
        


