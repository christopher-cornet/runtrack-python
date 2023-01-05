L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

liste2 = []

for i in L:
    if (i %2 == 0):
        liste2.append(i)
print(sum(liste2))