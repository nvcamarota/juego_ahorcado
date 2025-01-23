"""
1° Proyecto Integrador:
ADIVINA LA PALABRA

El objetivo consiste en desarrollar el juego interactivo "Adivina la palabra".
El funcionamiento esperado es el siguiente:
1. Al ejecutar el programa se mostrará por pantalla una palabra oculta, usando tantos guiones como letras que contiene la palabra a adivinar (la palabra a adivinar será elegida por el programa usando el módulo de Python "random"), la cantidad de vidas con las que cuenta el jugador y las cantidades de letras incorrectas que van ingresando.
2. Cuando el jugador ingresa una letra es necesario que se valide el dato (que sea una letra). Luego de validar la letra ingresada se corrobora si la letra ingresada pertenece a alguna de las letras de la palabra a adivinar.
3. Cada vez que el jugador ingrese una letra que NO pertenece a la palabra a adivinar se restará una vida.
4. El juego finaliza cuando el jugador queda sin vidas, cuando adivina todas las letras de la palabra o cuando selecciona no jugar más. Para todos los casos, se debe mostrar un mensaje indicando si ganó la partida o si perdió.
"""

import random

# Variables globales (diccionario de palabras que se pueden llegar a elegir al azar para jugar y la cantidad de vidas iniciales)
words = ['Programación', 'Lenguaje', 'Computadora', 'Aprendizaje', 'Módulo', 'Método', 'Desarrollo', 'Código', 'Python', 'JavaScript', 'Programador', 'Algoritmo', 'Hardware', 'Software']
lifes = 5

# Función para elegir una palabra aleatoria de la lista
def random_word():
    return random.choices(words)

# Función para mostrar la palabra censurada con guiones
def censored_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Función para transformar palabra aleatoria a capitalize, agregar letras correctas e incorrectas ingresadas en una lista y vidas iniciales
def lets_play():
    word = random_word().capitalize()
    guessed_letters = []
    incorrect_letters = []
    life = lifes
