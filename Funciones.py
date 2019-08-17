# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:15:08 2019

@author: Raul Milla
"""
import random
import pandas as pd
import os
import Prueba1
añadirm(0,1,0)
def anadirm(idm,nv,j):#el idm identifica al mons,el nv no se como ponerlo,el numero de moustro que habra en el cam
    nombre=ms.at[idm,0]
    nombre=nombre + " 1"
    Prueba1.campodebatalla.at[j,0]=nombre
    min=Prueba1.monstruos.at[idm,1]
    max=Prueba1.monstruos.at[idm,3]
    pvm=random.randint(min,max-1)
    Prueba1.campodebatalla.at[j,'Puntos de vida']=pvm
    i=2
    for i in 37:
        Prueba1.campodebatalla.at[j,i]=Prueba1.monstruos.at[idm,i]
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
def caminar():
    partida_pausa = 1
    while partida_pausa==1:
        print ("¿Hacia donde quieres ir?")
        print ("\t\t1 -N")
        print ("\t8 -NO\t\t2 -NE")
        print ("7 -O\t\t\t\t3 -E")
        print ("\t6 -SO\t\t4 -SE")
        print ("\t\t5 -S")
        opcion_elegida=0
        while opcion_elegida ==0:
            opcion_elegida = input("\nElige un número: ")
            if opcion_elegida=="1":
                print("")
                input("Has seleccionado Norte")
            elif opcion_elegida=="2":
                print("")
                input("Has seleccionado Noreste")
            elif opcion_elegida=="3":
                print("")
                input("Has seleccionado Este")
            elif opcion_elegida=="4":
                print("")
                input("Has seleccionado Sureste")
            elif opcion_elegida=="5":
                print("")
                input("Has seleccionado Sur")
            elif opcion_elegida=="6":
                print("")
                input("Has seleccionado Suroeste")
            elif opcion_elegida=="7":
                print("")
                input("Has seleccionado Oeste")
            elif opcion_elegida=="8":
                print("")
                input("Has seleccionado Noroeste")
            else:
                print("Te has equivocado")
                opcion_elegida=0
        direccion=opcion_elegida
        partida_pausa=0
        return  direccion
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