def get_count(sentence):
    letter_list = list(sentence)
    amount_a = letter_list.count("a")
    amount_e = letter_list.count("e")
    amount_i = letter_list.count("i")
    amount_o = letter_list.count("o")
    amount_u = letter_list.count("u")
    amount_vowels = amount_a + amount_e + amount_i + amount_o + amount_u
    return(amount_vowels)

get_count("hello my name is marvin")