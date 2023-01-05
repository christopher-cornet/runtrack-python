L = [155, 30, 98, 75, 50, 40, 110, 20, 184]

def liste(list):
    length = 0
    for i in list:
        length += 1
    return length

def liste2(list):
    print(list)
    list_length = liste(list)
    for i in range(list_length):
        for j in range(i + 1, (list_length)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print(list)

liste2(L)