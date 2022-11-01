
class Triangulo:
    
    def __init__(self, s1,s2,s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

def all_side(Triangulo):
    if Triangulo.s1 == 0 and Triangulo.s2 == 0 and Triangulo.s3 == 0:

        return False

    return True

def one_side(Triangulo):
    if Triangulo.s1 == 0 or Triangulo.s2 == 0 or Triangulo.s3 == 0:
        return False
    return True
def sum_sides(Triangulo):
    sum = (Triangulo.s1 + Triangulo.s2 + Triangulo.s3) / 2

    if sum <=  Triangulo.s1 or sum <= Triangulo.s2 or sum <= Triangulo.s3:

        return False

    return True

def check(Triangulo):
    if  all_side(Triangulo) == True and sum_sides(Triangulo) == True and one_side(Triangulo) == True:
        return True
    return False


