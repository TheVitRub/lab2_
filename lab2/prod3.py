import argparse


def main():
    parser = argparse.ArgumentParser(prog="solution.py", allow_abbrev=False)
    parser.add_argument('args', nargs='*', help='Arguments to print')

    args = parser.parse_args()

    if args.args:
        for arg in args.args:
            print(arg)
    else:
        print("no args")


if __name__ == "__main__":
    main()