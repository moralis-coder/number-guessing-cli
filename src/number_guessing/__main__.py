from . import cli
from . import difficulty_level
from . import game
from . import prompts


def print_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.\n")


def select_difficulty_level():
    selected_level = None
    while not selected_level:
        try:
            selected_level = prompts.prompt_select_from_options(
                'Please select a difficulty level:',
                difficulty_level.DIFFICULTY_OPTIONS
            )
        except prompts.InvalidOptionError as e:
            print(e)
            print("Please try again.\n")
    return selected_level


def main():
    args = cli.parse_args()

    print_welcome_message()
    selected_level = select_difficulty_level()
    
    game.GameSession(
        difficulty_level=selected_level,
        number_to_guess=args.test_number
    )()
