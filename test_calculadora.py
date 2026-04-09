# test_calculadora.py
from calculadora import sumar, multiplicar

def test_sumar_positivos():
    """Prueba la suma de dos números positivos."""
    assert sumar(1, 2) == 3

def test_sumar_negativos():
    """Prueba la suma de dos números negativos."""
    assert sumar(-1, -1) == -2

def test_multiplicar_cero():
    """Prueba la multiplicación por cero."""
    assert multiplicar(10, 0) == 0

def test_multiplicar_normal():
    """Prueba una multiplicación normal."""
    assert multiplicar(4, 5) == 20