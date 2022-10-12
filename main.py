#!/usr/bin/env python3

import argparse
import os
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pdftxtprettier",
        description="Prettier the extracted text from PDF.",
    )
    parser.add_argument(
        action="store", dest="input", help="input filename", metavar="[INPUT]", nargs=1
    )
    parser.add_argument(
        "--output",
        action="store",
        dest="output",
        help="output filename",
        metavar="--output",
        nargs=1,
        required=False,
    )
    parser.add_argument(
        "--overwrite", action="store_true", dest="overwrite", default=False
    )
    args = parser.parse_args()

    if not os.path.exists(args.input[0]):
        sys.stderr.write(parser.prog + ": ")
        sys.stderr.write("Error: the given input filename is not exist.")
        sys.stderr.write("\n")

    paragraph = ""

    with open(args.input[0]) as f:
        for line in f:
            line = line.strip()
            for i, c in enumerate(line):
                # Insert a brank line if the line ends with the end of the sentence.
                paragraph += line
                if i == (len(line) - 1) and (c == "." or c == "。"):
                    paragraph += "\n"
                    paragraph = ""
