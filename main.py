from game import Game
import words

if __name__ == "__main__":
    g = Game(words.get_words_list(5, 6), 5)
    g.play()