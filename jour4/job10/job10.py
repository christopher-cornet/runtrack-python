L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

multiply = 1

for i in range(len(L)):
    if 24 < L[i] < 91:
        multiply *= L[i]

print(multiply)