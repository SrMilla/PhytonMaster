# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:53:02 2019

@author: Raul Milla
"""
import os
menu()
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - primera opción")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t9 - salir")