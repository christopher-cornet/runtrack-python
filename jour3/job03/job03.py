def test(nombre):
    i = 0
    while i <= nombre:
        print (i)
        i += 1
        if (i == 26 or i == 37 or i == 88):
            i+=1

test(100)