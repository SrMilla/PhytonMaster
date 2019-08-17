# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:46:55 2019

@author: Raul Milla, Irene Mateos
"""
import random
import pandas as pd
import os
#Insertamos dataframe
personajes = pd.read_excel("Personajes.xlsx")
monstruos = pd.read_excel("Monstruos.xlsx")
campodebatalla=pd.read_excel("Campo de batalla.xlsx")
campodebatalla.at[3,'Mounstruo']=3

#estados = [luchando, andando, durmiendo, hablando]




#•t=personajes.at[0,'Usuario'] #Esto se usa?

#Declaración de las funciones
def competir(personaje1,personaje2,cualidad,cualidad2):
    Tirada = random.randit(0,20)+personajes.at[personaje1,cualidad]
    Tirada2 = random.randit(0,20)+personajes.at[personaje2,cualidad]
    if Tirada<Tirada2 :
        resultado=0
        print("Has fracasado")
    if Tirada>Tirada2 :
        resultado=1("Has triunfado")


def atacar(atacante, defensor, arma):
    contendientes = pd.read_excel("Batalla.xlsx")
    tirada_ataque = random.randit(0,20) + contendientes.at[atacante,bhabilidad] + contendientes.at[atacante,bcompetencia]
    tirada_defensa = random.randit(0,20) + contendientes.at[defensor,cualidad] + contendientes.at[atacante,bcompetencia]
    if tirada_ataque < tirada_defensa:
        resultado = 0
        print("El ataque no ha tenido éxito")
    else:
        print("El ataque es exitoso!")
        #consultando el arma hay que saber qué dados se tiran
def menu():
    #os.system('cls')
    partida_pausa = 1
    while partida_pausa == 1:
            print ("Selecciona una opción")
            print ("\t1 - Actualizar ")
            print ("\t2 - Empezar partida")
            print ("\t3 - salir")
            opcion_elegida = 0
            while opcion_elegida == 0:
                opcion = input("Qué deseas hacer? \nElige un número: ")
                if opcion=="1":
                        print("")
                        input("Has seleccionado actualizar")
                        actualizar()
                        opcion_elegida = 1
                elif opcion=="2":
                        print("")
                        input("Empezando partida")
                        opcion_elegida = 1
                        partida_pausa = 0
                elif opcion=="3":
                        print("Saliendo de la partida")
                        opcion_elegida = 1
                        partida_pausa = 0
                else: 
                        print("")
                        input("DING DONG YOU ARE MR WRONG...")

            
def actualizar():
       personajes = pd.read_excel("Personajes.xlsx")
       monstruos = pd.read_excel("Monstruos.xlsx")
       print("La lista de jugadores y monstruos ha sido actualizada")
       print("\n Volviendo al menu principal")


#######FUNCIÓN PRINCIPAL##############
#Creacion de menu
menu()
