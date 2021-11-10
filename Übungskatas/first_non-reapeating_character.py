def first_non_repeating_letter(string):
    split_list = list(string)
    low_list = list(string)
    new_list = []
    for i in range(len(low_list)):
        low_list[i] = low_list[i].lower()
    for index,n in enumerate(low_list):
        if low_list.count(n) > 1:
            pass
        elif low_list.count(n) == 1:
            return(split_list[index])
    return('')

print(first_non_repeating_letter("TVLlvVPpSStt"))