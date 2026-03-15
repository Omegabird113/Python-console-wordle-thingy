import random

class Game:
    def __init__(self, words_list: list[str], attempts: int):
        if not Game.__validate_words_list(words_list):
            raise ValueError("Invalid words list")

        if not Game.__validate_attempts(attempts):
            raise ValueError("Invalid mumber or value of attempts")

        self.__words = words_list
        self.__attempts = attempts

    @classmethod
    def __validate_words_list(cls, words: list[str]) -> bool:
        if not isinstance(words, list):
            return False
        if len(words) < 1:
            return False
        return all(isinstance(i, str) for i in words)

    @classmethod
    def __validate_attempts(cls, attempts: int) -> bool:
        if not isinstance(attempts, int):
            return False
        if attempts < 1:
            return False
        return True

    @classmethod
    def pick_word(cls, words: list[str]) -> str:
        return random.choice(words)

    @property
    def words_list(self) -> list[str]:
        return self.__words

    @words_list.setter
    def words_list(self, words: list[str]) -> None:
        if not Game.__validate_words_list(words):
            raise ValueError("Invalid words list")

        self.__words = words

    @property
    def attempts(self) -> int:
        return self.__attempts

    @attempts.setter
    def attempts(self, attempts: int) -> None:
        if not Game.__validate_attempts(attempts):
            raise ValueError("Invalid number or value of attempts")

        self.__attempts = attempts

    @classmethod
    def color_text(cls, text: str, color: str) -> str:
        color: str = color.lower().strip()
        colors: dict[str, str] = {
            "green": "\033[92m{}\033[00m,",
            "yellow": "\033[93m{}\033[00m,",
            "red": "\033[91m{}\033[00m,",
            "light purple": "\033[94m{}\033[00m,",
            "purple": "\033[95m{}\033[00m,",
            "cyan": "\033[96m{}\033[00m",
            "light gray": "\033[97m{}\033[00m",
            "black": "\033[90m{}\033[00m",
        }
        if color in colors:
            color_value: str = colors[color]
            return color_value.format(text)
        else:
            raise ValueError("Invalid color code")

    @classmethod
    def __get_correctiveness_string(cls, char_list: list[str], correctness_list: list[str]) -> str:
        colored_string: str = ""
        for ind, char in enumerate(char_list):
            if correctness_list[ind] == "here":
                colored_string += Game.color_text(char, "green")
            elif correctness_list[ind] == "other":
                colored_string += Game.color_text(char, "yellow")
            elif correctness_list[ind] == "not":
                colored_string += Game.color_text(char, "red")
            else:
                colored_string += char
        return colored_string

    @classmethod
    def __get_result_string(cls, entered_word: str, correct_word: str) -> str:
        split_entered_word: list[str] = list(entered_word)
        split_correct_word: list[str] = list(correct_word)

        correctiveness_list: list[str] = []
        uses: dict[str, int] = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}

        for ind, char in enumerate(split_entered_word):
            if char == split_correct_word[ind]:
                correctiveness_list.append("here")
                uses[char] += 1
            else:
                correctiveness_list.append("not")

        for ind, char in enumerate(split_entered_word):
            if char == split_correct_word[ind]:
                continue
            elif char in correct_word and correct_word.count(char) > uses[char]:
              uses[char] += 1
              correctiveness_list[ind] = "other"

        return Game.__get_correctiveness_string(split_entered_word, correctiveness_list)

    def __ask_to_input_word(self, letters: int) -> str:
        valid: bool = False
        word: str = ""
        while not valid:
            word = input("Enter a word to guess:\n")
            if len(word) != letters:
                print(f"{word} is not {letters} letters. Please try again.")
            elif word not in self.__words:
                print(f"{word} isn't in the word list, but it'll still count...")
                valid = True
            else:
                valid: bool = True
        return word

    def play(self) -> None:
        correct_word: str = Game.pick_word(self.__words)
        letter_count: int = len(correct_word)
        print(f"The correct word is {letter_count} letters.")
        running: bool = True
        attempts: int = 0
        while running:
            entered_word: str = self.__ask_to_input_word(letter_count).strip().lower()
            return_str: str = Game.__get_result_string(entered_word, correct_word)
            attempts += 1
            print(return_str)
            if entered_word == correct_word:
                print()
                print(Game.color_text("You win!", "green"))
                running = False
            elif attempts >= self.__attempts:
                print()
                print(Game.color_text("You lost!", "red"))
                print(f"The correct word was {Game.color_text(correct_word, 'yellow')}")
                running = False
