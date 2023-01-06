def draw_rectangle(width, height):
    nt = 1*width-2
    i=2
    print("|" + "-" * nt +"|")
    
    while i < height:
        i+=1
        print("|" + " " * nt + "|")
    print("|" + "-" * nt + "|")

draw_rectangle(10, 10)