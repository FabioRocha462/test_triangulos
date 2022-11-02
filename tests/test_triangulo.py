from pickletools import TAKEN_FROM_ARGUMENT1
from src.triangulo import Triangulo, check

def test_with_all_zero():
    
    T = Triangulo(0,0,0)
    assert check(T) == False

def test_with_iquals_values():
    T = Triangulo(5,5,5)
    assert check(T) == True

def test_with_diff_values():
    T = Triangulo(3,4,5)
    assert check(T) == True

def test_with_one_zero():
    T = Triangulo(0,3,4)
    assert check(T) == False

def test_with_value_max_side():
    T = Triangulo(1,5,6)
    assert check(T) == False

def test_with_two_values_equals():
    T = Triangulo(2,2,5)
    assert check(T) == False
    
