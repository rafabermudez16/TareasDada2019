'''
bUSCADORlINEAL .py
busca un numero en un arreglo de 10.000 numeros enteros aleatorios
'''
import random

def buscador(lista,x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1

lista = [random.randint(0,100) for _ in range(10000)]
print(buscador(lista,7))
print(buscador(lista,99))
print(buscador(lista,101))
print(buscador(lista,44))
