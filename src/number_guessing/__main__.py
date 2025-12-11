from . import difficulty_level
from . import prompts


def print_welcome_message():
    print("Welcome to the Number Guessing Game!\n")


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
    print_welcome_message()
    selected_level = select_difficulty_level()
    print(f"You have selected: {selected_level}\n")
