#Version 25.2304.+850

import  random #Modulo para seleccionar aleatorios
import os   #Modulo para interactuar con el sistema
import json #Modulo para leer archivos json

#función para leer el archivo json y regresar el diccionario de palabras
def load_words_from_json(filepath="words.json"): #Define la función, requiere la ruta del archivo como input.
    with open(filepath, 'r') as f:#abre el archivo en la ruta indicada como lectura como f(file)
        words_dictionary = json.load(f) #Crea la variable diccionario de palabras, lee el archivo json
    return words_dictionary #Retorna el diccionario de palabras

#Función para correr el juego
def run():
    words = load_words_from_json("words.json") #Carga la función para crear el diccionario y la guarda en una variable
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

    word = random.choice(words) #Palabra que se escoge de la base de datos aleatoriamente
    spaces = ["_"] * len(word) #Imprime los espacios en lugar de la palabra
    attemps = 0 #número de intentos con base en la cantdiad de muñecos
    user_letters = []


    while True: #Bucle para comenza el juego
        os.system("cls") #limpria la pantalla
        for character in spaces: #Buque que imprime los caracteres
            print(character, end=" ") #Imprimer los caracteres sin slato de linea, end permite usar espacio en su lugar
        print(images[attemps]) #Dibuja el mueño ahorcado
        letter = input("Elige una letra: \n").upper() #Lee la letra que ingresa el jugador

        if letter in user_letters:
            print(f"Ya has usado la {letter}")
        else:
            user_letters.append(letter)

        found = False #Variable de letra encontrada
        for idx, character in enumerate(word): #revisa el indice y cada caracter en la palabra
            if character == letter: # Valida si el caracter es igual a la letra del jugador
                spaces[idx] = letter #reemplaza un espacio por la letra
                found = True #cambia la variable de busqueda a verdadero

        if not found: # Si no se encuentra suma un intento
            attemps += 1

        if "_" not in spaces: #Valida que no queden espacios al encontrar la palabra
            os.system("cls")
            print(f'La palabra es {word.lower()}')
            print("🎉 Felicides ¡Ganaste! 🎉")
            break

        if attemps == 6: #Valida si el número de intentos máximos es alncanzado
            os.system("cls")
            print("💀 Has Perdido 💀")
            print(f'La palabra era {word.lower()}')
            break

if __name__ == '__main__':
    run()
