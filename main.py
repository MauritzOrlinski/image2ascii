from image_to_text.image_to_text import make_text, store_to_txt
from image_to_text.image_reader import get_image
import argparse


def main(input_file, width, store = None, print_out = None, output_file = None):
    image = get_image(input_file)
    output_for_terminal, output_for_file = make_text(image, width)

    if store:
        store_to_txt(output_for_file, output_file)

    if print_out:
        print(output_for_terminal)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Convert image to text")
    parser.add_argument("input_file", help = "Path to input file")
    parser.add_argument("width", help = "Width of output text", type = int)
    parser.add_argument("-s", "--store", help = "Store output to file", action = "store_true")
    parser.add_argument("-p", "--print_out", help = "Store output to file and print to terminal", action = "store_true")
    parser.add_argument("-o", "--output_file", help = "Path to output file")
    args = parser.parse_args()

    if args.store and args.output_file is None:
        parser.error("-s requires -o")

    elif args.input_file is None:
        parser.error("input_file is required")

    elif args.width is None:
        args.width = 100


    main(args.input_file, args.width, args.store, args.print_out, args.output_file)
