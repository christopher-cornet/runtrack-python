def fonction(nb_marches, height_marches):
    z = 7 * (5 * (nb_marches * height_marches) * 2)
    z_in_meter = z / 100
    x = (str(nb_marches))
    y = (str(height_marches))
    z_in_meter = (str(z_in_meter))
    print("Pour " + x + " marches de " + y + " cm, le gardien parcours " + z_in_meter + " m par semaine.")

fonction(20,30)