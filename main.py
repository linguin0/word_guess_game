import random

words = ["COMPUTER SCIENCE", "PROGRAMMING", "PYTHON", "KEYBOARD", "GITHUB", "TERMINAL", "MINERVA", "MOUSE"]
guesses = 8
completed = False

chosen_word = random.choice(words)
chosen_word_letters = list(chosen_word)

if " " in chosen_word_letters:
    current_word_letters = []
    for Item in chosen_word_letters:
        if Item == " ":
            current_word_letters.append(" ")
        else:
            current_word_letters.append("-")
else:
    current_word = "-" * len(chosen_word)
    current_word_letters = list(current_word)

guessed_letters = []

while not completed:
    print(f"\nYour current word: {"".join(current_word_letters)}")
    choice = input("\nGuess [G] or See Guessed Letters [L] > ")
    if choice.upper() == "G":
        letter_choice = input("Enter a letter > ").capitalize()
        if letter_choice not in chosen_word_letters:
            print("Incorrect guess, please try again!")
            guesses -= 1
        else:
            for Item in chosen_word_letters:
                if Item == letter_choice:
                    letter_position = chosen_word_letters.index(letter_choice)
                    current_word_letters[letter_position] = letter_choice
                    chosen_word_letters[letter_position] = "*"
        
        guessed_letters.append(letter_choice)
    elif choice.upper() == "L":
        print(guessed_letters)

    if chosen_word == "".join(current_word_letters):
        print(f"Well done! The word was {chosen_word}")
        completed = True
    elif guesses == 0:
        print(f"Oh no, you have run out of guesses. The word was {chosen_word}")
        completed = True
    else:
        print(f"You have {guesses} guesses left")