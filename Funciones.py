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
def pmenu(lista,pos,mapa,campodebatalla,personaje,mapamonstruos,monstruos):
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
            accion_no_selecionada=False
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
#aqui en vez de cargar desde xlsx lo suyo seria pasarlo en parametro ,para no estar guardando y cargando todo el rato
def atacar(atacante,defensor,arma):
    damage = 0
    #Carga de los dataframes
    contendientes = pd.read_excel("Campo de batalla.xlsx")
    armas = pd.read_excel("Armas_Hechizos.xlsx")

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
def sacar_lista_de_enemigos(campodebatalla):
    lista=[None]*(campodebatalla.shape[0]-1)
    for i in range(campodebatalla.shape[0]-1):
        lista[i]=campodebatalla.at[i+1,'Nombre']
    return lista
def seleccionar_objetivo(lista_enemigos):
    print("¿A quien deseas atacar")
    accion_no_seleccionada=True
    while accion_no_seleccionada:
        for i in range (len(lista_enemigos)):
            print(" -",i,lista_enemigos[i])
        opcion_elegida = input("\nElige un objetivo: ")
        opcion_elegida=int(float(opcion_elegida))
        if opcion_elegida<len(lista_enemigos)-1 and opcion_elegida>0:
            atacar(lista_enemigos[opcion_elegida])

        
    
#atacar('Rampo Doyle', 'Cocodrilo 1', 'Bola de fuego')
