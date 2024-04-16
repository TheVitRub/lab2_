import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sort', action='store_true', help='Sort output by key')
    parser.add_argument('args', nargs='*', help='Key-value pairs')

    return parser.parse_args()


def main():
    args = parse_arguments()

    arguments = {}

    for arg in args.args:
        key, value = arg.split('=')
        arguments[key] = value

    if args.sort:
        arguments = dict(sorted(arguments.items()))

    for key, value in arguments.items():
        print(f"Key: {key} Value: {value}")


if __name__ == "__main__":
    main()