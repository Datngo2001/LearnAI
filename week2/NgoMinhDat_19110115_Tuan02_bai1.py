import math


def tinhDelta(a, b, c):
    return (b*b - 4*a*c)


def giaiPT(a, b, c):
    delta = tinhDelta(a, b, c)
    if(delta < 0):
        print("Phuong trinh vo nghiem! \n")
        return
    if(delta == 0):
        print("Phuong trinh co nghiem kep: " + str(-(b/(2*a))))
        return
    if(delta > 0):
        print("Phuong trinh co nghiem 1 la: " +
              str((-b+math.sqrt(delta))/(2*a)))
        print("Phuong trinh co nghiem 2 la: " +
              str((-b-math.sqrt(delta))/(2*a)))
        return


giaiPT(1, 2, -3)
