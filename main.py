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
        dest="input", help="input filename", action="store", metavar="[INPUT]", nargs=1
    )
    parser.add_argument(
        dest="output",
        help="output filename",
        action="store",
        metavar="[OUTPUT]",
        nargs=1,
    )
    parser.add_argument(
        "--overwrite", dest="overwrite", action="store_true", default=False
    )
    args = parser.parse_args()

    if not os.path.Exist(args.input):
        sys.exit(1)
