from random import randint
from typing import Callable, Optional
from .difficulty_level import DifficultyLevel
from .prompts import InvalidGuessError, prompt_for_guess


class GameSession:
    def __init__(self, difficulty_level: DifficultyLevel, number_to_guess: Optional[int] = None, prompt: Callable[[str], int] = prompt_for_guess):
        self.difficulty_level = difficulty_level
        self.number_to_guess = randint(1, 100) if number_to_guess is None else number_to_guess
        self.attempts = 0
    
    def print_intro(self):
        print(f"Great! You have selected {self.difficulty_level} level.")
        print("Let's start the game!\n")

    def is_guess_correct(self, guess: int) -> bool:
        if guess < self.number_to_guess:
            print(f"Incorrect! The number is higher than {guess}.")
            return False
        
        if guess > self.number_to_guess:
            print(f"Incorrect! The number is lower than {guess}.")
            return False
        
        print(f"Congratulations! You've guessed the correct number in {self.attempts} attempts.")
        return True

    def __call__(self):
        self.print_intro()
        while self.attempts < self.difficulty_level.chances:
            try:
                self.attempts += 1
                guess = prompt_for_guess("Enter your guess: ")
                if self.is_guess_correct(guess):
                    return
                print()
            except InvalidGuessError as e:
                print(e)

        print(f"Game Over! You've used all your chances. The correct number was {self.number_to_guess}.")
