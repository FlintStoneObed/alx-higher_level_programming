#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    x = 0
    for a in range(x):
        try:
            print(f"{my_list[a]}", end="")
            x += 1
        except Exception as error:
            break
    print()
    return x
