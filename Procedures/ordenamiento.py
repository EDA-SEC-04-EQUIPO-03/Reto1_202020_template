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
        print("proceso 1")
        t1_start = process_time()
        iterator = it.newIterator(lst)
        ranking=[] 
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria1.lower() in element[column1]:
                # Otra opción es crear un TAD (línea 18), agregar los valores filtrados y utilizar la función ordenar
                ranking.append(element[column1])
        ranking.sort()
        ranking.reverse()
        if len(ranking)>10:
            while len(ranking)!=10:
                del ranking[-1]
        #Hallar 5 vote_average menores
        print("proceso 2")
        iterator2 = it.newIterator(lst)
        avg=[]
        while it.hasNext(iterator2):
            element2 = it.next(iterator2)
            if criteria2.lower() in element2[column2]:
                avg.append(element2[column2])
        avg.sort()
        if len(avg)>5:
            while len(avg)!=5:
                del avg[-1]
        #Hallar pelis con count vote mayores
        iterator3=it.newIterator(lst)
        nombres_count_vote=[]
        while it.hasNext(iterator3):
            element3=it.next[iterator3]
            for valor in ranking:
                if  valor == element3[column1] and element3["original_tittle"] not in nombres_count_vote:
                    nombres_count_vote.append(element3["original_tittle"])
        #Hallar pelis con count vote mayores
        iterator4=it.newIterator(lst)
        nombres_vote_avg=[]
        while it.hasNext(iterator4):
            element4=it.next[iterator4]
            for dato in avg:
                if  dato == element4[column2] and element4["original_tittle"] not in nombres_vote_avg:
                    nombres_vote_avg.append(element4["original_tittle"])
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return ("Las pelis con mayor número de votaciones son: " +nombres_count_vote+ " además las pelis con menor promedio de votoso son: "+ nombres_vote_avg)

def ordenar( lst, entrada):
    #Los elementos vienen ordenados desde la función anterior :( 
    if "+" in entrada: 
        sort.ShellSort(lst, less)
    else:
        sort.ShellSort(lst, greater)
    return lst

