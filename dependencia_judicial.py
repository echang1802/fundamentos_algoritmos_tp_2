# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:29:56 2020

@author: eloy.chang
"""

from utils import sqrt

class dependenciaJudicial:
    
    def __init__(self,index,fuero,nombre,tipo,direccion,localidad,departamento,telefono,latitud,longitud):
        self._index = int(index)
        self._fuero = fuero
        self._nombre = nombre
        self._tipo = tipo
        self._direccion = direccion
        self._localidad = localidad
        self._departamento = departamento
        self._telefono = telefono
        self._latitud = float(latitud)
        self._longitud = float(longitud)
        
    def fuero(self):
        return self._fuero
    
    def nombre(self):
        return self._nombre
    
    def tipo_de_ente(self):
        return self._tipo
    
    def direccion(self):
        return self._direccion
    
    def locatidad(self):
        return self._localidad
    
    def departamento_judicial(self):
        return self._departamento
    
    def telefono(self):
        return self._telefono
    
    def distancia(self,lat,long):
        diffLat = lat - self._latitud
        diffLong = long - self._longitud
        return sqrt((diffLat*diffLat) + (diffLong*diffLong))
    
    def __lt__(self,other):
        if self._departamento != other._departamento:
            return self._departamento < other._departamento
        if self._fuero != other._fuero:
            return self._fuero < other._fuero
        return self._nombre < other._nombre
    
    def __eq__(self,other):
        return self._departamento == other._departamento & \
            self._fuero == other._fuero & \
                self._nombre == other._nombre
                
    def __repr__(self):
        return "{" + self._fuero + ";" + self._nombre + ";" + \
            self._direccion + ";" + self._localidad + "}"
    
