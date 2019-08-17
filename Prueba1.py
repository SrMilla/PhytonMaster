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
monte = pd.read_excel("Monstruos.xlsx")

#anadirm(monstruos,campodebatalla,0,0,0)
#print("Bienvenid@",personajes.at[0,'Usuario'],"tu personaje",personajes.at[0,'Nombre'],"esta preparado para la accion")
#estados = [luchando, andando, durmiendo, hablando]
#t=personajes.at[0,'Usuario'] #Esto se usa?
#######FUNCIÓN PRINCIPAL##############
#Creacion de menu
#def anadirm(m,bf,idm,nv,j):#m sera el monstrario bf es el campo de batalla el idm identifica al mons,el nv no se como ponerlo,el numero de moustro que habra en el cam
#    nombre=m.at[idm,0]
#    nombre=nombre + " 1"
#    bf.at[j,0]=nombre
#    min=m.at[idm,1]
#    max=m.at[idm,3]
#    pvm=random.randint(min,max-1)
#    bf.at[j,'Puntos de vida']=pvm
#    i=2
#    for i in 37:
#        bf.at[j,i]=m.at[idm,i]
#monstruos = pd.read_excel("Monstruos.xlsx")
#campodebatalla=pd.read_excel("Campo de batalla.xlsx")
#def anadirm(idm,nv,j):#el idm identifica al mons,el nv no se como ponerlo,el numero de moustro que habra en el cam
#    nombre=monstruos.at[idm,0]
#    nombre=nombre + " 1"
#    j=0
#    nombre="Ire"
#    campodebatalla.at[0,"Monstruo"]=nombre
#    campodebatalla
#    min=monstruos.at[idm,1]
#    max=monstruos.at[idm,3]
#    pvm=random.randint(min,max-1)
#    campodebatalla.at[j,'Puntos de vida']=pvm
#    i=2
#    for i in 37:
#        campodebatalla.at[j,i]=monstruos.at[idm,i]
#t=list(personajes)
#p=t[4]
cbf=list(campodebatalla)
#def anadirm(bf,idm,nv,j):#el idm identifica al mons,el nv no se como ponerlo,el numero de moustro que habra en el cam
#    cm=list(monte)
#    nombre=monte.at[idm,cm[0]]
#    cbf=list(bf)
#    bf.at[j,cbf[0]]=nombre
#    print("va")
#    min=monte.at[0,cm[1]]
#    max=monte.at[idm,cm[3]]
#    pvm=random.randint(min,max-1)
#    bf.at[j,cbf[1]]=pvm
#    i=2
#    while i <36:
#        bf.at[j,cbf[i]]=monte.at[idm,cbf[i]]
#        i+=1
f.anadirm(campodebatalla,0,0,3)

#count=3
#while count<32:
#        campodebatalla.at[2,cbf[count+1]]=monstruos.at[0,cbf[count+1]]
#        count+=1