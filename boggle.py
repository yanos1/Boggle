from boggle_GUI import BoggleUI
from boggle_game import BoggleGame
from word_list import WORDS
from boggle_board_randomizer import randomize_board, LETTERS


class BoggleControl:
    def __init__(self):
        self.ui = BoggleUI(self.add_chars, self.check_word,self.clear_word, self.start_game)
        self.game = None
        self.ui.main_loop()

    def start_game(self):
        board = randomize_board(LETTERS)
        self.game:BoggleGame = BoggleGame(4,4,board)
        return board

    def add_chars(self,letter):
        return self.game.append_letter(letter)


    def check_word(self):
        return self.game.is_valid_word_check()

    def clear_word(self):
        return self.game.clear_word()


if __name__ == '__main__':
    boggle = BoggleControl()

