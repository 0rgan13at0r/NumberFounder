#!/usr/bin/env python3

import re
import logging
import time
import pyperclip
import sys
import argparse


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s---%(levelname)s---%(message)s")
# logging.disable(logging.CRITICAL)


def parse_clipboard(regular=None):
    """Parse clipboard"""

    numbers_count = 0

    for number in re.findall(regular, pyperclip.paste()):
        time.sleep(0.03)

        print(f"Found: +375-{''.join(number)}")
        numbers_count += 1

    print(f"\nDone\tNumbers count: {numbers_count}")


def parse_text_file(regular=None, text_file=None):
    """Parse text file"""

    numbers_count = 0
    
    try:
        with open(text_file, "r") as file:

            for number in re.findall(regular, file.read()):
                time.sleep(0.03)

                print(f"Found: +375-{''.join(number)}")
                numbers_count += 1

            print(f"\nDone\tNumbers count: {numbers_count}")

    except FileNotFoundError:
        logging.error("File not founded")


def main():
    phones_re = re.compile(r"\d{2}-\d{7}")  # Regular variable for phones

    if args.clipboard:
        parse_clipboard(phones_re)
    elif args.file:
        parse_text_file(phones_re, args.file)


if __name__ == '__main__':

    # Create command line parser
    parser = argparse.ArgumentParser(
        prog="NumberFounder.py",
        description="Usage for parsing text or clipboard for found phones number.",
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--clipboard", action="store_true", help="Usage clipboard for parsing numbers.",)
    group.add_argument("--file", help="Usage text file for parsing numbers.", metavar="FILE",)

    args = parser.parse_args()

    try:
        main()
    except KeyboardInterrupt:
        logging.info("Canceled")