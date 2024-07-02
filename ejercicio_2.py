"""
Desarrolle un programa que simule el contador de producción
en una fábrica de paneles solares. El programa debe permitir
al usuario ingresar el número de paneles solares producidos
en cada turno hasta que se alcance o supere una meta de
producción diaria.
Requisitos:
1. Solicitar al usuario ingresar la meta de producción
diaria.
2. Utilizar un ciclo while para solicitar al usuario
ingresar el número de paneles solares producidos en cada
turno.mensaje indicando el total acumulado de

3. Acumular el número total de paneles solares producidos.
4. Mostrar un mensaje indicando el total acumulado de
paneles solares producidos después de cada entrada.
5. Finalizar el programa cuando la producción total alcance
o supere la meta.    
"""
# Solicitar al usuario ingresar la meta de producción diaria
meta = int(input("Ingrese la meta de producción diaria: "))

# Inicializar el contador de producción
produccion_total = 0

# Utilizar un ciclo while para solicitar al usuario ingresar el número de paneles solares producidos en cada turno
while produccion_total < meta:
    produccion_turno = int(input("Ingrese el número de paneles solares producidos en este turno: "))
    produccion_total += produccion_turno
    print("Producción acumulada:", produccion_total)

print("Se ha alcanzado o superado la meta de producción diaria.")