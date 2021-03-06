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

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def lessCount(element1, element2):
    if int(element1["vote_count"]) < int(element2["vote_count"]):
        return True
    return False

def greaterCount(element1, element2):
    if int(element1["vote_count"]) > int(element2["vote_count"]):
        return True 
    return False

def lessAvg(element1, element2):
    if float(element1["vote_average"]) < float(element2["vote_average"]):
        return True
    return False

def greaterAvg(element1, element2):
    if float(element1["vote_average"]) > float(element2["vote_average"]):
        return True 
    return False
