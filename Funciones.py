# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:15:08 2019

@author: Raul Milla
"""
import random
import pandas as pd
import os
import time
monte = pd.read_excel("Monstruos.xlsx")
def pmenu(lista,pos,mapa):
    nl=len(lista)
    accion_no_selecionada=True
    while accion_no_selecionada:
        i=0
        j=0
        for i in range(nl):
            print("-",i," "+lista[i])
        opcion_elegida = input("\nElige un número: ")
        opcion_elegida=int(float(opcion_elegida))
#        for j in range(nl):
        if lista[opcion_elegida] == "Atacar":
            print("Opcion no disponible")
            accion_no_selecionada=False
        elif lista[opcion_elegida] == "Caminar":
            accion_no_selecionada=False
            aventura(pos,mapa)
            ubicacion(pos,mapa)
        elif lista[opcion_elegida] == "Salir":
            accion_no_selecionada=False
            return False                
    return True
def ubicacion(pos,mapa):
    #numero de ubicaciones que hay 
    nm=mapa.shape[0]
    #se busca ubicacion en el dataframe de mapa
    i=0
    t=0
    encontrado=False
    while i<nm and encontrado==False:
        if mapa.at[i,'x']==pos[0] and  mapa.at[i,'y']==pos[1]:
                encontrado=True#se interrumpe la busqueda
                t=i
        i+=1
    #t es la id de la ubicacion
    print(mapa.at[t,'descripcion'])
    
def aventura(pos,mapa):
    dir=caminar()
    x=0
    y=0
    if dir==1:
        print("")
        y=1
    elif dir==2:
        x=1
        y=0
    elif dir==3:
        x=1
    elif dir==4:
        y=-1
        x=1
    elif dir==5:
        y=-1
    elif dir==6:
        y=-1
        x=-1
    elif dir==7:
        x=-1
    elif dir==8:
        x=-1
        y=1
    pos[0]=pos[0]+x
    pos[1]=pos[1]+y
    print("Ahora estas en",pos[0],pos[1])
def capitulo1(pdf,bfdf,mdf,mp):
    print("Te encuentras en la nada")
    
    añadirp(pdf,bfdf)
    t=caminar()
    i=0
    while i < t:
        añadirm(bfdf,0,i+1)
        i+=1
    print("Oh no te has encontrado ",t," arañas\n Is time to fight")
def añadirp(pdf,bfdf):
    cp=list(pdf)
    cbf=list(bfdf)
    numerodejugadores=pdf.shape[0]
    i=0
    while i < numerodejugadores:
        bfdf.at[i,cbf[0]]=pdf.at[i,cp[0]]
        bfdf.at[i,cbf[1]]=pdf.at[i,cp[2]]
        bfdf.at[i,cbf[2]]=pdf.at[i,cp[3]]
        j=3
        while j < 37:
            bfdf.at[i,cbf[j]]=pdf.at[i,cbf[j]]
            j+=1
        i+=1
            
def quitarvidamonstruo(bf,idm,pv):
    cbf=list(bf)
    bf.at[idm,cbf[1]]=bf.at[idm,cbf[1]]-pv
    if bf.at[idm,cbf[1]]<1:
        bf.drop([idm],inplace=True)#se elimina la fila

def añadirm(bfdf,idm,j):#el idm identifica al mons,el nv no se como ponerlo,el numero de moustro que habra en el cam
    cm=list(monte)
    nombre=monte.at[idm,cm[0]]
    cbf=list(bfdf)
    bfdf.at[j,cbf[0]]=nombre
    print("va")
    min=monte.at[0,cm[1]]
    max=monte.at[idm,cm[3]]
    pvm=random.randint(min,max-1)
    bfdf.at[j,cbf[1]]=pvm
    bfdf.at[j,cbf[2]]=pvm

    i=3
    while i <37:
        bfdf.at[j,cbf[i]]=monte.at[idm,cbf[i]]
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
                break
        print("Caminas")
        time.sleep(3)
        direccion=opcion_elegida
        partida_pausa=0
        direccion=int(float(direccion))
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
    contendientes = pd.read_excel("Campo de batalla.xlsx")
    print(contendientes)
    print(atacante)
    print(contendientes.at[atacante,'Wisdom'])
    armas = pd.read_excel("Armas_Hechizos.xlsx")
    if armas.at[arma,Tipo] == "H":
        tirada_ataque = random.randit(0,20) + contendientes.at[atacante,Wisdom] + contendientes.at[atacante,bcompetencia]
    else:
        tirada_ataque = random.randit(0,20) + contendientes.at[atacante,Wisdom] + contendientes.at[atacante,bcompetencia]
    tirada_defensa = random.randit(0,20) + contendientes.at[defensor, "Clase de armadura"] #+ contendientes.at[atacante,bcompetencia]
    print("La tirada de ataque es: " + tirada_ataque)
    print("La tirada de ataque es: " + tirada_ataque)
    if tirada_ataque < tirada_defensa:
        resultado = 0
        print("El ataque no ha tenido éxito")
    else:
        print("El ataque es exitoso!")
        dados_damage = armas.at[arma,Damage]
        print(dados_damage)
        print("Daño:" + dados_damage)
        for i in range(0,dados_damage[0]):
            damage += random.randit(0,dados_damage[2])
        print(damage)

#atacar("Rampo Doyle", "cocodrilo1", "Bola de fuego")
