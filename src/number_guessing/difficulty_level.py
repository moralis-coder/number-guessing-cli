class DifficultyLevel:
    def __init__(self, level: str, chances: int):
        self.level = level
        self.chances = chances

    def __str__(self):
        return f"{self.level} ({self.chances} chances)"


DIFFICULTY_OPTIONS = {
    1: DifficultyLevel("Easy", 10),
    2: DifficultyLevel("Medium", 5),
    3: DifficultyLevel("Hard", 3)
}
