from typing import List, Tuple, Iterable, Optional
from boggle_board_randomizer import randomize_board, LETTERS, BOARD_SIZE
from word_list import read_words
from pprint import pprint

Board = List[List[str]]
Path = List[Tuple[int, int]]

cur_board = randomize_board(LETTERS)
WORD_LIST = read_words()

MOVEMENTS = [(-1, 0), (1, 0), (0, 1), (0, -1),
             (-1, 1), (-1, -1), (1, 1), (1, -1)]


def board_locations(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board[0]))]


def no_space_between_locations(path):
    index = 1
    for row, col in path:  # 1, 2
        if abs(path[index][0]) - row > 1:
            return None
        if abs(path[index][1]) - col > 1:
            return None
        if index == len(path) - 1:
            break
        index += 1
    return True


def path_to_word(board: Board, path: Path):
    rows = len(board) - 1
    cols = len(board[0]) - 1
    word = ""
    for loc in path:
        if is_valid_location(loc, rows, cols):
            word += board[loc[0]][loc[1]]
        else:
            return None
    return word


def is_valid_location(location, rows_size, cols_size):
    if 0 <= location[0] <= rows_size and 0 <= location[1] <= cols_size:
        return True
    return False


def in_word_list(word: str):
    if word in WORD_LIST:
        return word
    return None


def does_combination_exist(combination, words):
    for word in words:
        if combination in word[0:len(combination) + 1]:
            return True
    return False


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[
    str]:
    if no_space_between_locations(path):
        word = path_to_word(board, path)
        res = in_word_list(word)
    else:
        return None
    return res


def add_tuples(tup1, tup2):
    return tuple(tup1[i] + tup2[i] for i in range(len(tup1)))


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[
    Path]:
    visited = [[False for i in range(len(board[0]))] for j in
               range(len(board))]
    return find_length_n_paths_helper(n, board, words, 0, visited, loc=(0, 0),
                                      cur_path=[], res=[])


def find_length_n_paths_helper(n: int, board: Board, words: Iterable[str],
                               size: int, visited, res, cur_path, loc):
    if size == n:
        word = path_to_word(board, cur_path)
        if word in words:
            res.append(cur_path)
            cur_path = []
        else:
            cur_path = []
            return
    cur_path.append(loc)
    cur_word = path_to_word(board, cur_path)
    if cur_word == None:

        return
    if not does_combination_exist(cur_word, words):
        return
    if visited[loc[0]][loc[1]]:
        return
    visited[loc[0]][loc[1]] = True

    for direction in MOVEMENTS:
        find_length_n_paths_helper(n, board, words, size + 1, visited, res,
                                   cur_path, add_tuples(loc, direction))
        visited[loc[0]][loc[1]] = False
        cur_path = cur_path[:-1]

    return res


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[
    Path]:
    visited = [[False for i in range(len(board[0]))] for j in
    range(len(board))]
    return find_length_n_paths_helper(n, board, words, 0, visited, loc=(0, 0),
                                      cur_path=[], res=[])


def find_length_n_words_helper(n: int, board: Board, words: Iterable[str],
                               size: int, visited, res, cur_path, loc):
    if size == n:
        word = path_to_word(board, cur_path)
        if word in words:
            res.append(word)
            cur_path = []
        else:
            cur_path = []
            return
    cur_path.append(loc)
    cur_word = path_to_word(board, cur_path)
    if cur_word == None:
        return
    if not does_combination_exist(cur_word, words):
        return
    if visited[loc[0]][loc[1]]:
        return
    visited[loc[0]][loc[1]] = True

    for direction in MOVEMENTS:
        find_length_n_paths_helper(n, board, words, size + 1, visited, res,
                                   cur_path, add_tuples(loc, direction))
        visited[loc[0]][loc[1]] = False
        cur_path = cur_path[:-1]

    return res


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass


if __name__ == '__main__':
    # Test 1
    # print(is_valid_path(cur_board, [(0, 0), (1, 0), (2, 0)], WORD_LIST))
    # print(is_valid_path(cur_board, [(0, 0), (1, 1), (2, 0)], WORD_LIST))
    # print(is_valid_path(cur_board, [(0, 0), (1, 0), (2, 0)], WORD_LIST))
    # print(is_valid_path(cur_board, [(0, 0), (1, 1), (1, 2)], WORD_LIST))
    # print("")
    # print(is_valid_path(cur_board, [(0, 0), (1, 2), (2, 0)], WORD_LIST))
    # print(is_valid_path(cur_board, [(0, 0), (1, 3), (2, 0)], WORD_LIST))
    # # Test 2
    # print(board_locations(cur_board))
    # Test 3
    pprint(cur_board)
    print(find_length_n_paths(3, cur_board, WORD_LIST))
    print(find_length_n_words(3, cur_board, WORD_LIST))
