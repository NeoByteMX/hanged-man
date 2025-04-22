import  random #Modulo para seleccionar aleatorios
import os   #Modulo para interactuar con el sistema

#Función para correr el juego
def run():
    # Muñeco de ahorcado que se imprimirá
    images = [r'''
      +---+
      |   |
          |
          |
          |
          |
    =========''', r'''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', r'''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', r'''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', r'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', r'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', r'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    # Base de datos de palabras posibles
    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP"
    ]

    word = random.choice(DB) #Palabra que se escoge de la base de datos aleatoriamente
    spaces = ["_"] * len(word) #Imprime los espacios en lugar de la palabra
    attemps = 0 #número de intentos con base en la cantdiad de muñecos

    while True: #Bucle para comenza el juego
        os.system("cls") #limpria la pantalla
        for character in spaces: #Buque que imprime los caracteres
            print(character, end=" ") #Imprimer los caracteres sin slato de linea, end permite usar espacio en su lugar
        print(images[attemps]) #Dibuja el mueño ahorcado
        letter = input("Elige una letra: \n").upper() #Lee la letra que ingresa el jugador

        found = False #Variable de letra encontrada
        for idx, character in enumerate(word): #revisa el indice y cada caracter en la palabra
            if character == letter: # Valida si el caracter es igual a la letra del jugador
                spaces[idx] = letter #reemplaza un espacio por la letra
                found = True #cambia la variable de busqueda a verdadero

        if not found: # Si no se encuentra suma un intento
            attemps += 1

        if "_" not in spaces: #Valida que no queden espacios al encontrar la palabra
            os.system("cls")
            print("🎉 Felicides ¡Ganaste! 🎉")
            print(f'La palabra era {word.lower()}')
            break

        if attemps == 6: #Valida si el número de intentos máximos es alncanzado
            os.system("cls")
            print("💀 Has Perdido 💀")
            print(f'La palabra era {word.lower()}')
            break

if __name__ == '__main__':
    run()