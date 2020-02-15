"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Reto 1")
    print("1- Cargar información del reto")
    print("2- Requerimiento 1: Buenas películas de un director")
    print("3- Requerimiento 2: 10 películas con más votos y voto promedio. N películas con menos votos y voto promedio ")
    print("4- Requerimiento 3: N° Películas de un director y su promedio")
    print("5- Requerimiento 4: Nº Películas de un actor, su promedio y el director que más lo ha dirigido.")
    print("7- Requerimiento 2 ... etc")
    print("10- Requerimiento 2 Unificado")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo de peliculas
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las peliculas en la estructura de datos
    """
    controller.loadData(catalog)

def sortByVoteCount(catalog):
    controller.sortByVoteCount(catalog)
def sortByVoteAverage(catalog):
    controller.sortByVoteAverage(catalog)


def printBestMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las mejores peliculas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')
def printWorstMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las peores peliculas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')
def printMostVotedMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las películas más votadas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Votos: ' + movie['vote_count'])
    else:
        print ('No se encontraron peliculas')
def printLeastVotedMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las películas menos votadas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Votos: ' + movie['vote_count'])
    else:
        print ('No se encontraron peliculas')

"""
Menu principal
"""
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    if int(inputs[0])==1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog ()
        loadData (catalog)
        print ('Peliculas cargadas: ' + str(lt.size(catalog['movies'])))
        print ('Directores cargados: ' + str(lt.size(catalog['directors'])))
        print ("Actores cargados: " + str(lt.size(catalog['actors'])))
    elif int(inputs[0])==2:
        dir_name=input("Indique el nombre del director: ")
        movies=controller.getGoodMoviesByDirector(catalog,dir_name)
        print(movies)

        


    elif int(inputs[0])==3:
        sortByVoteAverage(catalog)
        number = input ("Buscando las TOP ?: ")
        movies = controller.getBestMovies (catalog, int(10))
        printBestMovies (movies)
        movies = controller.getWorstMovies (catalog, int(number))
        printWorstMovies (movies)
        sortByVoteCount(catalog)
        movies = controller.getMostVotedMovies (catalog, int(10))
        printMostVotedMovies (movies)
        movies = controller.getLeastVotedMovies (catalog, int(number))
        printLeastVotedMovies (movies)

    elif int(inputs[0])==4:
        dir_name = input("Nombre del director a buscar: ")
        movies = controller.getMoviesByDirector (catalog, dir_name)
        print(movies)


    elif int(inputs[0])==5:
        label = input ("Nombre del Actor a buscar: ")
        pass
    else:
        sys.exit(0)
sys.exit(0)