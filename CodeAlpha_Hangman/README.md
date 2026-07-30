# Hangman Game (Python)

A simple command-line **Hangman Game** built in Python. The program randomly selects a word, and the player has to guess it letter by letter before running out of attempts.

This project was built as part of my internship task at **CodeAlpha**.

---

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Sample Gameplay](#sample-gameplay)
- [Future Improvements](#future-improvements)
- [Acknowledgements](#acknowledgements)

---

## About the Project

Hangman is a classic word-guessing game. In this Python implementation:
- A word is randomly chosen from a predefined list.
- The player guesses one letter at a time.
- Correct guesses reveal the letter's position(s) in the word.
- Incorrect guesses reduce the number of remaining attempts.
- The game ends when the player either guesses the word correctly or runs out of attempts.

---

## Features

- Randomized word selection from a word list
- Tracks guessed letters to avoid repeated guesses
- Displays the word progress with blanks for unguessed letters
- Limits wrong guesses to a maximum of 6 attempts
- Clear win/loss messages at the end of the game

---

## How It Works

1. The program picks a random word from the `words` list.
2. The word is displayed as underscores (`_`), one for each letter.
3. The player enters a single letter as a guess.
4. If the letter is in the word, it is revealed in its correct position(s).
5. If the letter is not in the word, a wrong guess is recorded.
6. The game continues until:
   - The player guesses all letters correctly (**Win**), or
   - The player reaches the maximum number of wrong guesses (**Game Over**)

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mjcodes-77/codealpha_tasks.git
   ```
2. Navigate to the project folder:
   ```bash
   cd codealpha_tasks/CodeAlpha_Hangman
   ```
3. Run the game:
   ```bash
   python hangman.py
   ```

---

## Sample Gameplay

```
Welcome to Hangman Game!
Word:  _ _ _ _ _ _ _
Enter a letter: a
Correct Guess!
Word:  _ a _ _ _ _ _
Enter a letter: z
Wrong Guess!
Remaining guesses:  5
...
Congratulations! You guessed it right!
```

---

## Future Improvements

- Add a graphical interface (using Tkinter or Pygame)
- Add difficulty levels with different word lists
- Add a visual hangman figure that updates with wrong guesses
- Add a scoring system and word categories/hints

---

## Acknowledgements

This project was developed as part of my **Python Programming Internship at CodeAlpha**.

---

If you like this project, feel free to star the repository.
