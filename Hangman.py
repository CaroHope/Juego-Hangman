'''
Descripcion: Programa Principal en el que se puede jugar al Ahorcado.
             Tiene como Back-Office "ilustracion.py".
             Ejecute este programa aqui

Autor: Evelyn Carolina Jorge
Matricula: 20-0084
Segundo Parcial
'''

#Modulos
from random import choice
import time
from ilustracion import *


#Leer archivo
archivoll = 'palabras.txt'
with open(archivoll) as archivo:
    lines = archivo.readlines()
    lines = list(lines)


#Inicio Juego---------

print("Hola, Vamos a Jugar!")
print(" ")
time.sleep(0.5)
palabraUsuario= ""
intentos = 3

palabra =choice(lines) #Palabra aleatoria
x = 0
dibujo(x) #Grafico


while intentos>0:

    fallas=0
    for letra in palabra:  #for verifica si la letra esta en la que dijo el usuario
        if letra in palabraUsuario:
            print(letra, end="")
        else:
            print("_ ",end="")
            fallas +=1
    
    if fallas == 0:
        print("Excelente!!")
        print("La palabra era ",palabra)
        vida(fallas)
        break

    #Aqui se introduce la letra.
    letranew = input("introduce una letra: ") 
    palabraUsuario += letranew

    if letranew not in palabra:
        intentos-=1
        print("Letra incorrectaa")
        x +=1
        print("Tienes", +intentos, "intentos")
        dibujo(x)

    
    if intentos == 0:
        print(" ")
        print("Sorry, Perdiste :) ")
        print("La palabra era: ",palabra)
        muerte(intentos)



else:
    print("Gracias por jugar")
    time.sleep(0.5)
    print("Bye")
