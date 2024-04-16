import sys


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

    if '--sort' in options:
        lines.sort()

    if '--num' in options:
        for i, line in enumerate(lines):
            print(f"{i} {line.strip()}")
    else:
        for line in lines:
            print(line.strip())

    if '--count' in options:
        print(f"rows count: {len(lines)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR")
    else:
        options = sys.argv[1:-1]
        filename = sys.argv[-1]
        lines = read_file(filename)
        print_file_content(lines, options)