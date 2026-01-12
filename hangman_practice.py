import random


from hangman_words import word_list

lives = 6


from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guesses = []
while not game_over:


    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()



    display = ""

    if guess in guesses:
        print("You already guessed that, try again.")
        continue
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    guesses.append(guess)
    print("Word to guess: " + display)



    if guess not in chosen_word:
        lives -= 1
        print(f"Your guess {guess} is not in the word.")
        if lives == 0:
            game_over = True


            print(f"***********************YOU LOSE**********************\nThe word to solve was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    from hangman_art import stages

    print(stages[lives])
