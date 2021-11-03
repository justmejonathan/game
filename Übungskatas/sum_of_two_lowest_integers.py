def sum_two_smallest_numbers(numbers):
    numbers.sort()
    first_pos = int(numbers[0])
    sec_pos = int(numbers[1])
    add_two_smallest = first_pos + sec_pos
    return(add_two_smallest)

sum_two_smallest_numbers([19, 5, 42, 2, 77])