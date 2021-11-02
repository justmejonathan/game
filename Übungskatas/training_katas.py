
def digital_root(n):
    list_of_numbers = [int(d) for d in str(n)]
    while True:
        b = sum(list_of_numbers)
        if b < 10:
            return b
        list_of_numbers = [int(d) for d in str(b)]

print(digital_root(6666))
    
def root(n):
    numbers = [int(x) for x in str(n)]
    res = sum(numbers)
    if res>=10:
        return root(res)

    return res

print(root(6666))

# def digital_root(n):
#     list_of_numbers = str(n)
#     while len(list_of_numbers) >= 2:
#         new_list = [int(d) for d in list_of_numbers]
#         b = sum(new_list)     
#         str(b)
#         print(new_list)

# digital_root(6666)