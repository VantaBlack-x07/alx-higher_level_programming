#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    arg_len = sys.argv[1:]
    result = 0

    for arg in arg_len:
        result += int(arg)

    print(result)
