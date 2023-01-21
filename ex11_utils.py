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
#
# def no_space_between_locations(path):
#     index = 1
#     for row, col in path:  # 1, 2
#         if abs(path[index][0]) - row > 1:
#             return None
#         if abs(path[index][1]) - col > 1:
#             return None
#         if index == len(path) - 1:
#             break
#         index += 1
#     return True
#
#
# def path_to_word(board: Board, path: Path):
#     rows = len(board) - 1
#     cols = len(board[0]) - 1
#     word = ""
#     for loc in path:
#         if is_valid_location(loc, rows, cols):
#             word += board[loc[0]][loc[1]]
#         else:
#             return None
#     return word
#
#
# def is_valid_location(location, rows_size, cols_size):
#     if 0 <= location[0] <= rows_size and 0 <= location[1] <= cols_size:
#         return True
#     return False
#
#
# def in_word_list_log_time(word: str,words):
#         left = 0
#         right = len(words) - 1
#         while left <= right:
#             middle = (left + right) // 2
#             if words[middle] == word:
#                 return middle
#             elif words[middle] < word:
#                 left = middle + 1
#             else:
#                 right = middle - 1
#         return
#
#
# def is_valid_path(board: Board, path: Path, words) -> Optional[
#     str]:
#     if no_space_between_locations(path):
#         word = path_to_word(board, path)
#         res = in_word_list_log_time(word,words)
#         if res:
#             return words[res]
#         else:
#             return None
#     else:
#         return None
#
#
#
# def find_length_n_paths(n,board: List[List[str]], words: List[str]) -> List[List[Tuple[int,int]]]:
#     rows, cols = len(board), len(board[0])
#     found_paths = []
#     visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
#     for row in range(rows):
#         for col in range(cols):
#             find_length_n_paths_helper(n,board, row, col, [], found_paths, words,visited)
#     return found_paths
#
# def find_length_n_paths_helper(n,board: List[List[str]], row: int, col: int, current_path: List[Tuple[int,int]], found_paths: List[List[Tuple[int,int]]], words: List[str],visited):
#     if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
#         return
#     if visited[row][col]:
#         return
#
#     if len(current_path) == n:
#         word = path_to_word(board, current_path)
#         if word in words:
#             if current_path not in found_paths:
#                 found_paths.append(current_path.copy())
#         return
#
#     current_path.append((row,col))
#     visited[row][col] = True
#     for move in MOVEMENTS:
#         find_length_n_paths_helper(n,board, row+move[0], col+move[1], current_path, found_paths, words,visited)
#     visited[row][col] = False
#     current_path.pop()
#
#
# def find_len_n_words_help(all_paths,board,n,res):
#     for path in all_paths:
#         word_length = len(path_to_word(board, path))
#         if word_length == n:
#             res.append(path)
#     return res
#
#
# def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[
#     Path]:
#     sol = []
#     for i in range(n//2+1):
#         cur_paths = find_length_n_paths(n-i,board,words)
#         valid_paths = find_len_n_words_help(cur_paths,board,n,[])
#         for path in valid_paths:
#             sol.append(path)
#     return sol
#
#
# def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
#
#     found = {}
#     for i in range(len(board)*len(board[0]),2,-1):
#         cur = find_length_n_words(i,board,words)
#         for path in cur:
#             if path_to_word(board,path) not in found:
#                 found[path_to_word(board,path)] = path
#     return list(found.values())

##########################################YAN




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

def find_path(word, board, path, now_word, all_paths, only_one=False):
    # if only_one and there_is_shorter(all_paths, path):
    #     return
    if len(now_word) == len(word):
        print(word, now_word)
        if only_one and all_paths != []:
            if len(all_paths[0]) < len(path):
                all_paths[0] = path.copy()
        else:
            all_paths.append(path.copy())
        return
    for cell in get_all_around(path[-1], board,[]):
        now1_word = now_word + board[cell[0]][cell[1]]
        if cell not in path and now1_word == word[:len(now1_word)]:
            path.append(cell)
            find_path(word, board, path, now1_word, all_paths, only_one)
            del path[-1]


def find_paths(word, board, only_one=False):
    all_word_paths = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[:len(board[i][j])]:
                find_path(word, board, [(i,j)], board[i][j],
                          all_word_paths, only_one)
    return  all_word_paths



def should_it_keep_searching(comb,words):
    cur_comb = ""
    count = 0
    for i in range(1, len(comb)+1):
        cur_comb+=comb[i-1]
        low = 0
        high = len(words)-1
        while low <=high:
            mid = (low +high)//2
            print(words[mid][:i],cur_comb)
            if words[mid][:i]==cur_comb.upper():
                print(i, mid)

                count +=1
                break
            elif words[mid][:i] >cur_comb:
                high = mid
            else:
                low = mid


    if count == len(comb):
        return True
    return False

print(should_it_keep_searching("abf",WORD_LIST))
print(should_it_keep_searching("abdsadfg",WORD_LIST))
print(should_it_keep_searching("abgfdgdsf",WORD_LIST))
print(should_it_keep_searching("abddf",WORD_LIST))
print(should_it_keep_searching("abaf",WORD_LIST))
print(should_it_keep_searching("darkn",WORD_LIST))
print(should_it_keep_searching("faaa",WORD_LIST))
print(should_it_keep_searching("falllll",WORD_LIST))
print(should_it_keep_searching("foel",WORD_LIST))
print(should_it_keep_searching("abf",WORD_LIST))
print(should_it_keep_searching("asdgggghhhhhhhhhhg",WORD_LIST))






def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:

    found = {}
    for i in range(len(board)*len(board[0]),2,-1):
        print("round", i)
        cur = find_length_n_words(i,board,words)
        for path in cur:
            if path_to_word(board,path) not in found:
                found[path_to_word(board,path)] = path
    return list(found.values())


board = [[
    # Normal board
    ['A', 'I', 'P', 'H'],
    ['I', 'R', 'S', 'S'],
    ['A', 'E', 'E', 'T'],
    ['T', 'H', 'E', 'R']],
    [
        # Board with doubles
        ['E', 'M', 'AB', 'O'],
        ['IN', 'ON', 'AN', 'M'],
        ['ST', 'R', 'U', 'TH'],
        ['Y', 'ST', 'R', 'W']],
    [
        # Board with doubles
        ['W', 'E', 'AI', 'G'],
        ['S', 'N', 'AO', 'A'],
        ['TH', 'N', 'O', 'IN'],
        ['W', 'D', 'D', 'M']],
    [
        ['W', 'S', 'E', 'E'],
        ['Y', 'TH', 'H', 'AE'],
        ['M', 'I', 'Y', 'A'],
        ['T', 'W', 'H', 'C']]]

expected = [[('AIR', 9), ('AIRS', 16), ('AIRIEST', 49), ('AIREST', 36),
             ('AIRER', 25), ('AIS', 9), ('AIA', 9), ('ARS', 9),
             ('ARSE', 16), ('ARSES', 25), ('ARIS', 16), ('ARISH', 25),
             ('ARISE', 25), ('ARISES', 36), ('ARIA', 16), ('ARE', 9),
             ('ARES', 16), ('AREA', 16), ('ARET', 16), ('ARETS', 25),
             ('ARETE', 25), ('ARERE', 25), ('IRE', 9), ('IRES', 16),
             ('IRATE', 25), ('IRATEST', 49), ('ISH', 9), ('PIA', 9),
             ('PIR', 9), ('PIRS', 16), ('PIRAI', 25), ('PIRATE', 36),
             ('PIRATES', 49), ('PIS', 9), ('PISS', 16), ('PISSER', 36),
             ('PISH', 16), ('PISE', 16), ('PISES', 25), ('PISTE', 25),
             ('PISTES', 36), ('PSST', 16), ('PSI', 9), ('PST', 9),
             ('PRISS', 25), ('PRISE', 25), ('PRISES', 36),
             ('PRISER', 36), ('PRISERE', 49), ('PRAISE', 36),
             ('PRAISES', 49), ('PRAISER', 49), ('PRIES', 25),
             ('PRIEST', 36), ('PRIESTS', 49), ('PRE', 9), ('PREE', 16),
             ('PREES', 25), ('PRESS', 25), ('PRESSER', 49),
             ('PRESE', 25), ('PRESET', 36), ('PRESETS', 49),
             ('PRESES', 36), ('PREST', 25), ('PRESTS', 36),
             ('PRESTER', 49), ('PRAESES', 49), ('PRAT', 16),
             ('PRATE', 25), ('PRATES', 36), ('PREHEAT', 49),
             ('IRIS', 16), ('IRISES', 36), ('RIP', 9), ('RIPS', 16),
             ('RIA', 9), ('RISP', 16), ('RISPS', 25), ('RISE', 16),
             ('RISES', 25), ('RISER', 25), ('RAI', 9), ('RAIS', 16),
             ('RAISE', 25), ('RAISES', 36), ('RAISER', 36),
             ('RAIA', 16), ('REE', 9), ('REES', 16), ('REEST', 25),
             ('REESTS', 36), ('RES', 9), ('RESH', 16), ('RESET', 25),
             ('RESETS', 36), ('RESES', 25), ('RESEE', 25),
             ('REST', 16), ('RESTS', 25), ('RESTER', 36), ('REI', 9),
             ('REH', 9), ('RET', 9), ('RAT', 9), ('RATH', 16),
             ('RATHE', 25), ('RATHER', 36), ('RATHEREST', 81),
             ('RATHEST', 49), ('RATE', 16), ('RATES', 25), ('RAH', 9),
             ('RETS', 16), ('RETREE', 36), ('RETREES', 49),
             ('RETE', 16), ('RESEAT', 36), ('REHEAT', 36),
             ('SPIRE', 25), ('SPIREA', 36), ('SPIRES', 36),
             ('SPREE', 25), ('SPREES', 36), ('SPREATHE', 64),
             ('SPREATHES', 81), ('SPRAT', 25), ('SPREETHE', 64),
             ('SIP', 9), ('SIPS', 16), ('SIR', 9), ('SIRI', 16),
             ('SIRE', 16), ('SIREE', 25), ('SIREES', 36),
             ('SIRES', 25), ('SRI', 9), ('SET', 9), ('SETS', 16),
             ('SESH', 16), ('SER', 9), ('SERIPH', 36), ('SERIPHS', 49),
             ('SERA', 16), ('SERAI', 25), ('SERIATE', 49),
             ('SERE', 16), ('SEE', 9), ('SEER', 16), ('SEETHE', 36),
             ('SEETHER', 49), ('SEES', 16), ('SERES', 25),
             ('SEREST', 36), ('SERER', 25), ('SEI', 9), ('SEIR', 16),
             ('SEA', 9), ('SEAR', 16), ('SEARE', 25), ('SEAREST', 49),
             ('SEARER', 36), ('SEAT', 16), ('SETA', 16), ('STERE', 25),
             ('STEER', 25), ('STREET', 36), ('STERES', 36),
             ('STEERER', 49), ('SPIRIEST', 64), ('SPRIEST', 49),
             ('STEERS', 36),
             ('STEERIES', 64), ('SESE', 16), ('SERS', 16),
             ('SERAIS', 36), ('SERIATES', 64), ('SERIES', 36),
             ('SEERS', 25), ('AESIR', 25), ('AETHER', 36),
             ('AETHERS', 49), ('ARAISE', 36), ('ARAISES', 49),
             ('ATE', 9), ('ATES', 16), ('ESS', 9), ('ESSE', 16),
             ('ESES', 16), ('EST', 9), ('ESTS', 16), ('ESTER', 25),
             ('ERS', 9), ('ERSES', 25), ('ERST', 16), ('ERA', 9),
             ('ERE', 9), ('ERES', 16), ('EAR', 9), ('EARS', 16),
             ('EARST', 25), ('EAT', 9), ('EATH', 16), ('EATHE', 25),
             ('ETH', 9), ('ETHE', 16), ('ETHER', 25), ('ETHERS', 36),
             ('ETHERISH', 64), ('ETHERIST', 64), ('ETHERISTS', 81),
             ('ETA', 9), ('TES', 9), ('TESSERA', 49), ('TERSE', 25),
             ('TERAI', 25), ('TERAIS', 36), ('TERES', 25), ('TEE', 9),
             ('TEES', 16), ('TEER', 16), ('TEERS', 25), ('TEETH', 25),
             ('TEETHE', 36), ('TEETHER', 49), ('TRES', 16),
             ('TRESS', 25), ('TREE', 16), ('TREES', 25),
             ('TEETHES', 49), ('TEETHERS', 64), ('THE', 9),
             ('THERE', 25), ('THERES', 36), ('THETE', 25),
             ('THETES', 36), ('THEE', 16), ('THEES', 25),
             ('THESP', 25), ('THESPS', 36), ('THESE', 25),
             ('THESES', 36), ('THEIR', 25), ('THEIRS', 36),
             ('THAE', 16), ('THAR', 16), ('THARS', 25), ('TEETER', 36),
             ('TEST', 16), ('TESTS', 25), ('TESTE', 25),
             ('TESTES', 36), ('TESTER', 36), ('TESTEE', 36),
             ('TESTEES', 49), ('TERSEST', 49), ('TERSER', 36),
             ('TERETE', 36), ('TEA', 9), ('TEAR', 16), ('TEARS', 25),
             ('TEARER', 36), ('TEETERS', 49), ('TAE', 9), ('TAES', 16),
             ('TAR', 9), ('TARS', 16), ('TARSI', 25), ('TARSIA', 36),
             ('TARP', 16), ('TARPS', 25), ('TARA', 16), ('TARE', 16),
             ('TARES', 25), ('TAI', 9), ('TAIRA', 25), ('HER', 9),
             ('HERE', 16), ('HERES', 25), ('HET', 9), ('HETS', 16),
             ('HETE', 16), ('HETES', 25), ('HES', 9), ('HESP', 16),
             ('HESPS', 25), ('HEST', 16), ('HESTS', 25), ('HERS', 16),
             ('HERSE', 25), ('HERIES', 36), ('HEREAT', 36),
             ('HERSES', 36), ('HERISSE', 49), ('HEIR', 16),
             ('HEIRS', 25), ('HEIRESS', 49), ('HEAR', 16),
             ('HEARS', 25), ('HEARSE', 36), ('HEARSES', 49),
             ('HEARE', 25), ('HEARES', 36), ('HEARER', 36),
             ('HEAT', 16), ('HETAIRIA', 64), ('HETAIRIST', 81),
             ('HETAIRISTS', 100), ('HETAIRA', 49), ('HETAIRAI', 64),
             ('HAE', 9), ('HAES', 16), ('HAERES', 36), ('HAET', 16),
             ('HARSH', 25), ('HARP', 16), ('HARPIST', 49),
             ('HARPISTS', 64), ('HARPS', 25), ('HARISH', 36),
             ('HARE', 16), ('HARES', 25), ('HAIR', 16), ('HAIRS', 25),
             ('HAIRST', 36), ('HAIRSTS', 49), ('HAT', 9), ('HATE', 16),
             ('HATES', 25), ('HATER', 25), ('HATERS', 36),
             ('EERIE', 25), ('EERIEST', 49), ('RESPIRE', 49),
             ('RESPIRES', 64), ('RERISE', 36), ('RERAISE', 49),
             ('REHEAR', 36), ('REHEARS', 49), ('REHEARSE', 64),
             ('REHEARSES', 81)],
            [('EON', 4), ('MEIN', 9), ('MON', 4), ('MINE', 9),
             ('MANO', 9), ('MAN', 4), ('ABO', 4), ('ONE', 4),
             ('ONST', 4), ('ANON', 4), ('MOAN', 9), ('MURINE', 25),
             ('MURR', 16), ('MURRINE', 36), ('MURRIN', 25),
             ('MURRY', 25), ('MUON', 9), ('MUSTY', 16), ('MUST', 9),
             ('STY', 4), ('STRUM', 16), ('STRINE', 16), ('STONE', 9),
             ('RONIN', 9), ('RONE', 9), ('RUTH', 9), ('RUM', 9),
             ('RUSTY', 16), ('RUST', 9), ('RINE', 9), ('RIN', 4),
             ('RAN', 4), ('URINE', 16), ('THAN', 4), ('THRUM', 16),
             ('THRUST', 16), ('THRU', 9), ('STUM', 9), ('WURST', 16)],
            [('WENS', 16), ('WEN', 9), ('ENS', 9), ('AIGA', 9),
             ('AINE', 9), ('AINS', 9), ('AIN', 4), ('AIA', 4),
             ('GAINS', 16), ('GAIN', 9), ('SNOD', 16), ('SEWN', 16),
             ('SEW', 9), ('SEN', 9), ('NEWS', 16), ('NEW', 9),
             ('NTH', 4), ('NON', 9), ('NOD', 9), ('NOMINA', 25),
             ('NOM', 9), ('AGAIN', 16), ('NONES', 25), ('NONE', 16),
             ('ONS', 9), ('ODD', 9), ('ONES', 16), ('ONE', 9),
             ('DONNES', 36), ('DONNE', 25), ('DONS', 16), ('DON', 9),
             ('DOD', 9), ('DONE', 16), ('DOM', 9), ('DINO', 9),
             ('DIN', 4), ('MINA', 9), ('MINO', 9), ('MIND', 9),
             ('MONTHS', 25), ('MONTH', 16), ('MONS', 16), ('MON', 9),
             ('MOD', 9), ('MOA', 9)],
            [('SWY', 9), ('SEE', 9), ('SYTHE', 16), ('SHE', 9),
             ('SHY', 9), ('SHIM', 16), ('SHIT', 16), ('SHAY', 16),
             ('SHAH', 16), ('SHA', 9), ('EHS', 9), ('ETHS', 9),
             ('ETH', 4), ('THYMI', 16), ('THY', 4), ('THEE', 9),
             ('THE', 4), ('HES', 9), ('HETHS', 16), ('HETH', 9),
             ('HYTHES', 25), ('HYTHE', 16), ('HAE', 4), ('HITHES', 25),
             ('HITHE', 16), ('HIM', 9), ('HIYA', 16), ('HIT', 9),
             ('HAY', 9), ('HAH', 9), ('MYTHS', 16), ('MYTHI', 16),
             ('MYTHY', 16), ('MYTH', 9), ('MIHA', 16), ('YAHS', 16),
             ('YAH', 9), ('YAE', 4), ('ACHY', 16), ('ACH', 9),
             ('AHS', 9), ('AHI', 9), ('TITHES', 25), ('TITHE', 16),
             ('WITHS', 16), ('WITHY', 16), ('WITHES', 25),
             ('WITHE', 16), ('WITH', 9), ('WIT', 9), ('WHY', 9),
             ('WHIM', 16), ('WHIT', 16), ('WHA', 9), ('WYCH', 16),
             ('HAHS', 16), ('CAY', 9), ('CHIT', 16), ('CHI', 9),
             ('CHAY', 16), ('CHA', 9)]
            ]

all_word_from_dict = WORD_LIST  # Put all words from the dict
for test_num in range(len(board)):
    result = max_score_paths(board[test_num], all_word_from_dict)
    result = [(''.join([board[test_num][i][j] for i, j in path]),
               len(path) ** 2) for path in result]
    assert sorted(result) == sorted(expected[test_num])

def max_score_pathsx(board: Board, words) -> List[Path]:
    paths = []
    for word in words:
        path = find_paths(word, board, True)
        paths.extend(path)
    return paths
