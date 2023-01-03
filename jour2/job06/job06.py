def fonction(nombre):
    if(nombre > 0):
        print("Positif")
    elif(nombre < 0):
        print("Négatif")
    else:
        print("Veuillez choisir un autre chiffre que 0.")

fonction(5)
fonction(15)
fonction(-5)
fonction(-15)
fonction(0) # else