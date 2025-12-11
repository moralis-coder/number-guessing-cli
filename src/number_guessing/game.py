from random import randint, shuffle
from typing import Callable, Optional
from .difficulty_level import DifficultyLevel
from .prompts import InvalidGuessError, prompt_for_guess, select_difficulty_level


class Hint:
    def __init__(self, test: Callable[[int], bool], success_msg: str, failure_msg: str):
        self.test = test
        self.success_msg = success_msg
        self.failure_msg = failure_msg
    
    def __call__(self, number: int):
        if self.test(number):
            print(f'HINT: {self.success_msg}')
        else:
            print(f'HINT: {self.failure_msg}')


PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}


HINTS = [
    Hint(lambda n: n % 2 == 0, "The number is even.", "The number is odd."),
    Hint(lambda n: n % 3 == 0, "The number is divisible by 3.", "The number is not divisible by 3."),
    Hint(lambda n: n % 5 == 0, "The number is divisible by 5.", "The number is not divisible by 5."),
    Hint(lambda n: n in PRIMES, "The number is a prime number.", "The number is not a prime number."),
]



class Game:
    def __init__(self, test_number: Optional[int] = None, prompt: Callable[[], DifficultyLevel] = select_difficulty_level):
        self.test_number = test_number
        self.prompt = prompt

    def print_welcome_message(self):
        print("Welcome to the Number Guessing Game!")
        print("I am thinking of a number between 1 and 100.\n")
    
    def __call__(self):
        self.print_welcome_message()
        selected_level = self.prompt()
        GameSession(
            difficulty_level=selected_level,
            number_to_guess=self.test_number
        )()
    
    def play(self):
        self()


class GameSession:
    def __init__(self, difficulty_level: DifficultyLevel, number_to_guess: Optional[int] = None, prompt: Callable[[str], int] = prompt_for_guess):
        self.difficulty_level = difficulty_level
        self.number_to_guess = randint(1, 100) if number_to_guess is None else number_to_guess
        self.attempts = 0
        self.hints = HINTS[:]
        shuffle(self.hints)
    
    def print_intro(self):
        print(f"Great! You have selected {self.difficulty_level} level.")
        print("Let's start the game!\n")

    def is_guess_correct(self, guess: int) -> bool:
        if guess == self.number_to_guess:
            print(f"Congratulations! You've guessed the correct number in {self.attempts} attempts.")
            return True
    
        if guess < self.number_to_guess:
            print(f"Incorrect! The number is higher than {guess}.")
        
        if guess > self.number_to_guess:
            print(f"Incorrect! The number is lower than {guess}.")

        if len(self.hints) > 0:
            hint = self.hints.pop()
            hint(self.number_to_guess)
        
        return False

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
