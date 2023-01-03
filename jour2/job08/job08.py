def fonction(type, saison):
    if(type == "fruits" and saison == "hiver"):
        print("orange, mandarine et kiwi")
    elif(type == "fruits" and saison == "ete"):
        print("Poire, fraise, cassis")
    elif(type == "legume" and saison == "hiver"):
        print("carotte, topinambour, endive")
    elif(type == "legume" and saison == "ete"):
        print("artichaut, aubergine,navet")
    else:
        print("Veuillez choisir un type correct de fruit et de saison.")

fonction("fruits", "hiver")
fonction("fruits", "ete")
fonction("legume", "hiver")
fonction("legume", "ete")
fonction("viande", "printemps") # else