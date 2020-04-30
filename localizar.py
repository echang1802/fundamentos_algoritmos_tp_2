# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:31:12 2020

@author: eloy.chang
"""

import sys
from dependencia_judicial import dependenciaJudicial

f = open(sys.argv[1],"r")
lat = float(sys.argv[2])
long = float(sys.argv[3])

distanciaMinima = 999999999
dependenciaCercana = None
for linea in f:
    if "Fuero" in linea:
        continue
    valores = linea.split(";")
    index = valores[0]
    fuero = valores[1]
    nombre = valores[2]
    tipo = valores[3]
    direccion = valores[4]
    localidad = valores[5]
    departamento = valores[6]
    telefono = valores[7]
    latitud = float(valores[8].replace(",", "."))
    longitud = float(valores[9].replace(",", "."))
    dependencia = dependenciaJudicial(index, fuero, nombre, tipo, direccion, localidad,\
                                      departamento, telefono, latitud, longitud)
    distancia = dependencia.distancia(lat, long)
    if distancia < distanciaMinima:
        distanciaMinima = distancia
        dependenciaCercana = dependencia

print(dependenciaCercana)
    




