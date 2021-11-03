def find_short(s):
    word_list = s.split()
    word_list.sort(key=len)
    shortest_word = word_list[0]
    l = len(shortest_word)
    return l # l: shortest word length

find_short("bitcoin take over the world maybe who knows perhaps")