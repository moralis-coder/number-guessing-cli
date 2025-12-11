class InvalidOptionError(Exception):
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
