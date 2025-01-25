import random

# Variables globales (diccionario de palabras que se pueden llegar a elegir al azar para jugar y la cantidad de vidas iniciales)
words = ['Programación', 'Lenguaje', 'Computadora', 'Aprendizaje', 'Módulo', 'Método', 'Desarrollo', 'Código', 'Python', 'JavaScript', 'Programador', 'Algoritmo', 'Hardware', 'Software']
lifes = 5

# Función para elegir una palabra aleatoria de la lista
def random_word():
    return random.choice(words).upper()

# Función para mostrar la palabra censurada con guiones
def censored_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word]).upper()

# Función para definir las reglas del juego con condicionales
def lets_play():
    word = random_word()
    guessed_letters = []
    incorrect_letters = []
    life = lifes

    # Título del juego
    print('\n¡Vamos a jugar al juego "Adivina la palabra"! ¿Crees que puedas ganar? 😎')
    print('(¡ATENCIÓN! Las letras sin tildes y las letras con tildes cuentan como dos letras diferentes, por lo que debes tener esto en cuenta a la hora de pensar cuál puede ser la palabra 👀)\n')
    
    while life > 0:
        # Muestra la palabra censurada, vidas restantes y letras incorrectas
        print(f'La palabra a adivinar es: {censored_word(word, guessed_letters)}\n')
        print(f'Vida(s) restante(s): {life}')
        print(f'Letras incorrectas ingresadas: {', '.join(incorrect_letters)}\n')
        
        # Ingreso de datos
        input_letter = str(input('Ingrese una letra: ')).upper()
        
        # Validar el dato ingresado como alfabético y con longitud 1
        if not input_letter.isalpha() or len(input_letter) != 1:
            print('¡Error! ❌\nEl dato no es válido. Por favor, ingresar una sola letra válida.\n')
            continue
        
        # Verifica que la letra ingresada ya se encuentra registrada (correcta e incorrecta)
        if input_letter in guessed_letters or input_letter in incorrect_letters:
            print('Ya has ingresado esa letra ⚠\nPor favor, ingresa una letra diferente.\n')
            continue
        
        # Si la letra se encuentra en la palabra aleatoria, se agrega en la lista «guessed_letters»
        if input_letter in word:
            guessed_letters.append(input_letter)
            print(f'¡Muy bien! 😁\n"{input_letter}" se encuentra en la palabra a adivinar.\n')
            
        # Si la letra no se encuentra en la palabra aleatoria, se agrega en la lista «incorrect_letters» y se resta una vida
        else:
            incorrect_letters.append(input_letter)
            life -= 1
            print(f'¡Qué mal! 😥\n"{input_letter}" no se encuentra en la palabra a adivinar, por lo que pierdes una vida.\n')
            
        # Si la palabra censurada coincide con la aleatoria, se gana el juego
        if censored_word(word, guessed_letters) == word:
            print(f'¡Has ganado con {life} vida(s) restante(s)! 😎\nLa palabra era "{word.capitalize()}".\n')
            break
    
    # Si se pierden todas las vidas, finaliza el juego
    if life == 0:
        print(f'¡Te has quedado sin vidas, por lo que has perdido el juego! 😭\nLa palabra era "{word.capitalize()}".\n')

# Función para correr el juego y definir opciones posteriores al término del juego (volver a jugar, salir o mensaje de error en caso de ingresar un dato inválido)
def starting_game():
    lets_play()
    
    while True:
        try:
            try_again = str(input('¿Quieres volver a jugar? [S/N]: ')).upper()
            
            if try_again == 'S':
                print('\nVolvamos a hacerlo entonces ✨')
                lets_play()
                continue
            elif try_again not in ['S', 'N']:
                print('¡Error! ❌\nEl dato no es válido. Por favor, ingresar "S" para confirmar ó "N" para salir del juego.\n')
                continue
            else:
                print('¡Gracias por jugar! Te esperamos nuevamente en otra oportunidad. ¡Adiós! 👋\n')
                break    
        # En el caso de que el jugador interrumpa el programa, imprimirá en pantalla el siguiente mensaje
        except KeyboardInterrupt:
            print('\nCerrando el programa...')
            break
        
# Abrir el programa
starting_game()
