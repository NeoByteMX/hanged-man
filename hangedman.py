#Version 25.2304.+1011

import random #Module for selecting random items
import os   #Module for interacting with the system
import json #Module for reading json files


#Function to read the json file and return the dictionary of words
def load_words_from_json(filepath="words.json"): #Defines the function, requires the file path as input.
    with open(filepath, 'r') as f: #Opens the file at the indicated path in read mode as f(file)
        words_dictionary = json.load(f) #Creates the words dictionary variable, reads the json file
    return words_dictionary #Returns the dictionary of words
#Function to detect the os system and set clear
def os_system_clear():#Defines the function to set clear
    system = os.name #Detect the os name
    clear = "cls" if system == "nt" else "clear" #Set cls for windows and clear for other os
    return clear #return the clear string according the os system

#Function to run the game
def run():
    words = load_words_from_json("words.json") #Loads the function to create the dictionary and saves it in a variable
    # Hangman figure that will be printed
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

    word = random.choice(words) #Word that is randomly chosen from the database
    spaces = ["_"] * len(word) #Creates a list of underscores representing the word's length
    attemps = 0 #Number of attempts
    user_letters = [] #Create a list of letters used
    repeat_letter = ""
    while True: #Loop to start the game
        clear = os_system_clear()
        os.system(clear) #Clears the screen
        for character in spaces: #Loop that prints the characters
            print(character, end=" ") #Prints the characters without a newline, end allows using a space instead
        print(images[attemps]) #Draws the hangman figure
        print(repeat_letter)

        letter = input("Elige una letra: \n").upper() #Reads the letter entered by the player
        if letter in user_letters:
            repeat_letter = f"Ya has usado la {letter}"
        else:
            repeat_letter = ""
            user_letters.append(letter)
            found = False  # Letter found variable
            for idx, character in enumerate(word):  # Checks the index and each character in the word
                if character == letter:  # Validates if the character is equal to the player's letter
                    spaces[idx] = letter  # Replaces a space with the letter
                    found = True  # Changes the found variable to true

            if not found:  # If not found, adds an attempt
                attemps += 1

            if "_" not in spaces:  # Validates that no spaces remain when the word is found
                os.system(clear)
                print(f'La palabra es {word.lower()}')
                print("🎉 Felicides ¡Ganaste! 🎉")
                break

            if attemps == 6:  # Validates if the maximum number of attempts is reached
                os.system(clear)
                print("💀 Has Perdido 💀")
                print(f'La palabra era {word.lower()}')
                break

if __name__ == '__main__':
    run()
