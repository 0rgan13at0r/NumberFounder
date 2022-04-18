#!/usr/bin/env python3

import re
import time
import pyperclip
import argparse


def output_file(file: str = None, data: str = None):
    """
    Write data in user's file.
    """
    with open(file, "a") as file_f:
        file_f.write(data)


def parse_clipboard(regular: str = None, output: bool = False):
    """Parse clipboard"""

    numbers_count = 0

    for number in re.findall(regular, pyperclip.paste()):
        time.sleep(0.03)

        print(f"Found: {'-'.join(number)}")
        numbers_count += 1

        if output:
            output_file(args.output, f"{'-'.join(number)}\n")


    print(f"\nDone\tNumbers count: {numbers_count}")


def parse_text_file(regular: str = None, text_file: str = None, output: bool = False):
    """Parse text file"""

    numbers_count = 0
    
    try:
        with open(text_file, "r") as file:

            for number in re.findall(regular, file.read()):
                time.sleep(0.03)

                print(f"Found: {'-'.join(number)}")
                numbers_count += 1

                if output:
                    output_file(args.output, f"{'-'.join(number)}\n")

            print(f"\nDone\tNumbers count: {numbers_count}")

    except FileNotFoundError:
        print("File not found!")


def main():
    phones_re = re.compile(
        r"""(\+375|80)?  # Country's code
        \S?             # Delimiter
        (\d{2})         # City's code
        \S?             # Delimiter
        (\d{7})""",     # Other digits
        re.VERBOSE)

    if args.clipboard:
        parse_clipboard(phones_re, output=args.output)

    elif args.file:
        parse_text_file(phones_re, args.file, output=args.output)

    else:
        parser.print_help()


if __name__ == '__main__':

    # Create command line parser
    parser = argparse.ArgumentParser(
        prog="NumberFounder.py",
        description="Usage for parsing text or clipboard for found phones number.",
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--clipboard", action="store_true", help="Usage clipboard for parsing numbers.",)
    group.add_argument("--file", help="Usage text file for parsing numbers.", metavar="FILE",)

    parser.add_argument("-o", "--output", help="Output in file", type=str, metavar="FILE", default=False)

    args = parser.parse_args()

    try:
        main()
    except KeyboardInterrupt:
        print("\nCanceled")