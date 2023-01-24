from typing import List, Tuple, Iterable

Board = List[List[str]]
Path = List[Tuple[int, int]]

MOVEMENTS = [(-1, 0), (1, 0), (0, 1), (0, -1),
             (-1, 1), (-1, -1), (1, 1), (1, -1)]


def read_words():
    """
    this function creates list of words from exist file
    :return: list of words
    """
    word_list = []
    with open("boggle_dict.txt") as f:
        for word in f.readlines():
            word_list.append(word.replace("\n", ""))
    return word_list


###################################################


def has_space_between_locations(loc1, loc2):
    """
    this func checks if current path is continues
    :param loc1: first coordinate.
    :param loc2: second coordinate
    :return: True if it is a valid path, none either
    """
    if abs(loc1[0] - loc2[0]) <= 1:
        if abs(loc1[1] - loc2[1]) <= 1:
            return True
    return


def path_to_word(board: Board, path: Path):
    """
    this function translate locations in path to word
    :param board: game board
    :param path: path
    :return: word
    """
    word = ""
    for location in path:
        word += board[location[0]][location[1]]
    return word


def is_valid_path(board, path, words):
    """
    checks if our path is valid
    :param board: game board
    :param path: path
    :param words: a list of words
    :return: word if it is valid, else None
    """
    rows_num = len(board)
    cols_num = len(board[0])
    for loc in range(len(path) - 1):
        if not has_space_between_locations(path[loc], path[loc + 1]):
            return None
    for loc in path:  # in board
        if 0 <= loc[0] < rows_num and 0 <= loc[1] < cols_num:
            pass
        else:
            return None
    word = path_to_word(board, path)
    if word in set(words):  # if word in word list
        return word
    return None


def add_locations(loc1, loc2):
    """
    moves the location on board
    """
    return tuple(loc1[i] + loc2[i] for i in range(len(loc1)))


def get_all_around(board, location, path):
    """
    checks the location of the neighbors of a current location
    :param board: game board
    :param location: currant location
    :param path: path
    :return: list of location around our location
    """
    num_rows = len(board)
    num_cols = len(board[0])
    locations_around = []
    for move in MOVEMENTS:
        cur = add_locations(location, move)
        if cur[0] >= 0 and cur[0] < num_rows and cur[1] >= 0 and cur[1] < num_cols:
            if cur not in path:
                locations_around.append(cur)
    return locations_around


def word_exists(words, path, board):
    """
    searching in binary search if currant word belongs to the list of words
    :param words: list of words
    :param path: path of word
    :param board: game board
    :return: word if it's in our collection else None
    """
    word = path_to_word(board, path)
    left = 0
    right = len(words) - 1
    while left <= right:
        middle = (left + right) // 2
        if words[middle] == word:
            return middle
        elif words[middle] < word:
            left = middle + 1
        else:
            right = middle - 1
    return None


def sort_words(words):
    """sort the list of words"""
    sorted_words = sorted(words)
    return sorted_words


def find_length_n_paths(n: int, board: Board, words) -> List[Path]:
    """
    finds all paths with n length
    :param n: length
    :param board: game board
    :param words: list of words
    :return: list of all n' length paths
    """
    result = []
    words = sort_words(words)
    for i in range(len(board)):
        for j in range(len(board[i])):
            (find_length_n_paths_helper(n, board, [(i, j)], result, words))
    return result


def find_length_n_paths_helper(n: int, board: Board, path, result, words):
    """
    helps previous function find n' length paths by using backtracking
    :param n: length
    :param board: game board
    :param path: beginning of path
    :param result: empty list
    :param words: words collection
    :return: list of all paths we found
    """
    if n > len(board) * len(board[0]):
        return []
    if len(path) == n:
        word = word_exists(words, path, board)
        if word != None:
            result.append(path[:])
        return
    if not should_it_keep_searching(path_to_word(board, path), words):
        #  if the beginnig of the word doen't exist in the collection, stop
        return
    all_locations = get_all_around(board, path[-1], path)
    for location in all_locations:
        path.append(location)
        find_length_n_paths_helper(n, board, path, result, words)
        path.remove(path[-1])
    return


def find_len_n_words_help(all_paths, board, n, res):
    """
    gets a list of paths translate each path to word and add it if it is n' length
    :param all_paths: all paths n' length
    :param board: game board
    :param n: word length
    :param res: list of valid words
    :return:
    """
    for path in all_paths:
        word_length = len(path_to_word(board, path))
        if word_length == n:
            res.append(path)
    return res


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> \
        List[Path]:
    """
    finds all the words in n' length
    :param n: length
    :param board: game board
    :param words: collection
    :return: list of all words we found
    """
    sol = []
    for i in range(n // 2 + 1):
        cur_paths = find_length_n_paths(n - i, board, words)
        valid_paths = find_len_n_words_help(cur_paths, board, n, [])
        for path in valid_paths:
            sol.append(path)
    return sol


def should_it_keep_searching(comb, words):
    """
    gets the beginning of word and search it by binary search in word collection
    :return: True if found, else False
    """
    comb_len = len(comb)
    low = 0
    high = len(words) - 1
    while low <= high:
        mid = (low + high) // 2
        if words[mid][:comb_len] == comb.upper():
            return True
        elif words[mid][:comb_len] > comb.upper():
            high = mid - 1
        else:
            low = mid + 1

    return False


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    returns a list of valid paths that gets the max score
    :param board:game voard
    :param words: word collection
    """
    found = {}
    for i in range(len(board) * len(board[0]), 2, -1):
        cur = find_length_n_words(i, board, words)
        for path in cur:
            if path_to_word(board, path) not in found:
                found[path_to_word(board, path)] = path
    return list(found.values())
