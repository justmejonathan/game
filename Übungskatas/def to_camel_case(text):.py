# def to_camel_case(text):
#     x = text.replace('-', ' ').split(' ')
#     x = [y.replace('_', ' ') for y in x]
#     if x[0].istitle():
#         x = [word.capitalize() for word in x]
#         joined_again = "".join(x)
#         print(joined_again)
#     else:
#         first_word = x.pop(0)
#         x = [word.capitalize() for word in x]
#         y = "".join(x)
#         final = first_word + y
#         print(final)
# to_camel_case("hi_my_name_is_Marvin")

import re

def to_camel_case(text):
    x = re.split("_|-",text)
    if x[0].istitle():
        x = [word.capitalize() for word in x]
        joined_again = "".join(x)
        print(joined_again)
    else:
        first_word = x.pop(0)
        x = [word.capitalize() for word in x]
        y = "".join(x)
        final = first_word + y
        print(final)
to_camel_case("hi_my_name_is_Marvin")