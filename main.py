# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:46:55 2019

@author:  Milla y Mateos
"""
import random
import pandas as pd
import os
import Funciones as f
campodebatalla.shape[0]
p=f.sacar_lista_de_enemigos(campodebatalla,aramas,'Bola de fuego')
f.seleccionar_objetivo(campodebatalla,aramas,'Bola de fuego')
acciones=['Atacar',"Caminar","Salir"]
f.actualizarlistadeacciones(acciones,campodebatalla)
lista=[]
lista[0]=1
#1acciones[0]
#Insertamos dataframe
ubi=[0,0]
print("Bienvenido,cargando personajes...")
personajes = pd.read_excel("Personajes.xlsx")
print("Tu personaje  "+personajes.at[0,'Nombre']+" ya se ha cargado\nCargando monstruos...")
monstruos = pd.read_excel("Monstruos.xlsx")
mp=pd.read_excel("Mapa.xlsx")
campodebatalla=pd.read_excel("Campo de batalla.xlsx")
mapademonstruos=pd.read_excel("Mapa de Monstruos.xlsx")
aramas=pd.read_excel("Armas_Hechizos.xlsx")
#k=f.sacarindexmonstruo(t,monstruos)
#f.añadirmonstruopornombre(campodebatalla,monstruos,t,0)
#f.ponermonstruosdemapademonstruos(mapademonstruos,2,campodebatalla,monstruos)
#f.encuentro(mp,ubi,campodebatalla,personajes,mapademonstruos,monstruos)
c=True
while c:
    c=f.pmenu(acciones,ubi,mp,campodebatalla,personajes,mapademonstruos,monstruos,aramas,'Bola de fuego')
