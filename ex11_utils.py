from typing import List, Tuple, Iterable, Optional
from boggle_board_randomizer import randomize_board, LETTERS
from word_list import read_words
from pprint import pprint

Board = List[List[str]]
Path = List[Tuple[int, int]]

cur_board = randomize_board(LETTERS)
WORD_LIST = read_words()

MOVEMENTS = [(-1, 0), (1, 0), (0, 1), (0, -1),
             (-1, 1), (-1, -1), (1, 1), (1, -1)]

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


def in_word_list_log_time(word: str,words):
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
        return


def is_valid_path(board: Board, path: Path, words) -> Optional[
    str]:
    if no_space_between_locations(path):
        word = path_to_word(board, path)
        res = in_word_list_log_time(word,words)
        if res:
            return words[res]
        else:
            return None
    else:
        return None


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[
    Path]:
    res = []
    visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            find_length_n_paths_helper(n,board, visited, i, j, [], words, res)
    return res


def find_length_n_paths_helper(n, board, visited, i, j, current_path, words, res):
    if len(current_path) == n:
        word = path_to_word(board,current_path)
        if in_word_list_log_time(word,words):
            if current_path not in res:
                res.append(current_path)
        return
    if not is_valid_location((i,j),len(board)-1,len(board[0])-1):
        return
    if visited[i][j]:
        return
    current_path.append((i,j))
    visited[i][j] = True
    for direction in MOVEMENTS:
        find_length_n_paths_helper(n,board,visited,i+direction[0],j +direction[1],current_path,words,res)
    visited[i][j] = False
    current_path = current_path[:-1]

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


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:

    found = {}
    for i in range(len(board)*len(board[0]),2,-1):
        cur = find_length_n_words(i,board,words)
        for path in cur:
            if path_to_word(board,path) not in found:
                found[path_to_word(board,path)] = path
    return list(found.values())








