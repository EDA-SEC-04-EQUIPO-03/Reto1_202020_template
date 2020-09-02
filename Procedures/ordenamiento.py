import config as cf
import sys
import csv
from Sorting import shellsort as sh
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from DataStructures import arraylist as arr
from time import process_time 
from Funciones import Funciones as f

def hallar_elementos(lst, entrada, criterio):
    if lst['size']==0:
        print("La lista esta vacía")
        return 0
    else:
        t1_start= process_time()
        if entrada == "+":
            #orden creciente
            if criterio.lower() in "Count".lower():
                sh.shellSort(lst, f.greaterCount)
            else:
                sh.shellSort(lst, f.greaterAvg)
        elif entrada == "-":
            #orden decreciente
            if criterio.lower() in "Average".lower():
                sh.shellSort(lst, f.lessAvg)
            else:
                sh.shellSort(lst, f.lessCount)
        else:
            print("No ha indicado el criterio de ordenamiento")
            return {}
        dicc={}
        for i in range(1,11):
            elem=arr.getElement(lst, i)
            dicc[elem["original_title"]]=(elem["vote_count"],elem["vote_average"])
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return dicc




