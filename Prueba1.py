# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:46:55 2019

@author: Raul Milla, Irene Mateos
"""
import random
import pandas as pd


estados = [luchando, andando, durmiendo, hablando]

#Importación de los stats de los personajes y los stats generales de los monstruos
personajes = pd.read_excel("Personajes.xlsx")
monstruos = pd.read_excel("Monstruos.xlsx")


t=personajes.at[0,'Usuario'] #Esto se usa?

#Declaración de las funciones
def competir(personaje1,personaje2,cualidad,cualidad2):
    Tirada = random.randit(0,20)+personajes.at[personaje1,cualidad]
    Tirada2 = random.randit(0,20)+personajes.at[personaje2,cualidad]
    if Tirada<Tirada2 :
        resultado=0
        print("Has fracasado")
    if Tirada>Tirada2 :
        resultado=1("Has triunfado")


def atacar(atacante, defensor, arma)
    contendientes = pd.read_excel("Batalla.xlsx")
    tirada_ataque = random.randit(0,20) + contendientes.at[atacante,bhabilidad] + contendientes.at[atacante,bcompetencia]
    tirada_defensa = random.randit(0,20) + contendientes.at[defensor,cualidad] + contendientes.at[atacante,bcompetencia]
    if tirada_ataque < tirada_defensa:
        resultado = 0
        print("El ataque no ha tenido éxito")
    else:
        print("El ataque es exitoso!")
        #consultando el arma hay que saber qué dados se tiran
