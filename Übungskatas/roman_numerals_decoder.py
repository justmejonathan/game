
def solution(roman):
    numbers_list = []
    calculated_list = []
    split_list = list(roman)
    for i in split_list:
        if i == 'M':
            numbers_list.append(1000)
        elif i == 'D':
            numbers_list.append(500)
        elif i == 'C':
            numbers_list.append(100)
        elif i == 'L':
            numbers_list.append(50)
        elif i == 'X':
            numbers_list.append(10)
        elif i == 'V':
            numbers_list.append(5)
        elif i == 'I':
            numbers_list.append(1)

    if len(numbers_list) == 1:
        calculated_list.append(numbers_list[0])
        cal_sum = sum(calculated_list)
        return cal_sum

    #start:
    if numbers_list[0] >= numbers_list[1]:
        calculated_list.append(numbers_list[0])
    # if numbers_list[0] < numbers_list[1]:
    #     start_num = numbers_list[1] - numbers_list[0]
    #     calculated_list.append(start_num)
    #middle:
    for index, elem in enumerate(numbers_list): 
        if (index + 1 < len(numbers_list) and index > 0):
            if numbers_list[index] > numbers_list[index - 1]:
                middle_num = numbers_list[index] - numbers_list[index - 1]
                calculated_list.append(middle_num)
            elif numbers_list[index] >= numbers_list[index + 1]:
                calculated_list.append(numbers_list[index])
    #end:
    if numbers_list[-1] > numbers_list[-2]:
        end_num = numbers_list[-1] - numbers_list[-2]
        calculated_list.append(end_num)
    if numbers_list[-1] <= numbers_list[-2]:
        calculated_list.append(numbers_list[-1])

    return sum(calculated_list)


    #         if numbers_list[index] >= numbers_list[next_item]:
    #             calculated_list.append(numbers_list[index])
    #         if numbers_list[index] < numbers_list[next_item]:
    #             new_num = numbers_list[next_item] - numbers_list[index]
    #             print(new_num)
    #             calculated_list.append(new_num)
    # cal_sum = sum(calculated_list)
    # print(len(numbers_list))
    # print(cal_sum)
    # print(calculated_list)
    # print(numbers_list)
    # print(split_list)

print (solution('MXIV'))







# if len(numbers_list) == 1:
#             calculated_list.append(numbers_list[0])
#             cal_sum = sum(calculated_list)
#     else:
#         if numbers_list[0] >= numbers_list[1]:
#             calculated_list.append(numbers_list[0])
#         for index, elem in enumerate(numbers_list): 
#             if (index + 1 < len(numbers_list) and index != 0):
#                 previous = index - 1
#                 next_i = index + 1
#                 if numbers_list[index] > numbers_list[previous]:
#                     new_num = numbers_list[index] - numbers_list[previous]
#                     calculated_list.append(new_num)
#                 elif numbers_list[index] == numbers_list[previous]:
#                         calculated_list.append(elem)
#                 elif numbers_list[index] < numbers_list[previous] and numbers_list[index] < numbers_list[next_i]:
#                     pass
#                 elif numbers_list[-1] < numbers_list[previous]:
#                         calculated_list.append(elem)
#                 elif numbers_list[index] < numbers_list[previous] and numbers_list[index] > numbers_list[next_i]:
#                         calculated_list.append(elem)