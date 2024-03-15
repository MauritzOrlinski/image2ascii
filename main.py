import os
import sys
import time
from image_to_text.image_to_text import make_text, store_to_txt, get_color
from image_to_text.image_reader import get_image
import argparse
from image_to_text.terminal_size import get_terminal_size
import threading

stop_val = False


def signal_user_input():
    global stop_val
    i = input("wait for input")
    stop_val = True


def main(input_file, width, height=None, store=None, print_out=None, output_file=None, colorful=True, extended_chars=0, luminosity=True):
    image, bright = get_image(input_file)
    _, output_for_file = make_text(image, bright, width, colorful=colorful,
                                                     extended_chars=extended_chars, luminosity=luminosity, height=height)

    if store:
        store_to_txt(output_for_file, output_file)

    if print_out:
        threading.Thread(target=signal_user_input).start()
        clear_console = 'clear' if os.name == 'posix' else 'CLS'
        text_blink = 0
        while not stop_val:
            output_for_terminal, _ = make_text(image, bright, int(get_terminal_size()[1] / (extended_chars + 1)), colorful=colorful,
                                               extended_chars=extended_chars, luminosity=luminosity,
                                               height=get_terminal_size()[0] - 4)
            os.system(clear_console)
            sys.stdout.write(output_for_terminal)
            sys.stdout.write("\n" if text_blink % 4 <= 1 else "\nPress ENTER to exit")
            text_blink+=1
            sys.stdout.flush()
            time.sleep(0.1)
        os.system(clear_console)
        print("\033[0m Bye")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert image to text")
    parser.add_argument("input_file", help="Path to input file")
    parser.add_argument("-s", "--store", help="Store output to file", action="store_true")
    parser.add_argument("-p", "--print_out", help="Store output to file and print to terminal", action="store_true")
    parser.add_argument("-o", "--output_file", help="Path to output file")
    parser.add_argument("-dl", "--deactivate_luminosity", help="Decide if you want the program to simulate luminosity with chars"
                                                   "this should be disabled when using colorful mode in terminals with "
                                                   "no dark background. If this is disabled --colorful has to be enabled",
                        action="store_true", default=False)
    parser.add_argument("-c", "--colorful", help="Make the output colorful", action="store_true", default=False)
    parser.add_argument("-a", "--auto_width", help="get the maximal output width ", action="store_true", default=False)
    parser.add_argument("width", nargs='?', const=None, help="Width of output text", type=int)
    args = parser.parse_args()

    if args.store and args.output_file is None:
        parser.error("-s requires -o")

    elif args.input_file is None:
        parser.error("input_file is required")

    elif args.deactivate_luminosity and not args.colorful:
        parser.error("Violates the rule if --luminosity_active is disabled --colorful has to be enabled")
    elif args.width is None and not args.auto_width:
        parser.error("No width is given")
    elif args.width is None and args.auto_width:
        main(input_file=args.input_file, width=get_terminal_size()[1], height=get_terminal_size()[0], store=args.store, print_out=args.print_out,
             output_file=args.output_file, colorful=args.colorful, luminosity=args.deactivate_luminosity)
    else:
        main(input_file=args.input_file, width=args.width, store=args.store, print_out=args.print_out,
             output_file=args.output_file, colorful=args.colorful, luminosity=args.deactivate_luminosity)
