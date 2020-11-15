# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:09:45 2020

@author: eloy.chang
"""


class departamentosJudiciales:
    
    def __init__(self):
        self._departamentos = {}
                
    def existe_departamento(self,departamento):
        return departamento in self._departamentos.keys()
    
    def agregar_departamento(self,departamento,dependencia):
        self._departamentos[departamento] = [dependencia]
        return None
    
    def agregar_dependencia(self,departamento,dependencia):
        self._departamentos[departamento].append(dependencia)
        return None
    
    def ordenar(self):
        for departamento in self._departamentos.keys():
            self._departamentos[departamento] = sorted(self._departamentos[departamento])
        return None
    
    def guardar_en_archivo(self,file):
        f = open(file,"w")
        for dep in sorted(self._departamentos):
            f.write(dep + ":{" + ";".join(self._departamentos[dep]) + "}\n")
        f.close()
        return None
    
    def __repr__(self):
        text = ""
        for dep in sorted(self._departamentos):
            text += dep + ":{" + ";".join(self._departamentos[dep]) + "}\n"
        return text
            
            