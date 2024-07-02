""" 
Ejercicio 2: Tablero de Control de Minería
Desarrolle un programa que simule un tablero de control de
calidad en una mina. El tablero es una matriz de 4x4 que
representa las secciones de extracción. Cada celda de la
matriz puede contener un número del 0 al 9, indicando la
cantidad de impurezas detectadas en esa sección. El programa
debe permitir al usuario realizar las siguientes acciones:
1. Ingresar los datos de impurezas en cada sección.
2. Mostrar el tablero de control de calidad.
3. Calcular y mostrar el total de impurezas detectadas.
Requisitos:
•
•
•
Utilizar una matriz para representar el tablero de
control de calidad.
Utilizar ciclos for para recorrer y actualizar la
matriz.
Implementar las acciones de ingresar datos, mostrar el
tablero y calcular el total utilizando funciones.
"""

def ingresar_datos(tablero):
    for i in range(4):
        for j in range(4):
            impurezas = int(input(f"Ingrese la cantidad de impurezas en la sección [{i}][{j}]: "))
            tablero[i][j] = impurezas

def mostrar_tablero(tablero):
    for i in range(4):
        for j in range(4):
            print(tablero[i][j], end=" ")
        print()

def calcular_total(tablero):
    total = 0
    for i in range(4):
        for j in range(4):
            total += tablero[i][j]
    return total

#tablero = [[0] * 4 for _ in range(4)]

tablero = []
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(0)
    tablero.append(fila)
print(tablero)

ingresar_datos(tablero)
mostrar_tablero(tablero)
total_impurezas = calcular_total(tablero)
print(f"Total de impurezas detectadas: {total_impurezas}")