"""
Funcion entrega la multiplicacion de los numeros de una lista

    """
def multiplicacion(arreglo):

    resultado = 1

    for i in range(len(arreglo)):
        resultado = resultado * arreglo[i]

    return resultado

ejemploUno = [1,2,3,4]#24
ejemploDos = [1,2]#2


print(multiplicacion(ejemploUno))
print(multiplicacion(ejemploDos))
