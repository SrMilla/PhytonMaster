# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:46:55 2019

@author:  Milla y Mateos
"""
import random
import pandas as pd
import os
import Funciones as f
#lista=[]
#lista[0]=1
#1acciones[0]
#Insertamos dataframe

ubi=[0,0]
monstruos = pd.read_excel("Monstruos.xlsx")
mp=pd.read_excel("Mapa.xlsx")
campodebatalla=pd.read_excel("Campo de batalla.xlsx")
mapademonstruos=pd.read_excel("Mapa de Monstruos.xlsx")
armas=pd.read_excel("Armas_Hechizos.xlsx")
acciones=['Atacar',"Caminar","Salir"]
print("Bienvenido,cargando personajes...")
personajes = pd.read_excel("Personajes.xlsx")
print("Tu personaje  "+personajes.at[0,'Nombre']+" ya se ha cargado\nCargando monstruos...")
f.pmenu(acciones,ubi,mp,campodebatalla,personajes,mapademonstruos,monstruos,armas,'Bola de fuego')
