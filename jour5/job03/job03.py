def draw_rectangle(n):
    ligneVerticale = "|"
    ligneHorizontale = "-"
    plus_haut_bas = "+"
    sharp = "#"
    size = n + 1
    parametre = n
    
    for i in range(size):
        if i == 0 or i == size - 1:
            print(plus_haut_bas + (ligneHorizontale * (size - 2)) + plus_haut_bas)

        else:  
            print(ligneVerticale + (sharp * (parametre - 2))+ " " + (sharp * (n - parametre))+ ligneVerticale)
            parametre = parametre - 1
           
draw_rectangle(10)