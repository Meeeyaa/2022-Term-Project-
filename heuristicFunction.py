from cmu_112_graphics import *
from bossAndPlayerClass import *

###############################################################


def getWeightOfBoss(bossHp):
    fullBossHp = 960*(2/3)
    s0 = 0    

    if bossHp < 739:
        #low hp
        s0 = 3

    elif 739 <= bossHp <= 838:
        #mid hp
        s0 = 2

    elif 838 < bossHp <= 937:
        #high hp
        s0 = 1
    
    return s0


# def getWeightOfPlayer(playerHp):
#     fullPlayerHp = 960*(1/3)    
#     s1 = 0

#     if playerHp < (1/3)*fullPlayerHp:
#         #low hp
#         s1 = 1

#     elif (1/3)*fullPlayerHp <= playerHp <= (2/3)*fullPlayerHp:
#         #mid hp
#         s1 = 2

#     elif (2/3)*playerHp < playerHp <= fullPlayerHp:
#         #high hp
#         s1 = 3

#     return s1


def h(state):
    #heuristic Function used to score the states of the game

    bossHp = state[0]
    playerHp = state[1]

    bigNum = 10000000000000000000000000000000
    smallNum = -10000000000000000000000000000000
    totalScore = 0

    return getWeightOfBoss(bossHp)

    
# print(f'score: {h([(2/3)*960, 50])}')


