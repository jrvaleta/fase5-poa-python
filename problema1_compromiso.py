# -*- coding: utf-8 -*-
"""
Fase 5 - Evaluacion Final POA
Curso: Fundamentos de Programacion (213022) - UNAD
Estudiante: Jaime Rafael Valeta Mendoza - Grupo 93

Problema 1: Clasificacion del nivel de compromiso de sesiones de clientes.
Cada fila de la matriz tiene el formato:
    [ID del cliente, Duracion de la sesion (segundos), Numero de clics]
"""

# Datos iniciales: matriz con 6 sesiones de clientes
sesiones = [
    ["C001", 250, 12],   # Alto: mas de 180 s y mas de 8 clics
    ["C002", 45, 10],    # Bajo: menos de 60 s
    ["C003", 120, 5],    # Medio: no es Alto ni Bajo
    ["C004", 300, 2],    # Bajo: menos de 3 clics
    ["C005", 200, 8],    # Medio: 8 clics no es mayor que 8
    ["C006", 181, 9],    # Alto: justo por encima de los limites
]


def clasificar_compromiso(duracion, clics):
    """Devuelve 'Alto', 'Medio' o 'Bajo' segun la duracion y los clics."""
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def mostrar_informe(matriz):
    """Recorre la matriz e imprime el ID del cliente y su clasificacion."""
    print("=" * 50)
    print("   INFORME DE COMPROMISO DE SESIONES")
    print("=" * 50)
    print(f"{'ID Cliente':<12}{'Duracion (s)':<14}{'Clics':<8}{'Compromiso'}")
    print("-" * 50)

    for fila in matriz:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]
        nivel = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<12}{duracion:<14}{clics:<8}{nivel}")

    print("=" * 50)


# Programa principal
mostrar_informe(sesiones)
