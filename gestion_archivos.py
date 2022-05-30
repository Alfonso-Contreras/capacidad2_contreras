# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:50:35 2022

@author: Alfonso
"""

import os
def crear_archivo(nombre, contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()

def eliminar_archivo(nombre):
    os.remove(nombre)
    
def agregar_contenido_archivo(nombre,contenido):
    archivo = open("noticia.txt","at")

    archivo.write("\n" + contenido)
    archivo.close()

def leer_archivo(nombre):
    archivo = open(nombre,"rt", enconding ='utf8')
    contenido = archivo.read()
    return contenido