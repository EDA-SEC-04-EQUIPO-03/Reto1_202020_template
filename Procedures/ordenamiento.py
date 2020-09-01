import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from time import process_time 

def hallar_elementos(lst, criteria1, criteria2, column1, column2):
    if lst['size']==0:
        print("La lista esta vacía")
        return 0
    else:
        #Hallar 10 vote_count mayores
        #proceso 1
        t1_start = process_time()
        iterator = it.newIterator(lst)
        ranking={"primero":0,"segundo":0,"tercero":0,"cuarto":0,"quinto":0,"sexto":0,
                "septimo":0,"octavo":0,"noveno":0,"decimo":0}
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria1.lower() in element[column1] and element["original_tittle"] not in ranking:
                # Otra opción es crear un TAD (línea 18), agregar los valores filtrados y utilizar la función ordenar
                for cada_llave in ranking:
                    if ranking[cada_llave] < element[column1]:
                        del ranking[cada_llave]
                        ranking[column1["original_tittle"]]=element[column1]
        #Hallar 5 vote_average menores
        #proceso 2
        iterator2 = it.newIterator(lst)
        avg={"primero":0,"segundo":0,"tercero":0,"cuarto":0,"quinto":0}
        while it.hasNext(iterator2) and element["original_tittle"] not in avg:
            element2 = it.next(iterator2)
            if criteria2.lower() in element2[column2]:
                for cada_llave in avg:
                    if avg[cada_llave] < elemen2[column2]:
                        del avg[cada_llave]
                        avg[column2["original_tittle"]]=element2[column2]
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return (ranking, avg)

def ordenar( lst, entrada):
    #Los elementos vienen ordenados desde la función anterior :( 
    if "+" in entrada: 
        sort.ShellSort(lst, less)
    else:
        sort.ShellSort(lst, greater)
    return lst

