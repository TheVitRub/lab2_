import argparse


def calculate_sum(a, b):
    return a + b


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("a", type=int, nargs='?', help="First integer")
        parser.add_argument("b", type=int, nargs='?', help="Second integer")

        args = parser.parse_args()

        if args.a is None and args.b is None:
            print("NO PARAMS")
        elif args.a is None or args.b is None:
            print("TOO FEW PARAMS")
        else:
            print(calculate_sum(args.a, args.b))
    except argparse.ArgumentError as e:
        print(e)
    except Exception as e:
        print(type(e).__name__)


if __name__ == "__main__":
    main()