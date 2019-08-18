# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:46:55 2019

@author: Raul Milla, Irene Mateos
"""
import random
import pandas as pd
import os
import Funciones as f
#Insertamos dataframe
print("Bienvenido,cargando personajes...")
personajes = pd.read_excel("Personajes.xlsx")
print("Tu personaje  "+personajes.at[0,'Nombre']+" ya se ha cargado\nCargando monstruos...")
monstruos = pd.read_excel("Monstruos.xlsx")
campodebatalla=pd.read_excel("Campo de batalla.xlsx")
monte = pd.read_excel("Monstruos.xlsx")
f.capitulo1(personajes,campodebatalla,monstruos)