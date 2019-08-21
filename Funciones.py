# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:15:08 2019

@author: Milla y Mateos
"""
import random
import pandas as pd
import os
import time
#monte = pd.read_excel("Monstruos.xlsx")

def init(): #?     
    monstruos = pd.read_excel("Monstruos.xlsx")
    mp=pd.read_excel("Mapa.xlsx")
    campodebatalla=pd.read_excel("Campo de batalla.xlsx")
    mapademonstruos=pd.read_excel("Mapa de Monstruos.xlsx")
    armas=pd.read_excel("Armas_Hechizos.xlsx")

def encuentro(mapa,posicion,campodebatalla,personajes,mapademonstruos,monstruos):
    idubicacion=ubicacion(posicion,mapa)
    print(mapa.at[idubicacion,'descripcion'])
    semillademonstruos=mapa.at[idubicacion,'idsm']
    semillademonstruos=int(float(semillademonstruos))
    if semillademonstruos > 0:
        añadirp(personajes,campodebatalla)
        ponermonstruosdemapademonstruos(mapademonstruos,mapa.at[idubicacion,'idsm'],campodebatalla,monstruos)
        
def sacarindexmonstruo(nombre,monstruo):#devuelve un int,funciona
    i=0
    nombre=str(nombre)
    k=0
    continuar=True
    while i <(monstruo.shape[0]) and continuar:
        if nombre == monstruo.at[i,'Monstruo']:
            k=i
            continuar=False
        i+=1
    return k

def ponermonstruosdemapademonstruos(mapademonstruos,identificacionmapamon,campodebatalla,dataframemonstruos):
    indexmapa=transformaridsenindex(identificacionmapamon,mapademonstruos)
    numeromonstruos=mapademonstruos.shape[1]-1#☺le restamos uno de la semilla
    listademonstruos=list(mapademonstruos)#crea array,hay que quitar el del id
    i=1
    for i in range(numeromonstruos):
        j=1
        p=str(listademonstruos[i+1])
        k=mapademonstruos.at[indexmapa,listademonstruos[i]]
        idm=sacarindexmonstruo(p,dataframemonstruos)
        for j in range(k):
            print("Ha aparecido un",p)
            añadirm(campodebatalla,dataframemonstruos,idm,i+1,j+1)

def transformaridsenindex(n,mapademonstruos):#devuelve int
    continuar=True
    i=0
    lm=mapademonstruos.shape[0]
    while i<lm and continuar:
        if mapademonstruos.at[i,'IDS']==n:
            return i
        i+=1

def añadirsm(campodebatalla,semillademonstruo,monstruos,idsemilla,numero_de_jugadores):
    #sacamos el numero de monstruos que existen,quitamos una columna que es la del ID
    nm=semillademonstruo.shape[1]-1
    i=0
    listademonstruos=list(semillademonstruo)
    numeromonstruos=numero_de_jugadores
    while i < nm:
        idmonstruo=sacarindexmonstruo(listademonstruos[i],monstruos)
        para_añadir=int(float(semillademonstruo.at[idsemilla,listademonstruos[i]]))
        for j in range(para_añadir):
            añadirm(campodebatalla,monstruos,idmonstruo,numeromonstruos,j)
            numeromonstruos+=1

def pmenu(lista,pos,mapa,campodebatalla,personaje,mapamonstruos,monstruos,dataframearmas,arma):
#    mapa,posicion,campodebatalla,personajes,mapademonstruos,monstruos
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
            print("Opcion en desarollo")
            seleccionar_objetivo(campodebatalla,dataframearmas,arma)
            accion_no_selecionada=False
        elif lista[opcion_elegida] == "Estado":
            print("Tu vida es de:",campodebatalla.at[0,'Healt'])
            accion_no_selecionada=False
        elif lista[opcion_elegida] == "Salir y guardar":
            print("Guardando progreso...")
            
            print("Ya esta guardado")
        elif lista[opcion_elegida] == "Caminar":
            accion_no_selecionada=False
            aventura(pos,mapa)
            ubicacion(pos,mapa)
            encuentro(mapa,pos,campodebatalla,personaje,mapamonstruos,monstruos)
            
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
    return t
    #t es la id de la ubicacion
    #print(mapa.at[t,'descripcion'])

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

def añadirmonstruopornombre(bfdf,monte,nombre,j):#el idm identifica al mons,el nv no se como ponerlo,el numero de moustro que habra en el cam
    cm=list(monte)
    idm=sacarindexmonstruo(nombre,monte)
    nombre=monte.at[idm,cm[0]]
    cbf=list(bfdf)
    bfdf.at[j,cbf[0]]=nombre
    min=monte.at[0,cm[1]]
    max=monte.at[idm,cm[3]]
    pvm=random.randint(min,max-1)
    bfdf.at[j,cbf[1]]=pvm
    bfdf.at[j,cbf[2]]=pvm
    i=3
    while i <37:
        bfdf.at[j,cbf[i]]=monte.at[idm,cbf[i]]
        i+=1

def añadirm(bfdf,monte,idm,j,re):#el idm identifica al mons,el nv no se como ponerlo,el numero de moustro que habra en el cam
    cm=list(monte)
    nombre=monte.at[idm,cm[0]]
    cbf=list(bfdf)
    re=str(re)
    nombre=nombre+" "+re
    bfdf.at[j,cbf[0]]=nombre
    min=monte.at[0,cm[1]]
    max=monte.at[idm,cm[3]]
    pvm=random.randint(min,max-1)
    bfdf.at[j,cbf[1]]=pvm
    bfdf.at[j,cbf[2]]=pvm

    i=3
    while i <37:
        bfdf.at[j,cbf[i]]=monte.at[idm,cbf[i]]
        i+=1

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

#aqui en vez de cargar desde xlsx lo suyo seria pasarlo en parametro ,para no estar guardando y cargando todo el rato
def atacar(atacante,defensor,arma,contendientes,armas):
    damage = 0
    #Carga de los dataframes
    #Obtención de los índices de los personajes y el arma
    a = buscar_pers(atacante, contendientes)
    d = buscar_pers(defensor, contendientes)
    w = buscar_pers(arma, armas)    

    #Tiradas de ataque y defensa
    if armas.at[w,'Tipo'] == "H":
        tirada_ataque = random.randint(0,20) + contendientes.at[a,'Wisdom'] #+ contendientes.at[atacante,bcompetencia]
    else:
        tirada_ataque = random.randint(0,20) + contendientes.at[a,'Strength'] #+ contendientes.at[atacante,bcompetencia]
    tirada_defensa = random.randint(0,20) + contendientes.at[d, "Clase de armadura"] #+ contendientes.at[atacante,bcompetencia]
    print("La tirada de ataque es: " + str(tirada_ataque))
    print("La tirada de defensa es: " + str(tirada_defensa))
    
    if tirada_ataque < tirada_defensa:
        resultado = 0
        print("El ataque no ha tenido éxito")
    else:
        print("El ataque es exitoso!")
        dados_damage = armas.at[a,'Damage']
        print("Daño:" + dados_damage)
        print(dados_damage[0])
        print(dados_damage[2])
        for i in range(0,int(dados_damage[0])):
            damage += random.randint(0,int(dados_damage[2]))
        print(atacante + " ha infligido " + str(damage) + " puntos de daño a " + defensor)

    #Actualización de los puntos de vida
    contendientes.at[d, 'Health'] -= damage
    print("Vida de " + defensor + ": " + str(contendientes.at[d, 'Health']))

def buscar_pers(nombre, lista):
        for i in range(0,lista.shape[0]+1):
            if lista.at[i,'Nombre'] == nombre:
                return i

def sacar_lista(dataframe):
    lista=[None]*(dataframe.shape[0])
    for i in range(dataframe.shape[0]):
        lista[i]=dataframe.at[i,'Nombre']
    return lista

def seleccion_arma(armas):
    lista_armas = sacar_lista(armas)
    print("¿Qué deseas utilizar?")
    while True:
        print("Estas son tus armas:")
        for i in range (len(lista_armas)):
            print(" " + str(i+1) + " - " + armas.at[i, "Nombre"] + " (" + armas.at[i, "Tipo"] + ").> " + armas.at[i, "Damage"])
        opcion_elegida = input("\nElige un arma: ")
        opcion_elegida=int(float(opcion_elegida)-1)
        if opcion_elegida<len(lista_armas) and opcion_elegida>=0:
            print("Has elegido utilizar tu " + lista_armas[opcion_elegida])
            return lista_armas[opcion_elegida]
        else:
            print("No tienes ese arma")
    return arma
    

def seleccionar_objetivo(campodebatalla,dataframearmas,arma):
    lista_enemigos=sacar_lista(campodebatalla)
    print("¿A quien deseas atacar?")
    accion_no_seleccionada=True
    while accion_no_seleccionada:
        for i in range (len(lista_enemigos)):
            print(" ",i+1," -",lista_enemigos[i])
        opcion_elegida = input("\nElige un objetivo: ")
        opcion_elegida=int(float(opcion_elegida)-1)
        if opcion_elegida<len(lista_enemigos) and opcion_elegida>=0:
            print("Vas a atacar a ", lista_enemigos[opcion_elegida])
            atacar(campodebatalla.at[0,'Nombre'],lista_enemigos[opcion_elegida],arma,campodebatalla,dataframearmas)
            accion_no_seleccionada=False
        else:
            print("Objetivo no localizado")
        
def actualizarlistadeacciones(lista,campodebatalla):
    del lista[:]
    if campodebatalla.shape[0]>1:#significa que hay enemigos
        lista.append('Atacar')
        lista.append('Huir')
#    if objetos.shape[0]>0:
#        lista.append('Usar objeto')
    if campodebatalla.shape[0]<1:
        lista.append('Caminar')
    lista.append('Estado')
    lista.append('Salir')
    lista.append('Salir y guardar')

def guardar_salir(armas,contendientes, mapa, ubi):
    contendientes.to_excel('Campo de batalla.xlsx',sheet_name='Campo de batalla')
    mapa.to_excel('Mapa.xlsx',sheet_name='Mapa')


campodebatalla=pd.read_excel("Campo de batalla.xlsx")    
armas=pd.read_excel("Armas_Hechizos.xlsx")
a = seleccion_arma(armas)
seleccionar_objetivo(campodebatalla,armas, a)
