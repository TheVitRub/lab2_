
import argparse


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return None


def print_file_content(lines, options):
    if lines is None:
        print("ERROR")
        return

    if options.sort:
        lines.sort()

    if options.num:
        for i, line in enumerate(lines):
            print(f"{i} {line.strip()}")
    else:
        for line in lines:
            print(line.strip())

    if options.count:
        print(f"rows count: {len(lines)}")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Name of the file")
    parser.add_argument("--count", action="store_true", help="Print the count of lines at the end")
    parser.add_argument("--num", action="store_true", help="Print line numbers")
    parser.add_argument("--sort", action="store_true", help="Sort lines alphabetically")

    return parser.parse_args()


def main():
    args = parse_arguments()
    lines = read_file(args.filename)
    print_file_content(lines, args)


if __name__ == "__main__":
    main()
