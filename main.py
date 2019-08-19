# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:46:55 2019

@author:  Milla y Mateos
"""
import random
import pandas as pd
import os
import Funciones as f
acciones=['Atacar',"Caminar","Salir"]
#1acciones[0]
#Insertamos dataframe
print("Bienvenido,cargando personajes...")
personajes = pd.read_excel("Personajes.xlsx")
print("Tu personaje  "+personajes.at[0,'Nombre']+" ya se ha cargado\nCargando monstruos...")
monstruos = pd.read_excel("Monstruos.xlsx")
mp=pd.read_excel("Mapa.xlsx")
campodebatalla=pd.read_excel("Campo de batalla.xlsx")
mapademonstruos=pd.read_excel("Mapa de Monstruos.xlsx")

ubi=[0,0]
#while i<4:
#    f.aventura(mp,ubi)
#    f.ubicacion(ubi,mp)
#    i+=1
#continuar=True
#while continuar:
#   continuar=f.pmenu(acciones,ubi,mp)
f.añadirsm(campodebatalla,mapademonstruos,monstruos,0,0)
f.sacarindexmonstruo("Araña gigante",monstruos)
listam=list(mapademonstruos)
p=mapademonstruos.at[0,listam[1]]