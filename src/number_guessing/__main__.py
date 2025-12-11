from . import cli
from . import game


def main():
    args = cli.parse_args()
    game_instance = game.Game(test_number=args.test_number)
    game_instance.play()
