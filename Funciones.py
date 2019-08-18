# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:15:08 2019

@author: Raul Milla
"""
import random
import pandas as pd
import os
monte = pd.read_excel("Monstruos.xlsx")
def quitarvidamonstruo(bf,idm,pv):
    cbf=list(bf)
    bf.at[idm,cbf[1]]=bf.at[idm,cbf[1]]-pv
    if bf.at[idm,cbf[1]]<1:
        bf.drop([idm],inplace=True)#se elimina la fila
    
def anadirm(bf,idm,j):#el idm identifica al mons,el nv no se como ponerlo,el numero de moustro que habra en el cam
    cm=list(monte)
    nombre=monte.at[idm,cm[0]]
    cbf=list(bf)
    bf.at[j,cbf[0]]=nombre
    print("va")
    min=monte.at[0,cm[1]]
    max=monte.at[idm,cm[3]]
    pvm=random.randint(min,max-1)
    bf.at[j,cbf[1]]=pvm
    i=2
    while i <36:
        bf.at[j,cbf[i]]=monte.at[idm,cbf[i]]
        i+=1
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
def actualizar(personajes,monstruos):
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