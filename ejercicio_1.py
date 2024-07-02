""" 
Desarrolle un programa que evalúe la calidad de una botella de
plástico basada en dos criterios: capacidad y peso. El programa
debe permitir al usuario ingresar la capacidad y el peso de labotella y luego determinar si la botella pasa la inspección de
calidad según las siguientes reglas

1. La capacidad debe estar entre 500 ml y 2000 ml.
2. El peso debe estar entre 50 g y 100 g.
3. Si la capacidad y el peso están dentro de los rangos
aceptables, la botella pasa la inspección.
4. Si solo la capacidad o solo el peso está fuera de los
rangos aceptables, la botella requiere una revisión
adicional.
5. Si tanto la capacidad como el peso están fuera de los
rangos aceptables, la botella es rechazada.
"""

#Entradas
capacidad = int (input("Ingrese la capacidad de la botella: "))
peso = int (input("Ingrese el peso de la botella: "))
#Proceso
if capacidad>=500:
    if capacidad<=2000:
        if peso>=50:
            if peso<=100:
                print("La botella pasa la inspección")
            else:
                print("La botella requiere una revisión adicional")
        else:
            print("La botella requiere una revisión adicional")
    else:
        print("rechazado")
else:
    print("rechazado")
    
