import sys


def parse_arguments(args):
    sort_flag = False
    key_value_pairs = {}

    for arg in args:
        if arg == "--sort":
            sort_flag = True
        else:
            key, value = arg.split('=')
            key_value_pairs[key] = value

    return sort_flag, key_value_pairs


def print_key_value_pairs(key_value_pairs, sort_flag):
    if sort_flag:
        sorted_pairs = sorted(key_value_pairs.items())
    else:
        sorted_pairs = key_value_pairs.items()

    for key, value in sorted_pairs:
        print(f"Key: {key} Value: {value}")


sort_flag, key_value_pairs = parse_arguments(sys.argv[1:])
print_key_value_pairs(key_value_pairs, sort_flag)