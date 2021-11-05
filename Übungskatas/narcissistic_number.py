def narcissistic( value ):
    length_str = str(value)
    length_value = len(length_str)
    value_list = [int(d) for d in length_str]
    sum_of_powered_numbers = sum([x**length_value for x in value_list])
    if value == sum_of_powered_numbers:
        return True
    else:
        return False

narcissistic(123)