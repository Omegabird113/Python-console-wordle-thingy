from game import Game

if __name__ == "__main__":
    print(Game.color_text("a", "green") + Game.color_text("b", "red"))
    print(Game.generate_correctiveness_string_from_answer("gally", "goall"))

