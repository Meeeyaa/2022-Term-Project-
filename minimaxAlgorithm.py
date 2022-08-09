#Minimax Algorithm
#used to decide boss movement

from cmu_112_graphics import *




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


def h(state):

    bossHp = state[0]
    playerHp = state[1]

    bigNum = 10000000000000000000000000000000
    smallNum = -10000000000000000000000000000000
    totalScore = 0

    return getWeightOfBoss(bossHp)



def getEffect(action, possibleActions, bossTurn):
    for action in possibleActions:

        if bossTurn:
            if action == "attack_1":
                hp, attack = -10, -3
            elif action == "attack_2":
                hp, attack = -5, -10
            else:
                hp, attack = -3, -50

        else:
            if action == "attack_1":
                hp, attack = 10, 10
            elif action == "attack_2":
                hp, attack = 5, 25
            else:
                hp, attack = 3, 40

    return (hp, attack)




def miniMax(state, depth, bossTurn):
    #source used for psuedocode: https://www.cs.cmu.edu/~112/notes/student-tp-guides/GameAI.pdf


    #maximizer = boss, minimizer = player

    startingBossHp = state[0]
    startingPlayerHp = state[1] 


    #base case: gameOver or max depth reached, call heuristic function
    if depth == 0 or state[0] >= 960*(39/40) or state[1] <= 960*(1/40):
        score = h(state)
        print(f'score: {score}')
        return h(state)

    #recursive case: move made depending on turn
    else:

        possibleActions = ["attack_1", "attack_2", "attack_3"] #--> will be different attacks the boss can make
        bigNum = 10000000000000000000000000000000
        smallNum = -10000000000000000000000000000000

        #if boss turn, attack with best damage to healing ratio picked

        if bossTurn: #maximizer
            
            bestScore = smallNum


            for action in possibleActions:

                hp, attack = getEffect(action, possibleActions, bossTurn)
                newState = [startingBossHp + hp, startingPlayerHp + attack]

                bossTurn = not bossTurn
                score = miniMax(newState, depth-1, bossTurn)
        
                if score > bestScore:
                    bestScore = score

            return bestScore

        
        #else if player turn, attack with lowest damage picked; minimizer
        else:   
            
            bestScore = bigNum

            for action in possibleActions:
                hp, attack = getEffect(action, possibleActions, bossTurn)
                newState = [startingBossHp + attack, startingPlayerHp + hp] #--> list with boss and player hp attirbute

                bossTurn = not bossTurn
                score = miniMax(newState, depth-1, bossTurn)

                if score < bestScore:
                    bestScore = score
            
            return bestScore


# print(miniMax([800, 100], 2, True))