from ex11_utils import read_words


DIRECTIONS = [(1, 0), (1, 1), (0, 1), (0, -1), (1, -1), (-1, 0), (-1, 1),
              (-1, -1)]
WORDS = read_words()

class BoggleGame:
    def __init__(self, rows, cols, board):
        self._rows = rows
        self._cols = cols
        self.board = board
        self._cur_word = []
        self._words_found = []
        self.locations_remembered = []
        self._is_over = False
        self._last_clicked = None
        self._score = 0

    def get_cur_word(self):
        return self._cur_word

    def get_words_found(self):
        return self._words_found

    def reset_all_words(self):
        self._cur_word = []
        self._words_found = []
        self.locations_remembered = []
        return self._cur_word,self._words_found,self.locations_remembered



    def add_tuples(self, direction):
        return tuple((direction[i] + self._last_clicked[i]) for i in
                     range(len(direction)))

    def possible_location(self, location):
        if not self._last_clicked:
            return True

        elif abs(self._last_clicked[0] - location[0]) > 1 or \
        abs(self._last_clicked[1] - location[1]) > 1:
            return False
        elif location in self.locations_remembered:
            return False
        return True

    def append_letter(self, location):
        if self.possible_location(location):
            self._cur_word.append(self.board[location[0]][location[1]])
            self._last_clicked = location
            self.locations_remembered.append(location)
        return self._cur_word

    def is_valid_word_check(self):
        word = "".join(self._cur_word)
        self.clear_word()
        if word in WORDS and word not in self._words_found:
            self._score += len(word) ** 2
            self._words_found.append(word)
            self.locations_remembered = []
            return self.words_found_to_string().title(),self._score
        else:
            return False,self._score

    def words_found_to_string(self):
        words = ""
        is_first = True
        for word in self._words_found:
            if is_first:
                words+= word
                is_first = False
            else:
                words +=f",{word} "
        return words

    def clear_word(self):
        self._cur_word = []
        self._last_clicked = None
        self.locations_remembered = []
        return self._cur_word

