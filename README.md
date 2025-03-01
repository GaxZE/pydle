# Pydle

A Python implementation of the popular word guessing game Wordle.

## Description

Pydle is a command-line version of Wordle where players try to guess a 5-letter word in 6 attempts. After each guess, the game provides feedback using colors:

- 🟩 Green: Letter is in the correct position
- 🟨 Yellow: Letter exists in the word but in a different position
- ⬜ Gray: Letter is not in the word

## Features

- Command-line interface for easy gameplay
- Colorful feedback using ANSI color codes
- Dictionary of 5-letter English words
- 6 attempts to guess the word
- Input validation
- Score tracking

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/pydle.git

# Navigate to the directory
cd pydle

# Install dependencies
pip install -r requirements.txt

# Run the game
python play_pydle.py
```
