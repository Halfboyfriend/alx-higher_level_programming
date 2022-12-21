#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    
    Args:
        my_list(list): The list to be printed.
        x(int): The num of elements


    Returns:
        The num of elements to be printed.


    """
    i = 0
    for k in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return ret
