#Minimax Algorithm
#used to decide boss movement

from cmu_112_graphics import *



def miniMax(state, depth, bossTurn):
    #source used for psuedocode: https://www.cs.cmu.edu/~112/notes/student-tp-guides/GameAI.pdf


    #maximizer = boss 
    #minimizer = player


    #base case: gameOver or max depth reached, call heuristic function
    if app.gameOver or depth == 0:
        return score

    #recursive case: move made depending on turn
    else:

        possibleActions = [] #--> will be different attacks the boss can make]
        #if boss turn, move with highest damage picked
        if bossTurn: #maximizer
            smallNum = -10000000000000000000000000000000
            bestScore = smallNum
            bestAction = app.Boss.damage(app.Player)

            for action in possibleActions:
                newState = [app.Boss.getHp(), app.Player.getHp()] #--> list with boss and player hp attirbute
                state = newState
                bossTurn = not bossTurn
                score = miniMax(state, depth-1, bossTurn)
                if score > bestScore:
                    bestScore = score
                    bestMove = move
            return (bestScore, bestMove)

        
        #else if player turn, move with lowest damage picked; minimizer
        else:   
            bigNum = 10000000000000000000000000000000
            bestScore = bigNum
            bestMove = app.Player.damage(app.Boss)

            for action in possibleActions:
                newState = [app.Boss.getHp(), app.Player.getHp()] #--> list with boss and player hp attirbute
                state = newState
                bossTurn = not bossTurn
                score = miniMax(state, depth-1, bossTurn)
                if score < bestScore:
                    bestScore = score
                    bestMove = move
            return (bestScore, bestMove)