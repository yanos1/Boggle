from typing import List, Tuple, Iterable, Optional
from boggle_board_randomizer import randomize_board, LETTERS
from word_list import read_words

Board = List[List[str]]
Path = List[Tuple[int, int]]

cur_board = randomize_board(LETTERS)
WORD_LIST = read_words()

MOVEMENTS = [(-1, 0), (1, 0), (0, 1), (0, -1),
             (-1, 1), (-1, -1), (1, 1), (1, -1)]


def has_space_between_locations(loc1, loc2):
    if abs(loc1[0] - loc2[0]) <= 1:
        if abs(loc1[1] - loc2[1]) <= 1:
            return True
    return

def path_to_word(board: Board, path: Path):
    word = ""
    for location in path:
        word += board[location[0]][location[1]]
    return word


def is_valid_path(board, path, words):
    rows_num = len(board)
    cols_num = len(board[0])
    for loc in range(len(path)-1):
        if not has_space_between_locations(path[loc],path[loc+1]):
            return None
    for loc in path:
        if 0 <= loc[0] < rows_num and 0 <= loc[1] < cols_num:
            pass
        else:
            return None
    word = path_to_word(board,path)
    if word in set(words):
        return word
    return None


def add_locations(loc1,loc2):
    return tuple(loc1[i]+loc2[i] for i in range(len(loc1)))


def get_all_around(board,location,path):
    num_rows = len(board)
    num_cols = len(board[0])
    locations_around = []
    for move in MOVEMENTS:
        cur = add_locations(location,move)
        if cur[0]  >=0 and cur[0] <num_rows and cur[1] >=0 and cur[1] <num_cols:
            if cur not in path:
                locations_around.append(cur)
    return locations_around


def word_exists(words, path, board):
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
    sorted_words = sorted(words)
    return sorted_words


def find_length_n_paths(n: int, board: Board, words) -> List[Path]:
    result= []
    words = sort_words(words)
    for i in range(len(board)):
        for j in range(len(board[i])):
            (find_length_n_paths_helper(n, board, [(i, j)],result, words))
    return result

def find_length_n_paths_helper(n: int, board: Board, path,result, words):
    if n > len(board)*len(board[0]):
        return []
    if len(path) == n:
        word = word_exists(words,path,board)
        if word != None:
            result.append(path[:])
        return
    if not should_it_keep_searching(path_to_word(board,path),words):
        return

    all_locations = get_all_around(board, path[-1], path)
    for location in all_locations:
        path.append(location)
        find_length_n_paths_helper(n, board, path, result, words)
        path.remove(path[-1])
    return


def find_len_n_words_help(all_paths,board,n,res):
    for path in all_paths:
        word_length = len(path_to_word(board, path))
        if word_length == n:
            res.append(path)
    return res


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[
    Path]:
    sol = []
    for i in range(n//2+1):
        cur_paths = find_length_n_paths(n-i,board,words)
        valid_paths = find_len_n_words_help(cur_paths,board,n,[])
        for path in valid_paths:
            sol.append(path)
    return sol


def should_it_keep_searching(comb,words):
    comb_len = len(comb)
    low = 0
    high = len(words)-1
    while low <= high:
        mid = (low + high)//2
        if words[mid][:comb_len]==comb.upper():
            return True
        elif words[mid][:comb_len] > comb.upper():
            high = mid-1
        else:
            low = mid+1

    return False


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    found = {}
    for i in range(len(board)*len(board[0]),2,-1):
        cur = find_length_n_words(i,board,words)
        for path in cur:
            if path_to_word(board,path) not in found:
                found[path_to_word(board,path)] = path
    return list(found.values())

