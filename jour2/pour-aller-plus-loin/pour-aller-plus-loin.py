def fonction(a, b, c):
    if a <= b+c and b <= a+c and c <= a+b:
        print("Constructible")
    else:
        print("Non constructible")
    if a == b == c:
        print("Triangle équilatéral")
    elif a==b or b==c or c==a:
        print("Triangle isocèle")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Triangle rectangle")
    else:
        print("Triangle quelconque")

fonction(25, 25, 25)
fonction(33, 66, 33)
fonction(5, 12, 13)
fonction(10, 20, 30)
fonction(10, 80, 30)