def unique_in_order(iterable):
    split_list = list(iterable)
    if split_list[0] == split_list[1]:
        split_list.pop(1)

    for index, elem in enumerate(split_list):
        if (index + 1 < len(split_list) and index > 0):
            while split_list[index] == split_list[index - 1]:
                split_list.pop(index)

        if split_list[-1] == split_list[-2]:
            split_list.pop(1)
    return split_list

print(unique_in_order('AAAABBBCCDAABBB'))
#notsolvedyet