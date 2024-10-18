import pytest 
from suma import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(3, 7) == 10
    assert sumar(-1, 5) == 4
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(10, 5) == 5
    assert restar(3, 7) == -4
    assert restar(0, 0) == 0

def test_multiplicar():
    assert multiplicar(2, 5) == 10
    assert multiplicar(0, 5) == 0
    assert multiplicar(-1, 4) == -4

def test_dividir():
    assert dividir(8, 2) == 4
    assert dividir(9, 3) == 3

    with pytest.raises(ValueError):
        dividir(10, 0)