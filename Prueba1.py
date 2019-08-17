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
#estados = [luchando, andando, durmiendo, hablando]
f.menu()



#•t=personajes.at[0,'Usuario'] #Esto se usa?

#######FUNCIÓN PRINCIPAL##############
#Creacion de menu
menu()
