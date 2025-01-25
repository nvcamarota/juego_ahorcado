## <ins>Instrucciones para jugar a "Adivina la palabra" (El juego del ahorcado)</ins>:

El juego comienza mostrando por pantalla una palabra oculta con guiones que hay que adivinar cuál es. Se le pide al jugador que ingrese una letra por turno hasta lograr adivinar dicha palabra y ganar la partida o quedarse sin vidas y perder el juego.


### <ins>Reglas del juego</ins>:

1. **Inicio**:

    Se elegirá una palabra al azar y se mostrará censurada por pantalla junto a las vidas iniciales y las letras que el jugador vaya ingresando y que no se encuentren en la palabra.

2. **Ingresar la letra**:

    El juego pedirá al jugador que ingrese una letra que puede estar o no en la palabra a adivinar. No son válidos los ingresos de números, símbolos o palabras completas.
    ***A tener en cuenta 🛑: Las letras sin tildes y las letras con tildes cuentan como dos letras diferentes***, dado que hay palabras que las poseen y otras que no. ¡Ten cuidado!
    Una vez ingresada, se mostrará por pantalla en la palabra, en caso de ser correcta, o debajo de ésta si es incorrecta.

3. **Vidas**:

    El jugador inicia con cinco (5) vidas para adivinar la palabra. Cada vez que el jugador ingrese una letra incorrecta, se le restará una vida. 
    
4. **Fin**:

    • ***Victoria***:
    En el caso de que el jugador adivine la palabra con sus vidas restantes, el juego felicitará al jugador y dará por terminada la partida, mostrando cuál era la palabra oculta.

    • ***Derrota***:
    En el caso de que el jugador utilice todas sus vidas y no logre adivinar la palabra por completo el juego finalizará, notificando de la derrota al jugador y mostrará cuál era la palabra que no pudo adivinar.

    En ambos casos, se le preguntará al jugador si desea volver a jugar. Si accede, el juego se reiniciará para dar lugar a una nueva partida. De lo contrario, el juego se despedirá del jugador y se cerrará el programa.


### <ins>Cómo jugar</ins>:

1. **Clonar repositorio**:

    Abrir Git Bash en tu computadora, en la ubicación que desees clonar el repositorio del juego. Una vez allí, ejecutar el comando **`git clone https://github.com/nvcamarota/juego_ahorcado`**.

2. **Abrir juego**:

    En una terminal, ubicar la ruta de la carpeta dónde se encuentra el archivo **`juego_ahorcado.py`** y posicionarse allí. Una vez realizado, ejecutar el comando **`python juego_ahorcado.py`** para iniciar el juego.

3. **Cerrar juego**:

    Para cerrar el juego desde la consola, presionar las teclas "Ctrl + C" para finalizar el programa. En el caso de querer cerrar la consola desde donde se abrió el juego, presionar las teclas "Alt + F4".
