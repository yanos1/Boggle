from boggle_GUI import BoggleUI
from boggle_game import BoggleGame
from boggle_board_randomizer import randomize_board, LETTERS


class BoggleControl:
    """this class connecting between the UI part of our game and the backend
     part"""
    def __init__(self):
        """initialize ui object that gets the function below and acts
         according them"""
        self.ui = BoggleUI(self.add_chars, self.check_word, self.clear_word,
                           self.start_game, self.end_game)
        self.game = None
        self.ui.main_loop()

    def start_game(self):
        """
        creates game board and the game object
        :return: the new board
        """
        board = randomize_board(LETTERS)
        self.game: BoggleGame = BoggleGame(4, 4, board)
        return board

    def add_chars(self, letter):
        """
        manage the chars adding in the game
        :param letter: clicked letter
        :return: the word player creates
        """
        return self.game.append_letter(letter)

    def check_word(self):
        """
        manage the validation of a current word
        :return: word or score
        """
        return self.game.is_valid_word_check()

    def clear_word(self):
        """manage the deletion of word"""
        return self.game.clear_word()

    def end_game(self):
        """manage the end of the game"""
        return self.game.reset_all_words()


if __name__ == '__main__':
    boggle = BoggleControl()
