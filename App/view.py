"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def printMenu():
    print("""
Bienvenido
Por favor antes de continuar carga la información en el catálogo.

1- Cargar información en el catálogo
2- Listar los álbumes en un periodo de tiempo
3- Encontrar los artistas más populares
4- Clasificar las canciones por popularidad
5- Encontrar la canción más popular de un artista
6- Encontrar la discografia de un artista
7- Clasificar las canciones con mayor distribución
8- Pruebas de carga de datos
0- Salir
        """)


def loadData():
    albums, artists, tracks = controller.loadData(catalog)
    return albums, artists, tracks


catalog = newController()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        abm, ats, trc = loadData()
        print(f'Albumes cargados: {str(abm)}')
        print(f'Artistas cargados: {str(ats)}')
        print(f'Canciones cargadas: {str(trc)}')
    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass
    elif int(inputs[0]) == 8:
        size = input("Indique tamaño de la muestra. Ejm: 5%, 10%, etc...")
        ttype = input("Indique el tipo de lista usado: ARRAY_LIST o LINKED_LIST")
        sorter = input("Indique el tidp de algoritmo de ordenamiento: selection, insertion o shell")
        result = controller.sortArtists(catalog, int(size), ttype, sorter)
        delta_time = f"{result[1]:.3f}"
        sorted_list = result[0]
        print("Para", size, "elementos, delta tiempo:", str(delta_time))

    elif int(inputs[0]) == 0:
        sys.exit(0)
    else:
        continue
sys.exit(0)
