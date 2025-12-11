class InvalidOptionError(Exception):
    pass


class InvalidGuessError(Exception):
    pass


def prompt_select_from_options(prompt_message, options):
    print(prompt_message)
    for option_id, option in options.items():
        print(f"{option_id}: {option}")
    
    print()

    try:
        choice = int(input("Enter your choice: "))
        return options[choice]
    except (ValueError, KeyError):    
        raise InvalidOptionError("Invalid option value provided.")


def prompt_for_guess(prompt_message):
    try:
        return int(input(prompt_message))
    except ValueError:
        raise InvalidGuessError("Please enter a valid integer.")
