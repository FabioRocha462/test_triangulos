from pickletools import TAKEN_FROM_ARGUMENT1
from src.triangulo import Triangulo, check

def test_with_all_zero():
    
    T = Triangulo(3,4,5)
    assert check(T) == True