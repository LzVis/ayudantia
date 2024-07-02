""" 
Ejercicio 1: Gestión de Inventario de Componentes
Electrónicos
Desarrolle un programa que ayude a gestionar el inventario de
componentes electrónicos en una fábrica. El programa debe
permitir al usuario realizar las siguientes acciones:1. Agregar un nuevo componente al inventario.
2. Eliminar un componente del inventario.
3. Mostrar el inventario de componentes.
4. Salir del programa.
Requisitos:
•
•
•
Utilizar una lista para almacenar los componentes.
Utilizar ciclos for para recorrer y actualizar la lista.
Implementar las acciones de agregar, eliminar y mostrar
componentes utilizando funciones
"""

def agregar_componente(inventario):
    componente = input("Ingrese el nombre del componente: ")
    inventario.append(componente)
    print("Componente agregado exitosamente.")

def eliminar_componente(inventario):
    componente = input("Ingrese el nombre del componente a eliminar: ")
    if componente in inventario:
        inventario.remove(componente)
        print("Componente eliminado exitosamente.")

def mostrar_inventario(inventario):
    print("Inventario de componentes:")
    for componente in inventario:
        print(componente)

def gestionar_inventario():
    inventario = []
    while True:
        print("Seleccione una opción:")
        print("1. Agregar un nuevo componente al inventario.")
        print("2. Eliminar un componente del inventario.")
        print("3. Mostrar el inventario de componentes.")
        print("4. Salir del programa.")
        opcion = input("Ingrese el número de la opción: ")
        if opcion == "1":
            agregar_componente(inventario)
        elif opcion == "2":
            eliminar_componente(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

gestionar_inventario()