# Day-7-Project
## Hangman Game

A command-line implementation of the classic word-guessing game Hangman, built with Python.

## About

This is a Hangman game where you try to guess a randomly selected word one letter at a time. You have 6 lives—each wrong guess costs you a life. Guess all the letters before running out of lives to win!

Built as a learning project to practice Python loops, conditionals, lists, and modular code organization.

## How to Play

Run the game:
```bash
python main.py
```

**Gameplay:**
1. The game shows you blanks representing each letter in the mystery word
2. Guess one letter at a time
3. Correct guesses reveal the letter's position(s) in the word
4. Wrong guesses cost you one life (you start with 6)
5. Win by guessing all letters before running out of lives
6. Lose if you run out of lives before completing the word

## Example Game
```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

Word to guess: _ _ _ _ _ _
****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: _ a _ _ _ _

****************************6/6 LIVES LEFT****************************
Guess a letter: e
Your guess e is not in the word.
  +---+
  |   |
  O   |
      |
      |
      |
=========
```

## Project Structure
```
hangman/
├── hangman_practice.py              # Main game logic
├── hangman_words.py     # Word list for the game
└── hangman_art.py       # ASCII art (logo and hangman stages)
```

**Modules:**
- `hangman_words.py` - Contains the `word_list` with words to guess
- `hangman_art.py` - Contains `logo` (game title) and `stages` (hangman drawings)

## Game Features

- Random word selection from a word list
- Visual feedback with ASCII art hangman
- Tracks guessed letters to prevent duplicates
- Lives counter showing remaining attempts
- Win/lose conditions with appropriate messages
- Input validation (prevents duplicate guesses)

## Code Structure

**Main game loop:**
1. Display current word state (blanks and correctly guessed letters)
2. Get player's letter guess
3. Check if letter was already guessed (no penalty)
4. Reveal letter if correct, or lose a life if wrong
5. Display updated hangman stage
6. Check win condition (all letters guessed) or lose condition (0 lives)

**Key mechanics:**
- `correct_letters` - Tracks successfully guessed letters
- `guesses` - Tracks all guesses to prevent duplicates
- `lives` - Starts at 6, decrements on wrong guesses
- `display` - Builds the current word state each turn

## What I Learned

- **Modular code organization** - Separating game logic, data, and visuals into different files
- **List manipulation** - Tracking guessed letters and building display strings
- **Loop control** - Using `while` loops with `game_over` flag and `continue` statement
- **String building** - Constructing the display string character by character
- **Conditional logic** - Checking win/lose conditions and duplicate guesses
- **Input validation** - Preventing duplicate guesses with `if guess in guesses`

## Code Highlights

**Duplicate detection:**
```python
if guess in guesses:
    print("You already guessed that, try again.")
    continue  # Skip to next iteration without penalty
```

**Building word display:**
```python
for letter in chosen_word:
    if letter == guess:
        display += letter  # Show guessed letter
    elif letter in correct_letters:
        display += letter  # Show previously guessed letters
    else:
        display += "_"     # Still hidden
```

## Potential Improvements

- Add difficulty levels (easy/medium/hard word lists)
- Track and display all guessed letters
- Add input validation (ensure single letter, no numbers/symbols)
- Implement scoring system (based on lives remaining)
- Add word categories (animals, countries, etc.)
- Create two-player mode (one player enters word, other guesses)

## Dependencies

No external libraries required - uses only Python standard library:
- `random` - For random word selection

## Requirements

- Python 3.x
- `hangman_words.py` file with `word_list` variable
- `hangman_art.py` file with `logo` and `stages` variables

---


