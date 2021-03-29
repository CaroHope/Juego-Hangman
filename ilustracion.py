'''
Descripcion: Programa Back-Office del juego de Hangman.
             Este archivo contiene las ilustraciones y las
             funciones para poder llamar a las mismas dependiendo
             de la situación.
             *Ejecute el programa "Hangman.py".

Autor: Evelyn Carolina Jorge
Matricula: 20-0084
Segundo Parcial
'''

# Dibujos:.

fa0 = '''
        -------#
        |      |
               |
               |
               |
    ___________|
'''

fa1 = '''
        -------#
        |      |
      (╥﹏╥)   |
               |
               |
    ___________|
'''

fa2 = '''
        -------#
        |      |
      (╥﹏╥)   |
       /|\     |
               |
    ___________|
'''

fa3 = '''
        -------#
        |      |
      (╥﹏╥)   |
       /|\     |
        /\     |
    ___________|
'''

faYes = '''
   (つ✧ω✧)つ .'*•.brillo

'''
faMuerte = '''
(ノ｀Д´)ノ彡┻━┻

 Adivina mejor!
 
'''


#.. Funciones del Ahorcado ..

import time

#Funcion de juego
def dibujo(x):
    if x == 0:
        time.sleep(1)
        print(fa0)
    elif x ==1:
        time.sleep(1)
        print(fa1)
    elif x ==2:
        time.sleep(1)
        print(fa2)
    else:
        time.sleep(1)
        print(fa3)


#Funcion de Tristeza
def muerte(intentos):
    if intentos == 0:
        print(faMuerte)

#Funcion de Alegria
def vida(fallas):
    if fallas == 0:
        print(faYes)
