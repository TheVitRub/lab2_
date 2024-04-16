import argparse


def copy_file(source_file, dest_file, upper=False, lines=None):
    try:
        with open(source_file, 'r') as source:
            content = source.readlines()

            if upper:
                content = [line.upper() for line in content]

            if lines is not None:
                content = content[:lines]

            with open(dest_file, 'w') as dest:
                dest.writelines(content)

        print("File copied successfully!")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Source file name")
    parser.add_argument("dest", help="Destination file name")
    parser.add_argument("--upper", action="store_true", help="Convert text to upper case")
    parser.add_argument("--lines", type=int, help="Copy only the first N lines")

    args = parser.parse_args()

    copy_file(args.source, args.dest, args.upper, args.lines)


if __name__ == "__main__":
    main()