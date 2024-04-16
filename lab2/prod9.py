import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        formatted_lines = []
        current_line = ""

        for line in lines:
            words = line.strip().split()
            for word in words:
                if len(current_line) + len(word) + 1 <= frame_width:
                    if current_line:
                        current_line += " "
                    current_line += word
                else:
                    formatted_lines.append(current_line)
                    current_line = word

            if current_line:
                formatted_lines.append(current_line)
                current_line = ""

        formatted_lines = formatted_lines[:frame_height]

        return "\n".join(formatted_lines)
    except Exception as e:
        return str(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--frame-height", type=int, help="Frame height in characters")
    parser.add_argument("--frame-width", type=int, help="Frame width in characters")
    parser.add_argument("file_name", help="Name of the file")

    args = parser.parse_args()

    if args.frame_height and args.frame_width:
        formatted_text = format_text_block(args.frame_height, args.frame_width, args.file_name)
        print(formatted_text)
    else:
        print("Frame height and width must be provided.")


if __name__ == "__main__":
    main()