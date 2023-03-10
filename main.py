#!/usr/bin/env python3

from wcwidth import wcswidth
from typing import List

import argparse
import io
import os
import sys


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
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
    args: argparse.Namespace = parser.parse_args()

    if args.overwrite:
        args.output[0] = args.input[0]

    if not os.path.exists(args.input[0]):
        sys.stderr.write(parser.prog + ": ")
        sys.stderr.write("Error: the given input filename is not exist.")
        sys.stderr.write("\n")

    paragraph: str = ""

    s: io.StringIO = io.StringIO("")

    around_width: List[int] = [0, 0, 0]
    with open(args.input[0]) as f:
        for line in f:
            line = line.strip()
            for i, c in enumerate(line):
                if i < len(line) - 1:
                    around_width = [around_width[1], wcswidth(c), wcswidth(line[i + 1])]
                    # If `c` is an odd space, skip that.
                    if c == " " and around_width[0] == 2 and around_width[2] == 2:
                        c = ""
                # Insert a brank line if the line ends with the end of the sentence.
                paragraph += c
                if i == (len(line) - 1) and (c == "." or c == "。"):
                    paragraph += "\n"
                    s.write(paragraph + "\n")
                    paragraph = ""
    
    s.seek(0)

    with open(args.output[0], mode="w") as f:
        for line in s:
            f.write(line)
