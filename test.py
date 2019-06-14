if __name__ == '__main__':
    from random import randrange

    playerName = "bob"
    playerBlindJoueur = int
    playerBlindRoulette = int
    playerBlind = int
    playerBank = 1000


    def scoreRoulette():
        numberRandom=randrange(50)+1
        return numberRandom

    def getColorNumber( number):
        if(number %2 == 0):
            color = "black"
        else:
            color="red"
        return color

    def displayLoose():
        return print("perdu")

    def displayWin():
        return print("gagner")

    def getGain():
        return "la banque est de: "

    def getResult(playerBlind, numberPlayer):
        roulette = scoreRoulette()
        print('la roulette a fait: ', roulette)
        if(roulette == numberPlayer):
            return playerBlind*3
        elif(getColorNumber(roulette) == getColorNumber(numberPlayer)):
            return playerBlind*0.5
        else:
           return -1

    def maxNumber(numberPlayer):
        print('le nomvre doit étre <50')
        numberPlayer = int(input('choisi un nombre:'))
        return numberPlayer

    def startGame(playerBank):
        playerBlind = int(input("choisir une mise: "))
        if (playerBlind > playerBank):
            print("le joueur n'a pas assez")
            return playerBank
        else:
            numberPlayer = int(input('choisi un nombre:'))
            while numberPlayer > 50:
                numberPlayer = maxNumber(numberPlayer)

            result = int(getResult(playerBlind, numberPlayer))
            if(result == -1):
                playerBank -= playerBlind
                displayLoose()
                print(playerBlind)
                print(getGain(),playerBank)
                return playerBank
            else:
                playerBank += result
                displayWin()
                print(result)
                print(getGain(), playerBank)
                return playerBank
        return playerBank

    while playerBank > 0:
        playerBank=startGame(playerBank)
        if(playerBank<=0):
            print("perdu tu n'a plus d'oseille")
            break












