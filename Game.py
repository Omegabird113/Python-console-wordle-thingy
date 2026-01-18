import random

class Game:
    def __init__(self, words_list: list[str], attempts: int):
        if not Game.__validate_words_list(words_list):
            raise ValueError("Invalid words list")

        if not Game.__validate_attempts(attempts):
            raise ValueError("Invalid attempts value")

        self.__words = words_list
        self.__attempts = attempts

    @classmethod
    def __validate_words_list(cls, words: list[str]) -> bool:
        if type(words) != list:
            return False
        is_all_strs: bool = True
        for i in words:
            if type(i) != str:
                is_all_strs = False
        return is_all_strs

    @classmethod
    def __validate_attempts(cls, attempts: int) -> bool:
        if not type(attempts): return False
        if attempts < 1: return False
        return True

    @classmethod
    def pick_word(cls, words: list[str]) -> str:
        return random.choice(words)

    @property
    def words_list(self) -> list[str]:
        return self.__words

    @words_list.setter
    def words_list(self, words: list[str]):
        if not Game.__validate_words_list(words):
            raise ValueError("Invalid words list")

        self.__words = words

    @property
    def attempts(self) -> int:
        return self.__attempts

    @attempts.setter
    def attempts(self, attempts: int):
        if not Game.__validate_attempts(attempts):
            raise ValueError("Invalid attempts value")

        self.__attempts = attempts

    @classmethod
    def color_text(cls, text: str, color: str) -> str:
        if color == "green":
            return "\033[92m{}\033[00m".format(text)
        elif color == "yellow":
            return "\033[93m{}\033[00m".format(text)
        elif color == "red":
            return "\033[91m{}\033[00m".format(text)
        elif color == "light purple":
            return "\033[94m{}\033[00m".format(text)
        elif color == "purple":
            return "\033[95m{}\033[00m".format(text)
        elif color == "cyan":
            return "\033[96m{}\033[00m".format(text)
        elif color == "light gray":
            return "\033[97m{}\033[00m".format(text)
        elif color == "black":
            return "\033[97m{}\033[00m".format(text)
        else:
            raise ValueError("Invalid color")

    @classmethod
    def __generate_colored_text_return_string_from_list_helper(cls, char_list: list[str], correctness_list: list[str]):
        colored_string: str = ""
        for ind, char in enumerate(char_list):
            if correctness_list[ind] == "here":
                colored_string += Game.color_text(char, "green")
            if correctness_list[ind] == "other":
                colored_string += Game.color_text(char, "yellow")
            if correctness_list[ind] == "not":
                colored_string += Game.color_text(char, "red")
            else:
                colored_string += char
        return colored_string

    @classmethod
    def generate_correctiveness_string_from_answer(cls, entered_word: str, correct_word: str) -> str:
        split_entered_word: list[str] = entered_word.split()
        split_correct_word: list[str] = correct_word.split()

        correctiveness_list: list[str] = []
        uses: dict[str, int] = {
            "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0
        }

        for ind, char in enumerate(split_entered_word):
            if char == split_correct_word[ind]:
                correctiveness_list[ind] = "here"
            elif char in correct_word and correct_word.count(char) > uses[char]:
                uses[char] += 1
                correctiveness_list[ind] = "other"
            else:
                correctiveness_list[ind] = "not"

        return Game.__generate_colored_text_return_string_from_list_helper(split_entered_word, correctiveness_list)

    def __ask_to_input_word(self, letters: int) -> str:
        valid = False
        word = ""
        while not valid:
            word = input("Enter a word to guess:\n")
            if word in self.__words and len(word.split()) == letters:
                valid = True
            else:
                print(f"{word} is not a valid word. Please try again and...")
        return word




