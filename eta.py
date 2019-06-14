if __name__ == '__main__':
    from random import randrange

    joueurName = "Francis"
    joueurMoney = 1000

    bankMoney = 20000

    maxRand = 50

    def tournerRoulette():
        return randrange(maxRand)

    def isBlack(score):
        return score % 2 == 0;
    def isRed(score):
        return score % 2 != 0;

    def game(joueurMoney, bankMoney):
        joueurInput = int(input("Ton nombre"))
        joueurMise = int(input("Ta mise"))
        if (joueurMoney < joueurMise):
            print(joueurName, " a pas assez")
            return
        joueurMoney -= joueurMise;
        bankMoney += joueurMise
        result = getResult(joueurInput, joueurMise)
        if (result == -1):
            print("vous avez perdu")
        else:
            joueurMoney += result
            bankMoney -= result;
            print("Vous avez gagner ", result)
        print(joueurName, " a ", joueurMoney, " €")
        print("Banque a ", bankMoney, " €")

    def getResult(joueurNombre, joueurMise):
        roulette = tournerRoulette()
        print("Roulette tourne : ", roulette)
        if (roulette == joueurNombre):
            return joueurMise * 3;
        elif ((isBlack(joueurNombre) and isBlack(roulette)) or (isRed(joueurNombre) and isRed(roulette))):
            return joueurMise * 1.5
        else:
            return -1

    while True:
        game(joueurMoney, bankMoney)



