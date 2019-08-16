# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:46:55 2019

@author: Raul Milla
"""
import random
import pandas as pd
personajes=pd.read_excel("Personajes.xlsx")
personajes
t=personajes.at[0,'Usuario']


def competir(personaje1,personaje2,cualidad,cualidad2):
    Tirada=random.randit(0,20)+personajes.at[personaje1,cualidad]
    Tirada2=random.randit(0,20)+personajes.at[personaje2,cualidad]
    if Tirada<Tirada2 :
        resultado=0
        print("Has fracasado")
    if Tirada>Tirada2 :
        resultado=1("Has triunfado")
