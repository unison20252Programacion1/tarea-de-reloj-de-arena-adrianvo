# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return

    # Reloj de arena
    # Parte superior: de ancho máximo al mínimo (punto central)
    for i in range(m):
        espacios = ' ' * i
        repeticiones = (2 * m - 1) - (2 * i)
        print(espacios + s * repeticiones)

    # Parte inferior: triángulo creciente
    # Usamos la misma fórmula matemática pero invertimos el rango del iterador
    # i va desde m-2 bajando hasta 0
    for i in range(m - 2, -1, -1):
        espacios = ' ' * i
        repeticiones = (2 * m - 1) - (2 * i)
        print(espacios + s * repeticiones)
