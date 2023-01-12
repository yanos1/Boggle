
def read_words():
    word_list = []
    with open("boggle_dict.txt") as f:
        for word in f.readlines():
            word_list.append(word.replace("\n", ""))
    return word_list






