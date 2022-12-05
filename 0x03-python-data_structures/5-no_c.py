#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    i = 0
    for i in str_list:
        if i == 'c' or i == 'C':
            str_list[i] = ""
        i = i + 1
    return "".join(str_list)

