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
personajes = pd.read_excel("Personajes.xlsx")
monstruos = pd.read_excel("Monstruos.xlsx")
campodebatalla=pd.read_excel("Campo de batalla.xlsx")
print("Bienvenid@",personajes.at[0,'Usuario'],"tu personaje",personajes.at[0,'Nombre'],"esta preparado para la accion")
#estados = [luchando, andando, durmiendo, hablando]
f.menu()
personajes.at[0,'Usuario']="irene"
print(t)
f.anadirm(0,1,0)
#t=personajes.at[0,'Usuario'] #Esto se usa?
campodebatalla.at[0,'Monstruo']="cabra"
#######FUNCIÓN PRINCIPAL##############
#Creacion de menu
menu()
