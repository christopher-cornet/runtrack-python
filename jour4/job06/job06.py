def swap(liste):
    size = len(liste)
    temp = liste[0]
    liste[0] = liste[size - 1]
    liste[size - 1] = temp
     
    return liste

liste = [5, 10, 15, 20, 25]
 
print(swap(liste))