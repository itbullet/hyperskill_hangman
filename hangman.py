import random


words_list = ['python', 'java', 'kotlin', 'javascript']
wrong_chars = []
secret_word = random.choice(words_list)
print('HANGMAN')


def menu():
    while True:
        choice = input('Type "play" to play the game, "exit" to quit:')
        print()
        if choice == 'play':
            hangman()
        elif choice == 'exit':
            break
        else:
            continue


def hangman():
    guessed_word = ''.join(['-' for _ in secret_word])
    attempts = 8
    while attempts > 0:
        print(guessed_word)
        guess_char = input("Input a letter:")
        if len(guess_char) != 1:
            print("You should input a single letter\n")
        elif not guess_char.islower() or not guess_char.isalpha():
            print("Please enter a lowercase English letter\n")
        elif guess_char in guessed_word or guess_char in wrong_chars:
            print("You've already guessed this letter")
            if attempts > 0:
                print()
        elif guess_char in secret_word:
            guessed_word = ''.join([guess_char if guess_char == secret_word[i] else guessed_word[i] for i in range(len(secret_word))])
            if '-' not in guessed_word:
                break
            print()
        else:
            print("That letter doesn't appear in the word")
            wrong_chars.append(guess_char)
            attempts -= 1
            if attempts > 0:
                print()
    if attempts == 0:
        print('You lost!')
    else:
        print('You guessed the word!')
        print('You survived!')

menu()
