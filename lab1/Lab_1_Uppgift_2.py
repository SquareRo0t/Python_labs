def recept(antal):
    print("Ingredienser")
    print("")
    print("För Form:")
    print("ca " + str(10 / 4 * antal) + " g smör")
    print("ca " + str(0.75 / 4 * antal) + " dl ströbröd")
    print("")
    print("Sockerkaka:")
    print(str(round(3 / 4) * antal) + " st ägg")
    print(str(3 / 4 * antal) + " dl strösocker")
    print(str(2 / 4 * antal) + " tsk vaniljsocker")
    print(str(2 / 4 * antal) + " tsk bakpulver")
    print(str(3 / 4 * antal) + " dl vetemjöl")
    print(str(75 / 4 * antal) + " g smör")
    print(str(1 / 4 * antal) + " dl vatten")


#
def tidblanda(antal):
    blanda = 10 + antal
    return blanda


#
def tidgradda(antal):
    gradda = 30 + antal * 3
    return gradda


#
def sockerkaka(antal):
    recept(antal)
    print(str(tidblanda(antal) + tidgradda(antal)) + (" minuter"))
    print("")


#
sockerkaka(4)
sockerkaka(7)
