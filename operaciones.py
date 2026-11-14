"""Funciones matemáticas de la calculadora segura."""

import math


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


def promedio(numeros):
    if not numeros:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)


def convertir_texto_a_numero(texto):
    """Convierte texto a float. float() lanza ValueError si el texto no es numérico."""
    return float(texto)


def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(numero)
