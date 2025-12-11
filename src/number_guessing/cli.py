from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description="Number Guessing Game")
    parser.add_argument(
        '--test-number',
        type=int,
        help="Set a specific number to guess for testing purposes.",
        default=None,
    )

    return parser.parse_args()
